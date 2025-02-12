class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "Write a Python function that takes a list of integers and returns a list containing only the even numbers from the input list."},
            "2": {"code": "def mystery_function(s):\n    return ''.join([chr(ord(c) + 1) for c in s])"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'description' in t:
            return f"""{t['description']}\n\nYour task is to write a Python function that meets the above requirements. Ensure that your function is syntactically correct and works as expected. Provide your response in plain text format with the function definition."""
        else:
            return f"""The following Python function is provided:\n\n{t['code']}\n\nYour task is to explain what this function does. Ensure that your explanation is clear, accurate, and covers all aspects of the function's behavior. Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'description' in t:
            criteria = [
                "The function should correctly filter out even numbers from the input list.",
                "The function should be syntactically correct.",
                "The function should be written in Python.",
                "The function should handle edge cases correctly (e.g., empty list, list with no even numbers)."
            ]
        else:
            criteria = [
                "The explanation should accurately describe the function's behavior.",
                "The explanation should be clear and concise.",
                "The explanation should include details on how the function processes each character in the input string."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0