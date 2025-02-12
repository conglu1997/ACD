import json
import os
from collections import defaultdict
from enum import Enum

import backoff
import numpy as np
import openai
from hdbscan import HDBSCAN
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


@backoff.on_exception(backoff.expo, openai.RateLimitError)
def get_n_responses_from_gpt(
    client,
    msg,
    model,
    system_message,
):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": msg},
        ],
        temperature=0.7,
        max_tokens=1000,
        response_format={"type": "json_object"},
    )
    content = response.choices[0].message.content
    json_dict = json.loads(content, strict=False)

    return json_dict


def infer_cluster_labels(task_folder, output_path, scientist_model):
    system_msg = """You are a helpful assistant.
You are given a set of tasks within a cluster.

Reply concisely and exactly in JSON format with only the following keys:
- "thought": First, reason about the essence of the given tasks in the cluster.
- "label": Your summary label for the cluster of tasks.
- "capability_being_measured": The overall capability being measured by the tasks in this cluster.

This will be automatically parsed so ensure that the string response is precisely in the correct format."""

    # Initialize OpenAI client
    client = openai.OpenAI()

    # Load generated tasks.
    generation_task_archive = [
        os.path.join(task_folder, f)
        for f in os.listdir(task_folder)
        if os.path.isdir(os.path.join(task_folder, f))
    ]
    print(f"Generated task families: {generation_task_archive}")

    tasks = []
    for dir in generation_task_archive:
        task = Task(dir, base_task=False)
        if task.embedding is not None:
            tasks.append(task)

    tasks = sorted(tasks, key=lambda x: x.idx)
    embeddings = np.array([task.embedding for task in tasks])
    # Reduce dimensionality to 2D using t-SNE
    tsne = TSNE(n_components=2, random_state=42)
    embeddings_2d = tsne.fit_transform(embeddings)

    hdbscan = HDBSCAN(
        min_cluster_size=16,  # Increased significantly
        min_samples=4,        # Increased significantly
        cluster_selection_epsilon=2,  # Increased to be more inclusive
        cluster_selection_method="eom",
        metric="euclidean",   # Explicitly set the distance metric
    )
    cluster_labels = hdbscan.fit_predict(embeddings_2d)

    # Create a list to store the clustering results
    clustering_results = []

    # Iterate through tasks and cluster labels
    for task, cluster_label in zip(tasks, cluster_labels):
        result = {
            "dir": task.dir,
            "task_json": task.task_json,
            "cluster": int(
                cluster_label
            ),  # Convert numpy.int64 to int for JSON serialization
        }
        clustering_results.append(result)

    # Group tasks by cluster
    clusters = defaultdict(list)
    for task in clustering_results:
        cluster = task["cluster"]
        task_info = task["task_json"]
        clusters[cluster].append(task_info)

    # Dictionary to store cluster labels and capabilities
    cluster_info = {}

    # Process each cluster
    for cluster, tasks in clusters.items():
        prompt = f"[DATA]\nCluster {cluster} tasks:\n\n"
        for task in tasks:
            prompt += f"Name: {task['name_of_task']}\n"
            prompt += f"Description: {task['description_of_task']}\n"
            prompt += f"Capability: {task['capability_being_measured']}\n\n"

        prompt += (
            '\n\n\n[INSTRUCTION]\nConsider the above tasks in this cluster. Please provide a concise label (a natural language phrase within 10 words) for the cluster. Ensure that the label is very specific to the tasks; avoid being general. Avoid including general terms such as "problem-solving". Include more specific keywords from the tasks, such as "poem", "logic puzzles", etc. \n\nAlso, provide the overall capability being measured by the tasks in this cluster.'
        )

        json_dict = get_n_responses_from_gpt(
            client, prompt, scientist_model, system_msg
        )

        # Store the cluster information
        cluster_info[cluster] = {
            "label": json_dict["label"],
            "capability": json_dict["capability_being_measured"],
        }

        print(f"Cluster {cluster}:")
        print(f"Label: {json_dict['label']}")
        print(f"Capability: {json_dict['capability_being_measured']}")
        print("---")

    # Add labels and capabilities to clustering results
    for task in clustering_results:
        cluster = task["cluster"]
        if cluster in cluster_info:
            task["cluster_label"] = cluster_info[cluster]["label"]
            task["cluster_capability"] = cluster_info[cluster]["capability"]

    # Save updated clustering results
    with open(output_path, "w") as f:
        json.dump(clustering_results, f, indent=2)

    print(f"Cluster labels and capabilities have been saved to {output_path}")
