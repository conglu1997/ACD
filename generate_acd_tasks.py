import argparse
import concurrent.futures
import importlib.util
import json
import os
import pathlib
import random
import re
import shutil
import sys
import tempfile
import threading
from typing import Optional, Tuple, List, Any

import numpy as np
import openai

from src.acd_prompts import (
    initial_task_prompt,
    task_creation_system_msg,
    task_creation_reflexion_prompt,
    task_embedding_prompt,
    eval_zs_system_msg,
    eval_cot_system_msg,
)
from src.llm_utils import (
    get_response_from_llm,
    get_batch_responses_from_llm,
    get_embedding,
    extract_json_between_markers,
    create_client,
    AVAILABLE_LLMS,
)
from src.task_filter import eval_task_interestingness, eval_task_surprisingness

# Always use OpenAI embeddings.
embedding_client = openai.OpenAI()


def embedding_cosine_similarity(
    embedding1: list[float], embedding2: list[float]
) -> float:
    norm1 = np.linalg.norm(embedding1)
    norm2 = np.linalg.norm(embedding2)
    if norm1 == 0 or norm2 == 0:
        return 0.0  # Or handle as appropriate
    return np.dot(embedding1, embedding2) / (norm1 * norm2)


def sample_from_archive(
    archive: list[str], random_instance: random.Random
) -> tuple[str, str, str]:
    task = random_instance.choice(archive)
    task_python_file = os.path.join(task, "task.py")
    task_json_descriptor = os.path.join(task, "task.json")
    return task, task_python_file, task_json_descriptor


def update_metadata(task_dir: str, new_metadata: dict):
    metadata_path = os.path.join(task_dir, "metadata.json")
    # Read existing metadata
    if os.path.exists(metadata_path):
        with open(metadata_path, "r") as f:
            metadata = json.load(f)
    else:
        metadata = {}
    # Update metadata
    metadata.update(new_metadata)
    # Write updated metadata back to file
    with open(metadata_path, "w") as f:
        json.dump(metadata, f, indent=4)


def save_task_to_disk(
    new_task_dir: str, response: dict, metadata: Optional[dict] = None
):
    if metadata is None:
        metadata = {}
    new_task_code = response["task_family"]
    new_task_python_file = os.path.join(new_task_dir, "task.py")
    new_task_json_descriptor = os.path.join(new_task_dir, "task.json")
    with open(new_task_python_file, "w") as f:
        f.write(str(new_task_code))

    with open(new_task_json_descriptor, "w") as f:
        response_filtered = {
            k: v
            for k, v in response.items()
            if k
            in [
                "name_of_task",
                "description_of_task",
                "capability_being_measured",
                "estimated_human_difficulty",
            ]
        }
        json.dump(response_filtered, f, indent=4)

    if metadata:
        update_metadata(new_task_dir, metadata)


def load_task_family(task_dir: str):
    task_module_path = os.path.join(task_dir, "task.py")
    module_name = f"task_{os.path.basename(task_dir)}"
    spec = importlib.util.spec_from_file_location(module_name, task_module_path)
    task_module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = task_module
    spec.loader.exec_module(task_module)
    task_family = task_module.TaskFamily

    # Check task family has required methods.
    for method in ["get_tasks", "get_instructions", "score"]:
        if not hasattr(task_family, method):
            raise AttributeError(f"Task family must define a {method} method.")

    return task_family


def eval_agent_on_task(
    task_family: Any,
    args: argparse.Namespace,
    client: Any,
    client_model: str,
    n_shot: int = 1,
) -> Tuple[float, List[List[str]], List[List[str]], List[List[float]]]:
    task = task_family()
    scores = []
    all_answers = []
    all_submissions = []

    for j, (_, task_data) in enumerate(task.get_tasks().items()):
        task_scores = []
        instructions = task.get_instructions(task_data)
        if args.eval_agent_type == "zs":
            eval_system_msg = eval_zs_system_msg
        elif args.eval_agent_type == "cot":
            eval_system_msg = eval_cot_system_msg
        else:
            raise ValueError(f"Unknown eval_agent_type: {args.eval_agent_type}")
        submissions, _ = get_batch_responses_from_llm(
            msg=instructions,
            client=client,
            model=client_model,
            system_message=eval_system_msg,
            print_debug=args.print_llm_debug,
            n_responses=n_shot,
        )
        all_submissions.append(submissions)
        answers = []
        for submission in submissions:
            match = re.search(
                r"^Answer:\s*(.*)", submission, re.IGNORECASE | re.MULTILINE | re.DOTALL
            )
            if match:
                answer = match.group(1).strip()
                answers.append(answer)
            else:
                # If 'Answer:' is not found, use the entire submission
                answers.append(submission.strip())
        all_answers.append(answers)
        for i, ans in enumerate(answers):
            score = task.score(task_data, ans)
            assert 0 <= score <= 1, f"Invalid score: {score}"
            if score < 1:
                score = 0
            task_scores.append(score)
        scores.append(task_scores)

    # avg across tasks
    avg_score = float(
        np.mean(np.array([score for task_scores in scores for score in task_scores]))
    )
    return avg_score, all_answers, all_submissions, scores


def eval_proposal(response: dict, args, client, client_model) -> tuple[str, bool]:
    # Return LLM output or error, along with success.

    with tempfile.TemporaryDirectory() as anon_dir:
        # Ensure all required fields exist.
        required_fields = [
            "name_of_task",
            "description_of_task",
            "capability_being_measured",
            "estimated_human_difficulty",
            "task_family",
            "done",
        ]
        for field in required_fields:
            if field not in response:
                return f"Field {field} missing from response.", False

        # Ensure estimated human difficulty is valid
        if str(response["estimated_human_difficulty"]) not in ["1", "2", "3", "4", "5"]:
            return (
                f"Invalid estimated_human_difficulty: {response['estimated_human_difficulty']}, must be 1-5.",
                False,
            )

        # Save to disk first.
        try:
            save_task_to_disk(anon_dir, response)
        except Exception as e:
            return f"Error while saving task to disk: {e}", False

        # Load and run task.
        try:
            task_family = load_task_family(anon_dir)
        except Exception as e:
            return f"Error while loading task: {e}", False

        # Evaluate task.
        try:
            # For now, only take the score for the task, don't return exact answer.
            avg_score, *_ = eval_agent_on_task(task_family, args, client, client_model)
        except Exception as e:
            return f"Error while evaluating task: {e}", False

        return f"Task run successfully. Agent achieved score: {avg_score:.1f}/1.0", True


def discover_next_task(
    prev_python_file: str,
    prev_json_descriptor: str,
    other_tasks: list[str],
    args,
    scientist_client,
    scientist_client_model,
    subject_client,
    subject_client_model,
    gen_num: int,
) -> tuple[Optional[dict], List]:
    # Read files.
    with open(prev_python_file, "r") as f:
        prev_python = f.read()
    with open(prev_json_descriptor, "r") as f:
        prev_json = json.load(f)

    prev_json["task_family"] = prev_python
    prev_task_name = prev_json["name_of_task"]
    prev_json_str = json.dumps(prev_json, indent=4)
    msg_history = []

    # Initial response.
    try:
        response, msg_history = get_response_from_llm(
            msg=initial_task_prompt.format(
                prev_json=prev_json_str, other_task_jsons="\n\n".join(other_tasks)
            ),
            client=scientist_client,
            model=scientist_client_model,
            system_message=task_creation_system_msg.format(
                num_rounds=args.max_generation_reflections
            ),
            print_debug=args.print_llm_debug,
            msg_history=msg_history,
        )
        response = extract_json_between_markers(response)

        # Iteratively improve task with feedback.
        if args.max_generation_reflections > 1:
            success = False
            for j in range(args.max_generation_reflections - 1):
                eval_response, _ = eval_proposal(
                    response, args, subject_client, subject_client_model
                )
                response, msg_history = get_response_from_llm(
                    msg=task_creation_reflexion_prompt.format(
                        current_round=j + 2,
                        num_rounds=args.max_generation_reflections,
                        eval_response=eval_response,
                    ),
                    client=scientist_client,
                    model=scientist_client_model,
                    system_message=task_creation_system_msg.format(
                        num_rounds=args.max_generation_reflections
                    ),
                    print_debug=args.print_llm_debug,
                    msg_history=msg_history,
                )
                response = extract_json_between_markers(response)
                if response.get("done", "False").lower() == "true":
                    print(
                        f"Thread {gen_num}: Task generation converged after {j + 2} self-reflection rounds."
                    )
                    success = True
                    break

            if not success:
                print(
                    f"Thread {gen_num}: Task generation did not converge after {args.max_generation_reflections} rounds."
                )
                return None, []

    except Exception as e:
        print(
            f"Thread {gen_num}: Error while generating task from {prev_task_name}: {e}"
        )
        return None, []

    return response, msg_history


def get_task_summary(task_dir: str) -> str:
    # Load task JSON descriptor.
    with open(os.path.join(task_dir, "task.json"), "r") as f:
        task_json = json.load(f)

    # Get success from metadata.
    metadata_path = os.path.join(task_dir, "metadata.json")
    if os.path.exists(metadata_path):
        with open(metadata_path, "r") as f:
            metadata = json.load(f)
        # Base tasks have no accepted string but do succeed.
        agent_success_string = metadata.get("accepted", "yes")
    else:
        agent_success_string = "yes"

    human_difficulty_to_str = {
        "1": "very easy",
        "2": "easy",
        "3": "moderate",
        "4": "difficult",
        "5": "very difficult",
    }

    # Get first question.
    task_family = load_task_family(task_dir)()
    tasks = task_family.get_tasks()
    instruction = [task_family.get_instructions(t) for t in tasks.values()][0]

    formatted_prompt = task_embedding_prompt.format(
        name_of_task=task_json["name_of_task"],
        description_of_task=task_json["description_of_task"],
        capability_being_measured=task_json["capability_being_measured"],
        estimated_human_difficulty=human_difficulty_to_str[
            task_json["estimated_human_difficulty"]
        ],
        example_question=instruction,
        agent_succeeded=agent_success_string,
    )

    return formatted_prompt


def maybe_create_task_embedding(
    task_dir: str,
    force_new: bool = False,  # only needed if prompts changed for embeddings
) -> list[float]:
    metadata_path = os.path.join(task_dir, "metadata.json")
    # Read existing metadata
    if os.path.exists(metadata_path):
        with open(metadata_path, "r") as f:
            metadata = json.load(f)
    else:
        metadata = {}

    if not force_new and "embedding" in metadata:
        return metadata["embedding"]

    formatted_prompt = get_task_summary(task_dir)
    embedding = get_embedding(embedding_client, formatted_prompt)

    # Update metadata with the new embedding
    update_metadata(task_dir, {"embedding": embedding})

    return embedding


def get_closest_tasks(
    current_embedding: list[float],
    task_names: list[str],
    embeddings: list[list[float]],
    n: int = 5,
) -> list[str]:
    if len(task_names) != len(embeddings):
        raise ValueError("Length of task_names and embeddings must match.")
    if not task_names or not embeddings:
        return []  # Handle empty input lists

    distances = [
        embedding_cosine_similarity(current_embedding, emb) for emb in embeddings
    ]
    # Sort and get top n-closest tasks (i.e. highest cosine similarity)
    indices = np.argsort(distances)[::-1][:n]
    closest_tasks = [task_names[i] for i in indices]
    return closest_tasks


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--base_dir", type=str, default="seed_tasks")
    parser.add_argument("--print_llm_debug", action="store_true", default=False)
    parser.add_argument("--output_dir", type=str, default="experiment_dir")
    parser.add_argument(
        "--resume_dir",
        type=str,
        default=None,
        help="Path to existing output directory to resume from",
    )
    parser.add_argument("--num_generations", type=int, default=5000)
    parser.add_argument("--max_generation_reflections", type=int, default=5)
    parser.add_argument("--eval_n_shot", type=int, default=5)
    parser.add_argument("--eval_threshold", type=float, default=0.6)
    parser.add_argument("--num_neighbours_interesting", type=int, default=5)
    parser.add_argument("--num_neighbours_context", type=int, default=10)
    parser.add_argument("--force_new_embeddings", action="store_true", default=False)
    parser.add_argument(
        "--eval_agent_type", type=str, default="cot", choices=["zs", "cot"]
    )
    parser.add_argument(
        "--scientist_model",
        type=str,
        default="gpt-4o-2024-05-13",
        choices=AVAILABLE_LLMS,
    )
    parser.add_argument(
        "--subject_model", type=str, default="gpt-4o-2024-05-13", choices=AVAILABLE_LLMS
    )
    parser.add_argument(
        "--filter_model",
        type=str,
        default="gpt-4o-2024-05-13",
        choices=AVAILABLE_LLMS,
        help="Model to use for interestingness and surprise evaluations",
    )
    parser.add_argument(
        "--parallelism",
        action="store_true",
        default=False,
        help="Enable parallel generation",
    )
    args = parser.parse_args()

    # Create client
    scientist_client, scientist_client_model = create_client(args.scientist_model)
    subject_client, subject_client_model = create_client(args.subject_model)

    # Determine number of workers
    if args.parallelism:
        num_workers = min(os.cpu_count(), 10)
        print(f"Parallelism enabled with {num_workers} worker threads.")
    else:
        num_workers = 1
        print("Parallelism disabled. Running sequentially.")

    # Create a lock for synchronous archive management.
    archive_lock = threading.Lock()

    if args.resume_dir:
        output_dir = args.resume_dir
        print(f"Resuming from output directory: {output_dir}")
    else:
        output_dir = f"results/{args.output_dir}"
        pathlib.Path(output_dir).mkdir(parents=True, exist_ok=True)
        print(f"Output directory: {output_dir}")

    # Create the archive and load the base tasks.
    task_archive = [
        os.path.join(args.base_dir, f)
        for f in os.listdir(args.base_dir)
        if os.path.isdir(os.path.join(args.base_dir, f))
    ]
    print(f"Base task families: {task_archive}", flush=True)

    # Task embeddings
    task_embeddings = [
        maybe_create_task_embedding(task_dir, force_new=args.force_new_embeddings)
        for task_dir in task_archive
    ]

    # Load existing tasks if resuming
    failed_archive = []
    failed_embeddings = []
    if args.resume_dir:
        existing_tasks = [
            os.path.join(output_dir, f)
            for f in os.listdir(output_dir)
            if os.path.isdir(os.path.join(output_dir, f))
        ]
        print(f"Resuming with existing tasks: {existing_tasks}")
        task_archive.extend(existing_tasks)
        task_embeddings.extend(
            [
                maybe_create_task_embedding(
                    task_dir, force_new=args.force_new_embeddings
                )
                for task_dir in existing_tasks
            ]
        )
        existing_gen_nums = []
        for task_dir in existing_tasks:
            match = re.search(r"task_(\d+)_", os.path.basename(task_dir))
            if match:
                gen_num = int(match.group(1))
                existing_gen_nums.append(int(gen_num))
        if existing_gen_nums:
            starting_gen_num = max(existing_gen_nums) + 1
        else:
            starting_gen_num = 0
    else:
        starting_gen_num = 0

    # Total number of generations to perform
    total_generations = args.num_generations

    # Function to sanitize filenames
    def sanitize_filename(name):
        return re.sub(r'[<>:"/\\|?*]', "_", name)

    # Worker function
    def generate_task(
        gen_num,
        task_archive,
        failed_archive,
        args,
        scientist_client,
        scientist_client_model,
        subject_client,
        subject_client_model,
        output_dir,
    ):
        # Create a unique random instance for this thread
        thread_id = threading.get_ident()
        random_seed = gen_num + thread_id
        random_instance = random.Random(random_seed)

        print(f"Thread {gen_num}: Starting generation", flush=True)

        with archive_lock:
            (
                selected_family,
                task_python_file,
                task_json_descriptor,
            ) = sample_from_archive(task_archive, random_instance)
            idx_of_selected = task_archive.index(selected_family)
            rest_of_archive = (
                task_archive[:idx_of_selected] + task_archive[idx_of_selected + 1 :]
            )
            other_tasks = rest_of_archive + failed_archive

        print(f"Thread {gen_num}: Selected seed family: {selected_family}", flush=True)

        sampled_other_tasks = random_instance.sample(
            other_tasks, min(args.num_neighbours_context, len(other_tasks))
        )
        sampled_task_summaries = [
            get_task_summary(task_dir) for task_dir in sampled_other_tasks
        ]

        response, msg_history = discover_next_task(
            task_python_file,
            task_json_descriptor,
            sampled_task_summaries,
            args=args,
            scientist_client=scientist_client,
            scientist_client_model=scientist_client_model,
            subject_client=subject_client,
            subject_client_model=subject_client_model,
            gen_num=gen_num,
        )

        if response is None:
            print(f"Thread {gen_num}: Failed to generate task from {task_python_file}")
            return None

        # Make new folder for this task.
        new_name_of_task = response["name_of_task"]
        new_task_code = response["task_family"]

        new_task_dir = os.path.join(
            output_dir, f"task_{gen_num}_{sanitize_filename(new_name_of_task)}"
        )

        # Ensure no name conflicts.
        if os.path.exists(new_task_dir):
            print(f"Thread {gen_num}: Task already exists at {new_task_dir}. Skipping.")
            return None

        pathlib.Path(new_task_dir).mkdir(parents=True, exist_ok=True)

        # Save task to disk.
        save_task_to_disk(
            new_task_dir,
            response,
            metadata={
                "generated_from": selected_family,
                "msg_history": msg_history,
                "gen_num": gen_num,
            },
        )
        print(f"Thread {gen_num}: New task written to {new_task_dir}", flush=True)

        # Eval with the LLM agent.
        try:
            task_family = load_task_family(new_task_dir)
            success_rate, eval_answers, eval_submissions, scores = eval_agent_on_task(
                task_family,
                args,
                subject_client,
                subject_client_model,
                n_shot=args.eval_n_shot,
            )
            print(
                f"Thread {gen_num}: Evaluated {args.eval_n_shot}-shot success rate on {new_name_of_task}: {success_rate:.2f}"
            )
        except Exception as e:
            print(
                f"Thread {gen_num}: Error while performing final evaluation of {new_name_of_task}: {e}. Task removed from disk."
            )
            shutil.rmtree(new_task_dir, ignore_errors=True)
            return None

        # Update metadata with evaluation results
        task_successful = success_rate >= args.eval_threshold
        update_metadata(
            new_task_dir,
            {
                "success_rate": success_rate,
                "accepted": "yes" if task_successful else "no",
                "eval_answers": eval_answers,
                "eval_submissions": eval_submissions,
                "eval_scores": scores,
            },
        )

        return {
            "gen_num": gen_num,
            "new_task_dir": new_task_dir,
            "task_successful": task_successful,
            "new_task_code": new_task_code,
        }

    # Function to process generated tasks and perform synchronous operations
    def process_generated_task(result):
        with archive_lock:
            gen_num = result["gen_num"]
            new_task_dir = result["new_task_dir"]
            task_successful = result["task_successful"]
            new_task_code = result["new_task_code"]

            # Determine whether the task is interestingly new v.s. the archive.
            embedding = maybe_create_task_embedding(
                new_task_dir, force_new=args.force_new_embeddings
            )
            try:
                combined_archive = task_archive + failed_archive
                combined_embeddings = task_embeddings + failed_embeddings
                closest_tasks = get_closest_tasks(
                    embedding,
                    combined_archive,
                    combined_embeddings,
                    n=args.num_neighbours_interesting,
                )
                closest_task_summaries = [
                    get_task_summary(task_dir) for task_dir in closest_tasks
                ]
                decision = eval_task_interestingness(
                    new_task_summary=get_task_summary(new_task_dir),
                    closest_task_summaries=closest_task_summaries,
                    model=args.filter_model,
                    print_debug=args.print_llm_debug,
                )
            except Exception as e:
                print(f"Error while determining whether task is interestingly new: {e}")
                decision = False
            print(f"Thread {gen_num}: Task interestingly new?: {decision}")

            if not decision:
                print(
                    f"Thread {gen_num}: Task not interestingly new and removed from disk."
                )
                shutil.rmtree(new_task_dir, ignore_errors=True)
                return

            # Measure LLM surprise at the new task generated.
            try:
                surprise_decision, msg_history = eval_task_surprisingness(
                    new_task_summary=get_task_summary(new_task_dir),
                    new_task_code=new_task_code,
                    model=args.filter_model,
                    print_debug=args.print_llm_debug,
                )
            except Exception as e:
                print(
                    f"Error while determining whether task success is surprising: {e}"
                )
                surprise_decision = False
                msg_history = []
            print(f"Thread {gen_num}: LLM surprised by task?: {surprise_decision}")

            # Update metadata with surprise information
            update_metadata(
                new_task_dir,
                {
                    "surprising": "yes" if surprise_decision else "no",
                    "surprise_justification": msg_history,
                },
            )

            # Add new task to archive.
            if task_successful:
                task_archive.append(new_task_dir)
                task_embeddings.append(embedding)
                print(
                    f"Thread {gen_num}: Task added to capabilities archive. Archive size: {len(task_archive)}",
                    flush=True,
                )
            else:
                failed_archive.append(new_task_dir)
                failed_embeddings.append(embedding)
                print(
                    f"Thread {gen_num}: Agent failed at task. Failed archive size: {len(failed_archive)}",
                    flush=True,
                )

    # Generate tasks
    if num_workers > 1:
        with concurrent.futures.ThreadPoolExecutor(max_workers=num_workers) as executor:
            future_to_gen_num = {
                executor.submit(
                    generate_task,
                    gen_num,
                    task_archive,
                    failed_archive,
                    args,
                    scientist_client,
                    scientist_client_model,
                    subject_client,
                    subject_client_model,
                    output_dir,
                ): gen_num
                for gen_num in range(starting_gen_num, total_generations)
            }
            for future in concurrent.futures.as_completed(future_to_gen_num):
                gen_num = future_to_gen_num[future]
                try:
                    result = future.result()
                    if result:
                        process_generated_task(result)
                except Exception as exc:
                    print(f"Generation {gen_num} generated an exception: {exc}")
    else:
        for gen_num in range(starting_gen_num, total_generations):
            result = generate_task(
                gen_num,
                task_archive,
                failed_archive,
                args,
                scientist_client,
                scientist_client_model,
                subject_client,
                subject_client_model,
                output_dir,
            )
            if result:
                process_generated_task(result)


if __name__ == "__main__":
    main()
