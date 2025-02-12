import argparse
import json
import os
import re

# Add parent directory to Python path
import sys
import textwrap
from enum import Enum

import matplotlib.colors as mcolors
import numpy as np
import pandas as pd
import plotly.express as px
from sklearn.manifold import TSNE

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

from generate_acd_tasks import get_task_summary, load_task_family


def rgb_to_rgba(color, alpha=0.3):
    if color.startswith("#"):
        # Hex color code (e.g., #rrggbb)
        rgb = tuple(int(color.lstrip("#")[i : i + 2], 16) for i in (0, 2, 4))
    elif color.startswith("rgb"):
        # RGB color code (e.g., rgb(r, g, b))
        rgb = tuple(map(int, re.findall(r"\d+", color)))
    else:
        # Named color (e.g., "red", "blue")
        rgb = tuple(int(x * 255) for x in mcolors.to_rgb(color))

    # Return the RGBA string with the specified alpha value
    return f"rgba({rgb[0]}, {rgb[1]}, {rgb[2]}, {alpha})"


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
    parser.add_argument(
        "--acd_name",
        type=str,
        default="gpt4_gpt4",
        help="ACD experiment name (e.g. gpt4_gpt4)",
    )
    parser.add_argument("--task_folder", type=str, help="Path to task folder")
    parser.add_argument(
        "--clustering_labels_path", type=str, help="Path to clustering labels JSON file"
    )
    args = parser.parse_args()

    if not os.path.exists(args.clustering_labels_path):
        raise FileNotFoundError(
            f"Clustering results not found at {args.clustering_labels_path}"
        )
    else:
        print(f"Found clustering results at {args.clustering_labels_path}")

    # Read clustering results from JSON file
    with open(args.clustering_labels_path, "r") as f:
        clustering_results = json.load(f)

    # Load generated tasks.
    generation_task_archive = [
        os.path.join(args.task_folder, f)
        for f in os.listdir(args.task_folder)
        if os.path.isdir(os.path.join(args.task_folder, f))
    ]

    tasks = []
    for dir in generation_task_archive:
        task = Task(dir, base_task=False)
        if task.embedding is not None:
            tasks.append(task)

    tasks = sorted(tasks, key=lambda x: x.idx)

    # Prepare data for t-SNE
    embeddings = np.array([task.embedding for task in tasks])
    print(f"Number of interestingly new tasks: {len(embeddings)}")

    # Reduce dimensionality to 2D using t-SNE
    tsne = TSNE(n_components=2, random_state=42)
    embeddings_2d = tsne.fit_transform(embeddings)

    # Extract cluster labels and capabilities from clustering results
    cluster_int = []
    cluster_names = []
    cluster_capabilities = []
    hover_text = []
    for task in tasks:
        matching_result = next(
            (r for r in clustering_results if r["dir"] == task.dir), None
        )
        if matching_result:
            cluster_int.append(matching_result["cluster"])
            cluster_names.append(matching_result["cluster_label"])
            cluster_capabilities.append(matching_result["cluster_capability"])
        else:
            cluster_int.append(-1)
            cluster_names.append("")
            cluster_capabilities.append("")

        if not task.eval_answers:
            hover_str = f"Instructions: {task.instructions[0]}"
        elif task.eval_answers[0]:
            hover_str = f'Instructions: {task.instructions[0]}. <br><br> Response: {task.eval_answers[0][0]} <br><br> LLM judge: {"succeed" if task.metadata["accepted"] == "yes" else "fail"}'
        elif task.eval_answers[1]:
            hover_str = f'Instructions: {task.instructions[1]}. <br><br> Response: {task.eval_answers[1][0]} <br><br> LLM judge: {"succeed" if task.metadata["accepted"] == "yes" else "fail"}'
        else:
            hover_str = f"Instructions: {task.instructions[0]}"

        hover_str += (
            f"<br><br> Measured Capability: {matching_result['cluster_capability']}"
        )

        # Split the hover text into multiple lines for better readability.
        spacing = 120
        hover_str_array = []
        spacing_indices = [i for i in range(0, len(hover_str), spacing)]
        # adjust spacing indices to nearest space
        for i in range(1, len(spacing_indices)):
            idx = spacing_indices[i]
            while hover_str[idx] != " ":
                idx -= 1
            spacing_indices[i] = idx
        for i in range(1, len(spacing_indices)):
            hover_str_array.append(
                hover_str[spacing_indices[i - 1] : spacing_indices[i]]
            )
        hover_str_array.append(hover_str[spacing_indices[-1] :])
        hover_str = "<br>".join(h for h in hover_str_array)

        hover_text.append(hover_str)

    cluster_int = np.array(cluster_int)
    # Create DataFrame for Plotly Express
    data = {
        "embeddings_x": embeddings_2d[:, 0],
        "embeddings_y": embeddings_2d[:, 1],
        "hover_text": hover_text,
        "cluster": cluster_int,
        "cluster_label": cluster_names,
        "cluster_capability": cluster_capabilities,
    }

    # Create a new DataFrame from the dictionary
    df = pd.DataFrame(data)

    # Filter out the -1 cluster and convert 'cluster' to int
    df = df[df["cluster"] != -1]
    df["cluster"] = df["cluster"].astype(str)

    # Define a custom color scheme
    color_scheme = (
        px.colors.qualitative.Bold
        + px.colors.qualitative.D3
        + px.colors.qualitative.Set3
        + px.colors.qualitative.Alphabet
    )

    unique_clusters = df["cluster"].unique()

    cluster_colors = {
        cluster: color_scheme[i % len(color_scheme)]
        for i, cluster in enumerate(unique_clusters)
    }

    # Create t-SNE plot with Plotly Express, now including cluster information
    fig = px.scatter(
        df,
        x="embeddings_x",
        y="embeddings_y",
        color="cluster",
        color_discrete_map=cluster_colors,  # Use the cluster_colors mapping here
        hover_name="hover_text",
    )

    # Customize the plot appearance
    fig.update_traces(
        marker=dict(size=12, opacity=0.7)
    )  # Increase marker size and add some transparency
    # Add cluster labels with matching colors

    for cluster in unique_clusters:
        cluster_data = df[df["cluster"] == cluster]
        x_center = cluster_data["embeddings_x"].mean()
        y_center = cluster_data["embeddings_y"].mean()

        cluster_label = cluster_data["cluster_label"].iloc[0]
        cluster_color = cluster_colors[cluster]  # Use the same color mapping as before
        wrapped_text = "<br>".join(textwrap.wrap(f"{cluster_label}", width=20))

        fig.add_annotation(
            x=x_center,
            y=y_center,
            text=wrapped_text,
            showarrow=False,
            font=dict(size=12, color="black", family="Arial Black", weight="bold"),
            bgcolor=rgb_to_rgba("white", alpha=0.7),
            bordercolor=cluster_color,
            borderwidth=4,
            borderpad=4,
            width=150,  # Set a fixed width for the annotation box
            align="center",
        )

    # Update layout for a cleaner, more beautiful look
    fig.update_layout(
        showlegend=False,
        title=None,
        xaxis_title="",
        yaxis_title="",
        xaxis_showticklabels=False,
        yaxis_showticklabels=False,
        xaxis_showgrid=False,
        yaxis_showgrid=False,
        plot_bgcolor="white",
        margin=dict(l=0, r=0, t=0, b=0),
        width=1920,
        height=1080,
    )

    # Remove color axis (heatbar legend)
    fig.update_coloraxes(showscale=False)

    # Save as PDF
    pdf_path = f"reports/cluster_vis_{args.acd_name}.pdf"
    fig.write_image(pdf_path)


if __name__ == "__main__":
    main()
