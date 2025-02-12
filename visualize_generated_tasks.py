import argparse
import json
import os
import random
from enum import Enum

import numpy as np
import pandas as pd
import plotly.express as px
from sklearn.manifold import TSNE

from generate_acd_tasks import get_task_summary, load_task_family


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
            self.label = TaskLabel.BASE
            self.surprising = False
        else:
            self.surprising = self.metadata.get("surprising", "no") == "yes"
            accepted = self.metadata.get("accepted", "no") == "yes"
            if self.surprising:
                if accepted:
                    self.label = TaskLabel.SURPRISING_SUCCESS
                else:
                    self.label = TaskLabel.SURPRISING_FAILURE
            else:
                if accepted:
                    self.label = TaskLabel.SUCCESS
                else:
                    self.label = TaskLabel.FAILURE

        self.embedding = self.metadata.get("embedding", None)
        self.eval_answers = self.metadata.get("eval_answers", [])
        self.eval_scores = self.metadata.get("eval_scores", [])

        task_family = load_task_family(dir)()
        tasks = task_family.get_tasks()
        self.instructions = [task_family.get_instructions(t) for t in tasks.values()]
        if self.label != TaskLabel.BASE:
            self.idx = self.metadata["gen_num"]
        else:
            self.idx = 0

    def to_dict(self):
        return {
            "task_json": self.task_json,
            "metadata": self.metadata,
            "instructions": self.instructions,
        }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--base_dir", type=str, default="seed_tasks")
    parser.add_argument("--generation_dir", type=str, default="results/acd_gpt4o_gpt4o")
    args = parser.parse_args()

    # Load base tasks.
    base_task_archive = [
        os.path.join(args.base_dir, f)
        for f in os.listdir(args.base_dir)
        if os.path.isdir(os.path.join(args.base_dir, f))
    ]
    print(f"Base task families: {base_task_archive}")
    print()

    # Load generated tasks.
    generation_task_archive = [
        os.path.join(args.generation_dir, f)
        for f in os.listdir(args.generation_dir)
        if os.path.isdir(os.path.join(args.generation_dir, f))
    ]
    print(f"Generation task families: {generation_task_archive}")

    tasks = []
    for dir in base_task_archive:
        tasks.append(Task(dir, base_task=True))
    for dir in generation_task_archive:
        task = Task(dir, base_task=False)
        if task.embedding is not None:
            tasks.append(task)

    tasks = sorted(tasks, key=lambda x: x.idx)

    print("*" * 20 + "Surprising successes" + "*" * 20)
    for task in tasks:
        if task.label == TaskLabel.SURPRISING_SUCCESS:
            print(f"Index: {task.idx}")
            print(f"Label: {task.label.name}")
            print()
            print("-" * 20 + "Instructions" + "-" * 20)
            print(task.instructions[0])
            print("-" * 20 + "Sample response" + "-" * 20)
            print(task.eval_answers[0][0])
            print()

    print("*" * 20 + "Surprising failures" + "*" * 20)
    for task in tasks:
        if task.label == TaskLabel.SURPRISING_FAILURE:
            print(f"Index: {task.idx}")
            print(f"Label: {task.label.name}")
            print()
            print("-" * 20 + "Instructions" + "-" * 20)
            print(task.instructions[0])
            print("-" * 20 + "Sample response" + "-" * 20)
            print(task.eval_answers[0][0])
            print()

    # Prepare data for t-SNE
    embeddings = np.array([task.embedding for task in tasks])
    hover_text = []
    for task in tasks:
        if task.label != TaskLabel.BASE:
            # Collect all valid instruction-response pairs
            eval_scores = task.eval_scores
            eval_answers = task.eval_answers
            instructions = task.instructions

            valid_pairs = []

            # Loop over all instructions
            for inst_idx, (
                inst,
                scores_per_instruction,
                answers_per_instruction,
            ) in enumerate(zip(instructions, eval_scores, eval_answers)):
                if not scores_per_instruction or not answers_per_instruction:
                    continue

                if task.label in [TaskLabel.SUCCESS, TaskLabel.SURPRISING_SUCCESS]:
                    # Find all responses with score == 1
                    for i, score in enumerate(scores_per_instruction):
                        if score == 1:
                            response = answers_per_instruction[i]
                            valid_pairs.append((inst, response))
                elif task.label in [TaskLabel.FAILURE, TaskLabel.SURPRISING_FAILURE]:
                    # Find all responses with score == 0
                    for i, score in enumerate(scores_per_instruction):
                        if score == 0:
                            response = answers_per_instruction[i]
                            valid_pairs.append((inst, response))

            if valid_pairs:
                instruction, response = random.choice(valid_pairs)
            else:
                print(f"No matching response found for task {task.idx}")
                instruction = instructions[0] if instructions else ""
                response = ""
            hover_str = f"Instructions: {instruction}. <br><br> Response: {response}"
        else:
            instruction = task.instructions[0] if task.instructions else ""
            hover_str = f"Instructions: {instruction}"

        # Split the hover text into multiple lines for better readability.
        spacing = 120
        hover_str_array = []
        spacing_indices = [i for i in range(0, len(hover_str), spacing)]
        # Adjust spacing indices to nearest space
        for i in range(1, len(spacing_indices)):
            idx = spacing_indices[i]
            while (
                idx < len(hover_str)
                and hover_str[idx] != " "
                and idx > spacing_indices[i - 1]
            ):
                idx -= 1
            if idx == spacing_indices[i - 1]:  # No space found, use original index
                idx = spacing_indices[i]
            spacing_indices[i] = idx
        for i in range(1, len(spacing_indices)):
            hover_str_array.append(
                hover_str[spacing_indices[i - 1] : spacing_indices[i]]
            )
        hover_str_array.append(hover_str[spacing_indices[-1] :])
        hover_str = "<br>".join(h for h in hover_str_array)

        hover_text.append(hover_str)

    labels = [task.label.name for task in tasks]
    print(f"Number of interestingly new tasks: {len(embeddings)}")

    # Reduce dimensionality to 2D using t-SNE
    tsne = TSNE(n_components=2, random_state=42)
    embeddings_2d = tsne.fit_transform(embeddings)

    # Create DataFrame for Plotly Express
    # Create a new dictionary with your data
    data = {
        "embeddings_x": embeddings_2d[:, 0],
        "embeddings_y": embeddings_2d[:, 1],
        "labels": labels,
        "hover_text": hover_text,
    }

    # Create a new DataFrame from the dictionary
    df = pd.DataFrame(data)

    # Custom color palette for task types
    color_discrete_map = {
        "BASE": "#008000",
        "SUCCESS": "#0000FF",
        "FAILURE": "#FF0000",
        "SURPRISING_SUCCESS": "#800080",
        "SURPRISING_FAILURE": "#FFA500",
    }

    # Create t-SNE plot with Plotly Express
    fig = px.scatter(
        df,
        x="embeddings_x",
        y="embeddings_y",
        color="labels",
        hover_name="hover_text",
        title="t-SNE Visualization of Task Space",
        color_discrete_map=color_discrete_map,  # Apply custom colors
    )

    # Customize the plot appearance (optional)
    fig.update_traces(marker=dict(size=6))  # Increase marker size

    fig.write_html("t-SNE_visualization.html")

    fig.show()


if __name__ == "__main__":
    main()
