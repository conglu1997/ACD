base_system_msg = """You are an expert in designing task families to assess the capabilities of large language models (LLMs). 
You will write an analytical section for a report examining the capabilities and limitations of large language models.
Your goal is to analyze and synthesize insights about LLM capabilities by examining:
1) The LLM's performance and solutions on tasks designed to test specific capabilities.
2) Any patterns, strengths, or limitations revealed through this analysis.
Focus on identifying surprising successes and failures from the point of view of an expert human evaluator.
"""

cluster_analysis_system_msg = (
    base_system_msg
    + """You will be given a cluster of related task families that evaluate specific LLM capabilities, along with the LLM's responses and performance on these tasks.

Your goal is to:
1) Carefully examine the example tasks and the LLM's responses
2) Analyze the LLM's proficiency level on the evaluated capabilities
3) How these examples provide meaningful insights about the model's capabilities or limitations
4) Draw meaningful conclusions about the LLM's strengths and limitations in this capability area

Respond precisely in the following format including the JSON start and end markers:

THOUGHT:
<THOUGHT>

RESPONSE JSON:
```json
<JSON>
```

In <THOUGHT>, first deeply think and reason about the patterns and insights revealed by examining this cluster of related tasks.

In <JSON>, provide a JSON response with the following fields:
- "overall_analysis": A brief conclusion based on examining the example tasks and the LLM's responses, including key capabilities demonstrated and limitations revealed
- "surprising_example_analysis_X": Analysis of why this success or failure was surprising and what it reveals about the LLM's capabilities or limitations
- "insights": Key insights and takeaways about the LLM's capabilities based on analyzing this cluster of related tasks

For EACH provided example, include a "surprising_example_analysis_X" field in the JSON response, where X is replaced with the example's index number.
This will be automatically parsed so ensure that the string response is precisely in the correct format.
"""
)

cluster_analysis_prompt = """# Task Cluster Analysis
Cluster Name: {cluster_name}

# Capabilities Being Evaluated
{capabilities}
Note: Please examine the examples carefully to verify which capabilities are actually being tested.

# Tasks in Cluster
{task_names}

# Performance Statistics
Overall Success Rate: {overall_success_rate}
Success Rate by Task Difficulty:
{difficulty_breakdown}

# Surprising Example
Below are examples where the LLM succeeded or failed on tasks that reveal its capabilities or limitations.

{surprising_examples}

Please analyze:
1. What specific capabilities were demonstrated or lacking in the examples
2. Any patterns in the successes and failures
3. Notable or surprising results that reveal insights about the LLM's abilities
4. What this suggests about the LLM's understanding and limitations
5. How these insights connect to broader questions about LLM capabilities
"""


example_selection_system_msg = (
    base_system_msg
    + """You will be given a cluster of related task families that evaluate specific LLM capabilities, along with the LLM's responses and performance on these tasks.
Your goal is to identify surprising successes and failures that reveal meaningful insights about LLM capabilities.

Respond precisely in the following format including the JSON start and end markers:

THOUGHT:
<THOUGHT>

RESPONSE JSON:
```json
<JSON>
```

In <THOUGHT>, carefully analyze which examples demonstrate unexpected or notable behavior. Consider:
1) Surprising successes on challenging tasks that demonstrate unexpected capabilities
2) Unexpected failures on seemingly simple tasks that reveal limitations
3) Examples that challenge common assumptions about LLM capabilities

In <JSON>, provide a JSON response with the following fields:
- "surprising_success_example_idx": List of indices for the most surprising or noteworthy successful tasks (0-3 indices)
- "surprising_failure_example_idx": List of indices for the most surprising or noteworthy failed tasks (0-3 indices)

Format for index lists: Empty list [], single index [1], or multiple indices [0, 1, 3]

This will be automatically parsed so ensure that the string response is precisely in the correct format.
"""
)

example_selection_prompt = """# Task Cluster Analysis
Cluster Name: {cluster_name}

# Capabilities Being Evaluated
{capabilities}

# Tasks Overview
Total Tasks: {num_tasks}
Overall Success Rate: {overall_success_rate}

# Task Examples
{task_examples}

Please analyze these examples carefully to identify:
1) Which examples show surprising or unexpected successes, particularly:
   - Complex tasks handled with sophisticated reasoning
   - Challenging edge cases solved successfully
   - Tasks requiring capabilities not typically associated with LLMs

2) Which examples show surprising or unexpected failures, particularly:
   - Simple tasks that unexpectedly failed
   - Inconsistent performance on similar tasks
   - Failures that reveal interesting limitations

Focus on examples that would be genuinely surprising to an LLM expert researcher and provide meaningful insights about the model's capabilities or limitations.

In your response <THOUGHT>, briefly reason about EACH provided example and explain why it is (or isn't) surprising from the perspective of an LLM expert researcher.
Focus on examples that reveal genuinely unexpected capabilities or limitations.
"""

# overall_example_selection_system_msg = base_system_msg + """You will now select the most surprising examples from a collection of previously identified surprising successes and failures across various task clusters. Your goal is to identify the examples that provide the most significant insights into the LLM's capabilities and limitations.

# Respond precisely in the following format including the JSON start and end markers:

# THOUGHT:
# <THOUGHT>

# RESPONSE JSON:
# ```json
# <JSON>
# ```

# In <THOUGHT>, analyze each provided example and reason about why it is (or isn't) among the most surprising from the perspective of an LLM expert researcher. **Maintain a high bar for what counts as surprising—an example should challenge established understanding of LLM behavior.**

# In <JSON>, provide a JSON response with the following field:
# - "top_surprising_examples_idx": List of indices for the most surprising examples (3 indices).

# Format for index list: `[0, 2, 4]`.

# This will be automatically parsed so ensure that the string response is precisely in the correct format.
# """

overall_summary_system_msg = (
    base_system_msg
    + """You are an expert researcher and engineer in Language Models. You are writing a very professional technical report to inform readers of the summary of tested LLM's capabilities and limitations.
You will now provide an overall analysis and summary of the LLM's capabilities based on all the surprising tasks identified across various clusters. Your goal is to synthesize insights about the LLM's strengths and limitations, referencing specific results from the clusters using '#Cluster_i' to refer to examples.

Respond precisely in the following format including the JSON start and end markers:

THOUGHT:
<THOUGHT>

RESPONSE JSON:
```json
<JSON>
```

In <THOUGHT>, deeply analyze the patterns observed across all clusters, considering both the surprising successes and failures. Your analysis should be detailed and reference specific results, using '#Cluster_i' to refer to examples from clusters.

In <JSON>, provide a JSON response with the following fields:
- "abstract": An abstract to this report. The first sentence should introduce the use of the {scientist} model as a scientist to study the {subject} model's capabilities. Then summarize the main contents.
- "overall_summary": A comprehensive summary of the LLM's capabilities based on your analysis. Introduce the context for the reader, e.g. start with sentences like "In this report, we are going to examine this LLM's ... The LLM shows ..."
- "insight": A very detailed and long analysis to elaborate the above summary. Be very specific. Don't just list names of tasks, but dive into details to elaborate. Should be a list of str.
- "surprising_capabilities": Key surprising capabilities demonstrated by the LLM. Should be a list of str, and the analysis should be detailed and long.
- "surprising_failures": Notable limitations or failures revealed. Should be a list of str, and the analysis should be detailed and long.
- "data_insights": Analysis and interpretation of the numerical data provided (e.g., success rates, performance statistics). Should be a list of str, and the analysis should be detailed and long.

This will be automatically parsed so ensure that the string response is precisely in the correct format.
"""
)

# Define the overall summary prompt
overall_summary_prompt = """# Overall Summary

You have analyzed the LLM's performance across multiple task clusters and identified surprising successes and failures.

# Scientist and Subject
You are now using the {scientist} model as a scientist to study the {subject} model's capabilities.

# Cluster Summaries
{cluster_summaries}

# Overall Statistics
{overall_statistics}

Please synthesize a comprehensive analysis of the LLM's capabilities based on the information above. In your analysis:

1. Refer to specific results from clusters using '#Cluster_i' to refer to examples.
2. Provide detailed observations about patterns in the LLM's performance across different clusters.
3. Highlight surprising capabilities that challenge established understanding of LLM behavior.
4. Discuss surprising failures that reveal significant limitations.
5. Include analysis of numerical data, such as success rates and performance statistics.

In your response <THOUGHT>, provide a detailed reasoning process that leads to your conclusions.

After your analysis, provide the JSON response with the required fields.
"""

human_difficulty_to_str = {
    "1": "very easy",
    "2": "easy",
    "3": "moderate",
    "4": "hard",
    "5": "very hard",
}


def get_task_example_str(task):
    # Find first successful example if task was accepted, otherwise first failed example
    example_idx = 0
    if task.accepted:
        # Find first successful example
        for idx, score in enumerate(task.metadata["eval_scores"][0]):
            if score == 1:
                example_idx = idx
                break
    else:
        # Find first failed example
        for idx, score in enumerate(task.metadata["eval_scores"][0]):
            if score == 0:
                example_idx = idx
                break
    return f"""**Task**:
{task.name}
**Task Description**: 
{task.task_json['description_of_task']}
**Difficulty Level**: 
{task.difficulty} ({human_difficulty_to_str[str(task.difficulty)]})
**Instructions**:
{task.instructions[0]}
**Model Response Example**:
{task.eval_answers[0][example_idx]}
**Judge for Above Example**:
{"Successful" if task.metadata['eval_scores'][0][example_idx] == 1 else "Failed"}
**Overall Success Rate**:
{task.success_rate*100:.1f}%"""


def get_make_report_init_prompt(cluster_info):
    # Format the cluster analysis prompt with the provided info
    formatted_prompt = cluster_analysis_prompt.format(
        cluster_name=cluster_info["cluster_name"],
        capabilities=cluster_info["capabilities"],
        task_names="\n".join(cluster_info["task_names"]),
        overall_success_rate=f"{cluster_info['success_rate']:.1%}",
        difficulty_breakdown="\n".join(
            [
                f"Difficulty {diff} ({human_difficulty_to_str[str(diff)]}): {rate:.1%} ({cluster_info['difficulty_percentages'][diff]} of tasks)"
                for diff, rate in cluster_info["difficulty_success_rates"].items()
                if rate is not None
            ]
        ),
        surprising_examples=(
            "\n".join(
                [
                    f"## Example {idx+1}\n" f"{task.example_str}\n"
                    for idx, task in enumerate(cluster_info["surprising_tasks"])
                ]
            )
            if cluster_info["surprising_tasks"]
            else "No surprising tasks found."
        ),
    )
    return cluster_analysis_system_msg, formatted_prompt


def get_selected_surprising_examples(cluster_info):
    # Format the example_selection_prompt with the provided examples
    formatted_prompt = example_selection_prompt.format(
        cluster_name=cluster_info["cluster_name"],
        capabilities=cluster_info["capabilities"],
        num_tasks=cluster_info["num_tasks"],
        overall_success_rate=f"{cluster_info['success_rate']:.1%}",
        task_examples="\n\n".join(
            [
                f"## Example {idx+1}\n{task.example_str}"
                for idx, task in enumerate(cluster_info["all_examples"])
            ]
        ),
    )
    return example_selection_system_msg, formatted_prompt


def get_overall_summary_prompt(all_cluster_info, test_model):
    scientist, subject = test_model.split("_")
    # Prepare cluster summaries
    cluster_summaries = ""
    for cluster_id, cluster in all_cluster_info.items():
        cluster_name = cluster.get("cluster_name", "N/A")
        capabilities = cluster.get("capabilities", "N/A")
        success_rate = cluster.get("success_rate", 0)
        analysis = cluster.get("analysis", {})
        if not analysis:
            continue

        cluster_summary = f"""## Cluster_{cluster_id}
**Cluster Name**: {cluster_name}
**Capabilities**: {capabilities}
**Success Rate**: {success_rate:.2%}

**Overall Analysis**:
{analysis['overall_analysis']}

**Insights**:
{analysis['insights']}

"""
        cluster_summaries += cluster_summary

    # Prepare overall statistics
    # Collect cluster success rates
    cluster_success_rates = {}
    total_success_rate = 0
    cluster_count = 0

    for cluster_id, cluster in all_cluster_info.items():
        sr = cluster.get("success_rate")
        if sr is not None:
            cluster_success_rates[f"Cluster_{cluster_id}"] = sr
            total_success_rate += sr
            cluster_count += 1

    if cluster_count > 0:
        overall_success_rate = total_success_rate / cluster_count
    else:
        overall_success_rate = 0

    # Convert the overall statistics dict into text
    overall_statistics = f"**Overall Success Rate**: {overall_success_rate:.2%}\n\n**Cluster Success Rates:**\n"
    for cluster_id, sr in cluster_success_rates.items():
        overall_statistics += f"- Cluster_{cluster_id}: {sr:.2%}\n"

    # Return the system message and formatted prompt
    return overall_summary_system_msg.format(
        scientist=scientist, subject=subject
    ), overall_summary_prompt.format(
        cluster_summaries=cluster_summaries,
        overall_statistics=overall_statistics,
        scientist=scientist,
        subject=subject,
    )
