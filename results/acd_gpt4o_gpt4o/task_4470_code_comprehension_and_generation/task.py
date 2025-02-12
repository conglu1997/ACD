class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"code": "def process_data(data):\n    result = []\n    for item in data:\n        if item % 2 == 0:\n            result.append(item * 2)\n        else:\n            result.append(item + 1)\n    return result\n\ndata = [1, 2, 3, 4, 5]\nprint(process_data(data))", "bug_description": "The function is supposed to double even numbers and add 1 to odd numbers, but it does not produce the correct result for the list [1, 2, 3, 4, 5]."},
            "2": {"requirements": "Write a Python function that takes a list of integers and returns a new list with each integer squared. The function should be named 'square_list'."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "code" in t:
            return f"""Debug the following piece of code based on the provided bug description. Ensure that the corrected code performs the intended functionality.

Code: {t['code']}

Bug Description: {t['bug_description']}

Provide your corrected code in plain text format with proper indentation."""
        else:
            return f"""Write a piece of code based on the following requirements:

Requirements: {t['requirements']}

Ensure that your code is functional and meets the specified requirements. Provide your code in plain text format with proper indentation."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "code" in t:
            criteria = ["The corrected code should double even numbers and add 1 to odd numbers correctly for the list [1, 2, 3, 4, 5]."]
        else:
            criteria = ["The code should define a function named 'square_list' that takes a list of integers and returns a new list with each integer squared."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
