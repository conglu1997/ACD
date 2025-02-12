import re
from typing import List, Tuple

import openai

from src.acd_prompts import (
    interestingly_new_prompt,
    interestingly_new_system_msg,
    surprising_prompt,
    surprising_system_msg,
)
from src.llm_utils import get_response_from_llm

# By default, all LLM-judgment is done with GPT-4.
client = openai.OpenAI()


def eval_task_interestingness(
    new_task_summary: str,
    closest_task_summaries: List[str],
    model: str = "gpt-4o-2024-05-13",
    print_debug: bool = False,
) -> bool:
    prompt = interestingly_new_prompt.format(
        new_task=new_task_summary,
        closest_tasks="\n\n".join(closest_task_summaries),
    )

    response_text, _ = get_response_from_llm(
        msg=prompt,
        client=client,
        model=model,
        system_message=interestingly_new_system_msg,
        print_debug=print_debug,
    )

    match = re.search(r"Decision:\s*(Yes|No)", response_text, re.IGNORECASE)
    if match:
        decision = match.group(1).strip().lower() == "yes"
    else:
        decision = False

    return decision


def eval_task_surprisingness(
    new_task_summary: str,
    new_task_code: str,
    model: str = "gpt-4o-2024-05-13",
    print_debug: bool = False,
) -> Tuple[bool, List[str]]:
    prompt = surprising_prompt.format(
        new_task=new_task_summary,
        new_task_code=new_task_code,
    )

    response_text, msg_history = get_response_from_llm(
        msg=prompt,
        client=client,
        model=model,
        system_message=surprising_system_msg,
        print_debug=print_debug,
    )

    match = re.search(r"Decision:\s*(Yes|No)", response_text, re.IGNORECASE)
    if match:
        decision = match.group(1).strip().lower() == "yes"
    else:
        decision = False

    return decision, msg_history
