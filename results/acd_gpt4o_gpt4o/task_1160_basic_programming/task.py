class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"requirements": "Write a Python function that takes a list of numbers and returns the sum of its elements. Ensure that your function handles empty lists by returning 0."},
            "2": {"code": "def find_maximum(nums):\n    max_num = nums[0]\n    for num in nums:\n        if num > max_num:\n            max_num = num\n    return max_num\n", "error": "There is a mistake in the code. Debug it to find the correct maximum number in the list."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "requirements" in t:
            instructions = f"""Your task is to write a Python function based on the following requirements:

{t['requirements']}

Provide your solution in plain text format."""
        else:
            instructions = f"""Your task is to debug the following Python code. The current code has an error and does not return the correct maximum number from the list. Identify and fix the error.

Code:
{t['code']}

{t['error']}

Provide your corrected code in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "requirements" in t:
            criteria = ["The function should be syntactically correct.", "The function should correctly return the sum of the list elements.", "The function should handle empty lists by returning 0."]
        else:
            criteria = ["The corrected code should be syntactically correct.", "The corrected code should return the correct maximum number from the list."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
