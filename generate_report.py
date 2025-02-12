import argparse
import concurrent.futures
import json
import os
import random
from enum import Enum

import openai
from tqdm import tqdm

from generate_acd_tasks import get_task_summary, load_task_family
from src.acd_report_prompts import (
    get_make_report_init_prompt,
    get_task_example_str,
    get_selected_surprising_examples,
    get_overall_summary_prompt,
    human_difficulty_to_str,
)
from src.llm_infer_cluster_labels import infer_cluster_labels
from src.llm_utils import get_response_from_llm, extract_json_between_markers

# Set OpenAI API key as an environment variable
client = openai.OpenAI()


def get_model_full_name(model):
    if model.startswith("gpt4"):
        return "gpt-4o-2024-08-06"
    elif model.startswith("claude"):
        return (
            "bedrock/anthropic.claude-3-5-sonnet-20240620-v1:0"
            if os.environ.get("AWS_ACCESS_KEY_ID")
            else "claude-3-5-sonnet-20240620"
        )
    else:
        return model


class TaskLabel(Enum):
    BASE = 1
    SUCCESS = 2
    FAILURE = 3
    SURPRISING_SUCCESS = 4
    SURPRISING_FAILURE = 5


class Task:
    def __init__(
        self,
        dir: str,
        base_task: bool,
    ):
        self.dir = dir
        self.task_summary = get_task_summary(dir)
        task_json_path = os.path.join(dir, "task.json")
        metadata_path = os.path.join(dir, "metadata.json")
        with open(task_json_path, "r") as f:
            self.task_json = json.load(f)
        with open(metadata_path, "r") as f:
            self.metadata = json.load(f)

        if base_task:
            raise AssertionError("do not count base task")
        else:
            self.name = self.task_json["name_of_task"]
            self.surprising = self.metadata.get("surprising", "no") == "yes"
            self.accepted = self.metadata.get("accepted", "no") == "yes"
            if self.surprising:
                if self.accepted:
                    self.label = TaskLabel.SURPRISING_SUCCESS
                else:
                    self.label = TaskLabel.SURPRISING_FAILURE
            else:
                if self.accepted:
                    self.label = TaskLabel.SUCCESS
                else:
                    self.label = TaskLabel.FAILURE

        self.embedding = self.metadata.get("embedding", None)
        self.eval_answers = self.metadata.get("eval_answers", [])

        task_family = load_task_family(dir)()
        tasks = task_family.get_tasks()
        self.instructions = [task_family.get_instructions(t) for t in tasks.values()]
        self.difficulty = int(self.task_json["estimated_human_difficulty"])
        self.success_rate = self.metadata["success_rate"]
        if self.label != TaskLabel.BASE:
            self.idx = self.metadata["gen_num"]
        else:
            self.idx = 0

        self.example_str = get_task_example_str(self)

    def to_dict(self):
        return {
            "task_json": self.task_json,
            "metadata": self.metadata,
            "instructions": self.instructions,
        }


def generate_cluster_analysis(cluster_info, scientist_model):
    (
        example_selection_system_msg,
        example_selection_formatted_prompt,
    ) = get_selected_surprising_examples(cluster_info)
    response, msg_history = get_response_from_llm(
        msg=example_selection_formatted_prompt,
        client=client,
        model=scientist_model,
        system_message=example_selection_system_msg,
        print_debug=False,
        msg_history=None,
    )
    surprising_idx_json = extract_json_between_markers(response)
    if not (
        surprising_idx_json["surprising_success_example_idx"]
        + surprising_idx_json["surprising_failure_example_idx"]
    ):
        return None
    cluster_info["surprising_tasks"] = [
        cluster_info["all_examples"][idx - 1]
        for idx in surprising_idx_json["surprising_success_example_idx"]
        + surprising_idx_json["surprising_failure_example_idx"]
    ]
    cluster_analysis_system_msg, cluster_analysis_prompt = get_make_report_init_prompt(
        cluster_info
    )
    response, msg_history = get_response_from_llm(
        msg=cluster_analysis_prompt,
        client=client,
        model=scientist_model,
        system_message=cluster_analysis_system_msg,
        print_debug=False,
        msg_history=None,
    )
    response = extract_json_between_markers(response)
    for idx, task in enumerate(cluster_info["surprising_tasks"]):
        response[f"surprising_example_{idx + 1}"] = task.example_str
    return response


def process_cluster(cluster_id, tasks, scientist_model):
    if cluster_id == -1:  # Skip noise cluster
        return cluster_id, None

    # Calculate overall success rate using eval scores
    total_score = 0
    total_count = 0
    for task in tasks:
        if task.label != TaskLabel.BASE:  # Exclude base tasks
            total_count += 1
            # Average the 0/1 scores across all examples
            scores_array = task.metadata["eval_scores"]
            task_score = sum(
                sum(example_scores) for example_scores in scores_array
            ) / sum(len(example_scores) for example_scores in scores_array)
            total_score += task_score

    # Calculate success rates by difficulty
    difficulty_counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    difficulty_scores = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    for task in tasks:
        if task.label != TaskLabel.BASE:
            difficulty_counts[task.difficulty] += 1
            scores_array = task.metadata["eval_scores"]
            task_score = sum(
                sum(example_scores) for example_scores in scores_array
            ) / sum(len(example_scores) for example_scores in scores_array)
            difficulty_scores[task.difficulty] += task_score

    difficulty_success_rates = {}
    for diff in range(1, 6):
        if difficulty_counts[diff] > 0:
            difficulty_success_rates[diff] = (
                difficulty_scores[diff] / difficulty_counts[diff]
            )
        else:
            difficulty_success_rates[diff] = None

    # Calculate percentage of tasks at each difficulty level
    difficulty_percentages = {}
    for diff in range(1, 6):
        if total_count > 0:
            difficulty_percentages[
                diff
            ] = f"{difficulty_counts[diff] / total_count * 100:.1f}%"
        else:
            difficulty_percentages[diff] = "0%"

    cluster_name = tasks[0].cluster_label
    success_rate = total_score / total_count if total_count > 0 else 0

    cluster_info = {
        "cluster_name": cluster_name,
        "success_rate": success_rate,
        "num_tasks": total_count,
        "difficulty_success_rates": difficulty_success_rates,
        "difficulty_percentages": difficulty_percentages,
        "task_names": list(set(task.name for task in tasks)),
        "capabilities": tasks[0].cluster_capability,
    }

    # Find top 3 surprising failure/success tasks
    failure_tasks = []
    success_tasks = []

    for task in tasks:
        if task.label == TaskLabel.SURPRISING_FAILURE:
            failure_tasks.append((task.difficulty, task.success_rate, task))
        elif task.label == TaskLabel.SURPRISING_SUCCESS:
            success_tasks.append((task.difficulty, task.success_rate, task))

    # Sort failures by ascending difficulty
    failure_tasks.sort(key=lambda x: x[0])
    # Sort successes by descending difficulty
    success_tasks.sort(key=lambda x: -x[0])

    # Take top 10 of each, prioritizing difficulty ranking while avoiding duplicates
    seen_failure_names = set()
    filtered_failures = []
    for diff, rate, task in failure_tasks:
        if len(filtered_failures) >= 10:
            break
        if task.name not in seen_failure_names:
            filtered_failures.append(task)
            seen_failure_names.add(task.name)

    seen_success_names = set()
    filtered_successes = []
    for diff, rate, task in success_tasks:
        if len(filtered_successes) >= 10:
            break
        if task.name not in seen_success_names:
            filtered_successes.append(task)
            seen_success_names.add(task.name)

    all_examples = filtered_failures + filtered_successes
    random.shuffle(all_examples)
    cluster_info["all_examples"] = all_examples

    cluster_info["analysis"] = generate_cluster_analysis(cluster_info, scientist_model)
    return cluster_id, cluster_info


def write_cluster_analysis(
    task_folder, acd_name, scientist_model, clustering_results, cluster_analysis_path
):
    # Load generated tasks
    generation_task_archive = [
        os.path.join(task_folder, f)
        for f in os.listdir(task_folder)
        if os.path.isdir(os.path.join(task_folder, f))
    ]
    print(f"Generation task families size: {len(generation_task_archive)}")

    tasks = []
    for dir in generation_task_archive:
        task = Task(dir, base_task=False)
        if task.embedding is not None:
            tasks.append(task)

    cluster = {}
    for task in tasks:
        matching_result = next(
            (r for r in clustering_results if r["dir"] == task.dir), None
        )
        if matching_result:
            task.cluster = matching_result["cluster"]
            task.cluster_label = matching_result["cluster_label"]
            task.cluster_capability = matching_result["cluster_capability"]
        else:
            raise AssertionError("no matched entry")
        if task.cluster not in cluster:
            cluster[task.cluster] = [task]
        else:
            cluster[task.cluster].append(task)

    cluster_info = {}

    with concurrent.futures.ThreadPoolExecutor(max_workers=25) as executor:
        future_to_cluster = {
            executor.submit(
                process_cluster, cluster_id, tasks, scientist_model
            ): cluster_id
            for cluster_id, tasks in cluster.items()
        }
        for future in tqdm(
            concurrent.futures.as_completed(future_to_cluster),
            total=len(cluster),
            desc="Analyzing clusters",
        ):
            cluster_id = future_to_cluster[future]
            try:
                cluster_id, info = future.result()
                if info:
                    cluster_info[cluster_id] = info
            except Exception as e:
                print(f"Error processing cluster {cluster_id}: {e}")

    # Save cluster info to JSON file
    serializable_cluster_info = {
        cluster_id: {
            "cluster_name": info["cluster_name"],
            "capabilities": info["capabilities"],
            "task_names": info["task_names"],
            "num_tasks": info["num_tasks"],
            "success_rate": info["success_rate"],
            "difficulty_percentages": info["difficulty_percentages"],
            "difficulty_success_rates": info["difficulty_success_rates"],
            "analysis": info["analysis"],
        }
        for cluster_id, info in cluster_info.items()
    }
    if not os.path.exists(os.path.dirname(cluster_analysis_path)):
        os.makedirs(os.path.dirname(cluster_analysis_path))
    output_path = cluster_analysis_path
    with open(output_path, "w") as f:
        json.dump(serializable_cluster_info, f, indent=4)
    print(f"Saved cluster analysis to {output_path}")
    return serializable_cluster_info


def write_overall_summary(
    acd_name, scientist_model, overall_summary_path, all_cluster_info
):
    overall_summary_system_msg, overall_summary_prompt = get_overall_summary_prompt(
        all_cluster_info, acd_name
    )
    response, msg_history = get_response_from_llm(
        msg=overall_summary_prompt,
        client=client,
        model=scientist_model,
        system_message=overall_summary_system_msg,
        print_debug=False,
        msg_history=None,
    )
    overall_summary = extract_json_between_markers(response)

    with open(overall_summary_path, "w") as f:
        json.dump(overall_summary, f, indent=4)
    print(f"Saved overall summary to {overall_summary_path}")
    return overall_summary


def create_hyper_link_text_base(text, all_cluster_info):
    import re

    # Create a map of cluster tags to hyperlinks, removing special characters except hyphens, spaces, and commas
    cluster_name_map = {}
    for i, info in all_cluster_info.items():
        clean_name = re.sub(r"[^a-zA-Z0-9\s-]", "", info["cluster_name"])
        hyperlink = f"[{info['cluster_name']}](#{clean_name.lower().replace(' ', '-')})"
        cluster_name_map[f"#Cluster_{i}"] = hyperlink

    # Sort the cluster name map keys from high to low to prevent partial replacements
    for cluster_tag in sorted(
        cluster_name_map.keys(), key=lambda x: int(x.split("_")[1]), reverse=True
    ):
        text = text.replace(cluster_tag, cluster_name_map[cluster_tag])

    return text


MODEL_NAME = {"gpt4": "GPT-4o", "llama": "Llama-8B", "sonnet": "Claude 3.5 Sonnet"}


def convert_to_markdown(
    task_folder, acd_name, clustering_labels_path, all_cluster_info, overall_summary
):
    from datetime import datetime

    # Get the current year and month
    current_year = datetime.now().year
    current_month = datetime.now().month
    # Get the current day
    current_day = datetime.now().day

    scientist, subject = acd_name.split("_")
    try:
        scientist, subject = MODEL_NAME[scientist], MODEL_NAME[subject]
    except:
        pass

    # Generate cluster visualization
    import subprocess

    result = subprocess.run(
        [
            "python",
            "src/visualize_generated_tasks_cluster.py",
            "--acd_name",
            acd_name,
            "--task_folder",
            task_folder,
            "--clustering_labels_path",
            clustering_labels_path,
        ],
        capture_output=True,
        text=True,
    )
    print(f"Visualization script output:\n{result.stdout}")
    cluster_vis_fig_path = os.path.abspath(f"reports/cluster_vis_{acd_name}.pdf")
    if not os.path.exists(cluster_vis_fig_path):
        print(
            f"Warning: Cluster visualization figure not found at {cluster_vis_fig_path}"
        )

    # Generate cluster success rate visualization
    result = subprocess.run(
        [
            "python",
            "src/visualize_cluster_success_rate.py",
            "--acd_name",
            acd_name,
            "--clustering_labels_path",
            clustering_labels_path,
        ],
        capture_output=True,
        text=True,
    )
    print(f"Success rate visualization script output:\n{result.stdout}")
    cluster_radar_fig_path = os.path.abspath(f"reports/cluster_radar_{acd_name}.pdf")
    if not os.path.exists(cluster_radar_fig_path):
        print(f"Warning: Cluster radar figure not found at {cluster_radar_fig_path}")

    markdown_report = (
        f"""---
title: 'ACD Capability Report on {subject} Subject'
author:
- name: {scientist}
abstract: |
  {overall_summary['abstract']}
template: scientific_reports
bibliography: references.bib
...
"""
        + """
\\setcounter{tocdepth}{2}
\\tableofcontents

\\newpage
"""
    )
    create_hyper_link_text = lambda text: create_hyper_link_text_base(
        text, all_cluster_info
    )
    # Start with the overall summary
    markdown_report += f"# Overview\n\n"
    markdown_report += (
        f"{create_hyper_link_text(overall_summary['overall_summary'])}\n\n"
    )
    markdown_report += (
        f"![Visualization of task families discovered by ACD on {subject} subject by {scientist} scientist over 5000 generations.]({cluster_vis_fig_path})"
        + "{#fig:cluster width=100%}\n\n"
    )
    markdown_report += "## Insights\n"
    for insight in overall_summary["insight"]:
        markdown_report += f"- {create_hyper_link_text(insight)}\n"
    markdown_report += "\n## Surprising Capabilities\n"
    for capability in overall_summary["surprising_capabilities"]:
        markdown_report += f"- {create_hyper_link_text(capability)}\n"
    markdown_report += "\n## Surprising Failures\n"
    for failure in overall_summary["surprising_failures"]:
        markdown_report += f"- {create_hyper_link_text(failure)}\n"

    markdown_report += f"\n\n![Success rates on each cluster of tasks.]({cluster_radar_fig_path}){{#fig:radar width=55%}}\n\n"

    markdown_report += "\n## Data Insights\n"
    for insight in overall_summary["data_insights"]:
        markdown_report += f"- {create_hyper_link_text(insight)}\n"

    # Add cluster information
    markdown_report += "\n\\newpage\n# Detailed Task Analysis\n"
    for cluster_id, cluster_info in all_cluster_info.items():
        if not cluster_info["analysis"]:
            continue
        markdown_report += f"## {cluster_info['cluster_name']}\n\n"
        markdown_report += f"### Overview\n\n"
        markdown_report += f"**Capabilities**: {cluster_info['capabilities']}\n\n"
        markdown_report += f"**Number of Tasks**: {cluster_info['num_tasks']}\n\n"
        markdown_report += f"**Success Rate**: {cluster_info['success_rate']:.2%}\n"
        markdown_report += "\n**Difficulty Success Rates**:\n"
        for difficulty, rate in cluster_info["difficulty_success_rates"].items():
            if not rate:
                continue
            markdown_report += (
                f"- {human_difficulty_to_str[str(difficulty)]}: {rate:.2%}\n"
            )
        markdown_report += "\n**Difficulty Percentages**:\n"
        for difficulty, percentage in cluster_info["difficulty_percentages"].items():
            if "0.0" in percentage:
                continue
            markdown_report += (
                f"- {human_difficulty_to_str[str(difficulty)]}: {percentage}\n\n"
            )
        markdown_report += f"### Analysis\n\n"
        markdown_report += f"{cluster_info['analysis']['overall_analysis']}\n"
        markdown_report += "\n**Insights**:\n\n"
        markdown_report += f"{cluster_info['analysis']['insights']}\n\n"
        markdown_report += f"### Task Examples\n"
        idx = 1
        for i in range(1, 7):
            example_key = f"surprising_example_{i}"
            analysis_key = f"surprising_example_analysis_{i}"
            if analysis_key in cluster_info["analysis"]:
                markdown_report += f"#### Example {idx}\n"
                idx += 1
                examples = (
                    cluster_info["analysis"][example_key]
                    .replace("\n", "\n> ")
                    .replace("###", "\n> ###")
                )
                markdown_report += f"> {examples}\n\n"
                markdown_report += f"{cluster_info['analysis'][analysis_key].replace(f'Example {i}', f'Example {idx}')}\n\n"

    return markdown_report


def main():
    parser = argparse.ArgumentParser(description="Generate report for ACD")
    parser.add_argument("--task_folder", type=str, help="Task folder path")
    parser.add_argument("--scientist", type=str, default="gpt4", help="Scientist name")
    parser.add_argument(
        "--subject", type=str, default="gpt4", help="Subject model name"
    )
    args = parser.parse_args()

    if not os.path.exists(args.task_folder):
        raise FileNotFoundError(f"Task folder '{args.task_folder}' does not exist")

    acd_name = f"{args.scientist}_{args.subject}"
    scientist_model = get_model_full_name(args.scientist)

    clustering_labels_path = os.path.join(
        args.task_folder, f"clustering_results_{acd_name}.json"
    )

    if not os.path.exists(clustering_labels_path):
        infer_cluster_labels(args.task_folder, clustering_labels_path, scientist_model)
    else:
        print(f"Found clustering results at {clustering_labels_path}")

    # Read clustering results from JSON file
    with open(clustering_labels_path, "r") as f:
        clustering_results = json.load(f)

    cluster_analysis_path = f"reports/{acd_name}/cluster_analysis.json"
    if not os.path.exists(cluster_analysis_path):
        all_cluster_info = write_cluster_analysis(
            args.task_folder,
            acd_name,
            scientist_model,
            clustering_results,
            cluster_analysis_path,
        )
    else:
        print(f"Loading existing cluster analysis from {cluster_analysis_path}")
        with open(cluster_analysis_path, "r") as f:
            all_cluster_info = json.load(f)

    overall_summary_path = f"reports/{acd_name}/overall_summary.json"
    if not os.path.exists(overall_summary_path):
        overall_summary = write_overall_summary(
            acd_name, scientist_model, overall_summary_path, all_cluster_info
        )
    else:
        print(f"Loading existing overall summary from {overall_summary_path}")
        with open(overall_summary_path, "r") as f:
            overall_summary = json.load(f)

    overall_summary_md_path = f"reports/{acd_name}/report.md"

    if not os.path.exists(overall_summary_md_path):
        overall_summary_md = convert_to_markdown(
            args.task_folder,
            acd_name,
            clustering_labels_path,
            all_cluster_info,
            overall_summary,
        )
        with open(overall_summary_md_path, "w") as f:
            f.write(overall_summary_md)
        print(
            f"Converted overall summary to markdown and saved to {overall_summary_md_path}"
        )
    else:
        print(f"Markdown summary already exists at {overall_summary_md_path}")


if __name__ == "__main__":
    main()
