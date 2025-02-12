class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem_description": "Write a Python function that takes a list of integers and returns a new list with only the prime numbers."},
            "2": {"buggy_code": "def find_max(numbers):\n    max_num = numbers[0]\n    for num in numbers:\n        if num > max_num:\n            max_num = num\n    return min_num", "expected_behavior": "The function should return the maximum number in the list."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'problem_description' in t:
            return f"""Your task is to generate a Python function to solve the following problem:

{t['problem_description']}

Ensure your code is correct, efficient, and follows Python conventions. Provide the complete function definition in plain text format without additional explanations."""
        else:
            return f"""Your task is to debug the following Python function:

{t['buggy_code']}

The function is supposed to perform the following behavior:
{t['expected_behavior']}

Identify and correct the errors in the code to ensure it behaves as expected. Provide the corrected code in plain text format without additional explanations."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'problem_description' in t:
            criteria = ["The code should be correct and functional.", "The code should follow Python conventions.", "The code should be efficient."]
        else:
            criteria = ["The corrected code should fix the errors.", "The corrected code should perform as expected.", "The corrected code should follow Python conventions."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
