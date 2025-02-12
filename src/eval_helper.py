import re
from typing import List, Optional

import openai

from src.llm_utils import get_response_from_llm

# By default, all LLM-judgment is done with GPT-4.
client = openai.OpenAI()

judge_system_msg = """You are an impartial judge evaluating the quality of responses provided by an AI assistant.
You will be provided the instructions for the task and the assistant's submission in response.
You will decide whether or not the agent succeeded at the task.
Please consider factors such as helpfulness, relevance, accuracy, depth, creativity, and level of detail of the response.
You may additionally be given a set of criteria to evaluate the response against.
Do not allow the length of the response to influence your decision.

Respond precisely in the following format:

THOUGHT:
<THOUGHT>

DECISION:
<DECISION>

In <THOUGHT>, briefly reason about the agent's response and whether it meets the additional criteria.

In <DECISION>, provide your answer as either "Yes" or "No"."""

judge_prompt = '''Instruction: {instructions}
Submission: {submission}

Additional Evaluation Criteria:
"""
{criteria}
"""
'''


# Function to extract the decision from the response using regular expressions
def extract_decision(response: str) -> Optional[str]:
    decision_pattern = r"DECISION:\s*(Yes|No)\s*$"
    match = re.search(decision_pattern, response, re.IGNORECASE | re.MULTILINE)
    if match:
        return match.group(1).strip().capitalize()
    return None


# Automated LLM judge helper function
# Returns a boolean indicating whether the submission succeeded at the task, and meets any additional criteria
def eval_with_llm_judge(
    instructions: str,  # The instructions for the task
    submission: str,  # The submission to evaluate
    criteria: Optional[
        List[str]
    ] = None,  # Additional criteria to evaluate the submission against
    model: str = "gpt-4o-2024-05-13",
    print_debug: bool = False,
) -> bool:
    criteria_str = "\n".join([f"* {c}" for c in criteria]) if criteria else ""

    prompt = judge_prompt.format(
        instructions=instructions,
        submission=submission,
        criteria=criteria_str,
    )

    if print_debug:
        print("Judge Prompt:\n", prompt)

    response, *_ = get_response_from_llm(
        msg=prompt,
        client=client,
        model=model,
        system_message=judge_system_msg,
        print_debug=print_debug,
    )

    if print_debug:
        print("LLM Response:\n", response)

    decision = extract_decision(response)

    if decision is None:
        if print_debug:
            print("Failed to extract decision. Defaulting to 'No'.")
        return False  # Default to False if decision cannot be determined

    return decision == "Yes"
