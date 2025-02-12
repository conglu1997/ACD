import argparse
import json
import os
import textwrap
from math import pi

import matplotlib.pyplot as plt
import numpy as np


def plot_cluster_radar_mpl(acd_name, model_cluster_stats, models):
    """
    Creates a radar chart comparing success rates for the given models
    across all discovered clusters, using Matplotlib.
    - Uses a half-angle shift so that top/bottom are between labels.
    - Employs quadrant-based label rotation so text faces outward.
    - Nudges whichever labels are *closest* to top (pi/2) and bottom (3*pi/2).
    - Restores the savefig command.
    """

    # Collect all unique clusters across models
    all_clusters = set()
    for stats in model_cluster_stats.values():
        all_clusters.update(stats.keys())
    all_clusters = sorted(list(all_clusters))
    n_clusters = len(all_clusters)

    if n_clusters == 0:
        print("No clusters found; cannot plot radar.")
        return

    # Wrap each cluster label to reduce overlap
    def wrap_label(label, width=25):
        return "\n".join(textwrap.wrap(label, width))

    wrapped_clusters = [wrap_label(c, width=25) for c in all_clusters]

    # -- Angles with a half-step shift so top/bottom is a gap --
    angles = np.linspace(0, 2 * np.pi, n_clusters, endpoint=False)
    half_step = (2 * np.pi / n_clusters) / 2
    angles += half_step
    angles = np.concatenate((angles, [angles[0]]))  # close loop

    fig, ax = plt.subplots(subplot_kw={"polar": True}, figsize=(10, 10))

    # Plot each model's data
    for model in models:
        model_stats = model_cluster_stats.get(model, {})
        rates = []
        for cluster in all_clusters:
            cluster_data = model_stats.get(cluster, {"success": 0, "total": 0})
            rate = (
                cluster_data["success"] / cluster_data["total"]
                if cluster_data["total"]
                else 0
            )
            rates.append(rate)
        rates.append(rates[0])  # close loop

        legend_label = subject
        ax.plot(angles, rates, label=legend_label, linewidth=2)
        ax.fill(angles, rates, alpha=0.15)

    # Offset so the "gap" is at 12 o'clock
    ax.set_theta_offset(pi / 2)
    # Reverse direction to go clockwise
    ax.set_theta_direction(-1)

    # Radial grid lines
    grid_values = [0.2, 0.4, 0.6, 0.8, 1.0]
    ax.set_rgrids(grid_values, labels=[str(g) for g in grid_values])
    ax.set_ylim(0, 1)

    # Angles for the labels (excluding the appended angle)
    label_angles = angles[:-1]
    ax.set_thetagrids(np.degrees(label_angles), labels=wrapped_clusters, fontsize=6)
    # --- Only change: increase pad to move the labels outward ---
    ax.tick_params(axis="x", pad=10)

    # Quadrant-based rotation for outward facing text
    for label, angle_rad in zip(ax.get_xticklabels(), label_angles):
        if angle_rad <= pi / 2:
            # Quadrant I
            ha, va = "center", "bottom"
            angle_text = angle_rad * (-180 / pi) + 90
        elif pi / 2 < angle_rad <= pi:
            # Quadrant II
            ha, va = "center", "top"
            angle_text = angle_rad * (-180 / pi) + 90
        elif pi < angle_rad <= 3 * pi / 2:
            # Quadrant III
            ha, va = "center", "top"
            angle_text = angle_rad * (-180 / pi) - 90
        else:
            # Quadrant IV
            ha, va = "center", "bottom"
            angle_text = angle_rad * (-180 / pi) - 90

        label.set_rotation(angle_text)
        label.set_horizontalalignment(ha)  # Always center horizontally
        label.set_verticalalignment(va)  # Keeps top/bottom alignment as before

    # Title & legend
    ax.set_title("Success Rate Comparison by Task Cluster", y=1.12, fontsize=20)
    ax.legend(
        loc="upper right",
        bbox_to_anchor=(1.2, 1.15),
        fontsize=14,
        title_fontsize=16,
        frameon=True,
        title="Eval Model",
    )

    plt.tight_layout()
    plt.savefig(f"reports/cluster_radar_{acd_name}.pdf", dpi=300, bbox_inches="tight")


parser = argparse.ArgumentParser(description="Visualize cluster success rates")
parser.add_argument(
    "--acd_name",
    type=str,
    default="gpt4_gpt4",
    help="ACD experiment name (e.g. gpt4_gpt4)",
)
parser.add_argument(
    "--clustering_labels_path", type=str, help="Path to clustering labels JSON file"
)
args = parser.parse_args()

MODEL_NAME = {"gpt4": "GPT-4o", "llama": "Llama-8B", "sonnet": "Claude 3.5 Sonnet"}
scientist, subject = args.acd_name.split("_")
try:
    scientist, subject = MODEL_NAME[scientist], MODEL_NAME[subject]
except:
    pass
eval_threshold = 0.6

clustering_labels_path = args.clustering_labels_path
if not os.path.exists(clustering_labels_path):
    raise FileNotFoundError(f"Clustering results not found at {clustering_labels_path}")
else:
    print(f"Found clustering results at {clustering_labels_path}")

# Load clustering results
with open(clustering_labels_path, "r") as f:
    clustering_data = json.load(f)

# Create a mapping of task names to cluster info
task_to_cluster = {}
for item in clustering_data:
    task_to_cluster[item["dir"]] = {
        "cluster": item["cluster"],
        "label": item["cluster_label"],
        "capability": item["cluster_capability"],
    }

# Dictionary to store cluster-level stats
cluster_stats = {}
total_tasks = 0
successful_tasks = 0

for task_dir, cluster_info in task_to_cluster.items():
    # Get success rate from metadata
    metadata_file = os.path.join(task_dir, "metadata.json")
    if not os.path.exists(metadata_file):
        continue

    with open(metadata_file, "r") as f:
        metadata = json.load(f)
    success_rate = metadata.get("success_rate", 0)

    total_tasks += 1
    if success_rate >= eval_threshold:
        successful_tasks += 1

    # Track cluster success
    cluster_label = cluster_info["label"]
    if cluster_label not in cluster_stats:
        cluster_stats[cluster_label] = {"total": 0, "success": 0}
    cluster_stats[cluster_label]["total"] += 1
    if success_rate >= eval_threshold:
        cluster_stats[cluster_label]["success"] += 1

model_cluster_stats = {subject: cluster_stats}
overall_success_rate = successful_tasks / total_tasks if total_tasks > 0 else 0
print(
    f"Overall success rate: {overall_success_rate:.2%} ({successful_tasks}/{total_tasks})"
)
# Call the Matplotlib radar function
plot_cluster_radar_mpl(args.acd_name, model_cluster_stats, [subject])
