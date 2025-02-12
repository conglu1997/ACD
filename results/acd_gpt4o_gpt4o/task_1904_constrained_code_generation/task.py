class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "description": "Write a Python function that takes a list of numbers and returns a new list with only the even numbers. The function should be implemented in a single line using list comprehension.",
                "constraints": "The function must use list comprehension and be implemented in a single line."
            },
            "2": {
                "description": "Write a Python function that takes a string and returns the string with each word reversed. The function should not use any built-in Python string reversal methods.",
                "constraints": "The function must manually reverse each word and should not use any built-in methods like [::-1] or reversed()."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to write a Python function based on the following description and constraints:

Description: {t['description']}

Constraints: {t['constraints']}

Provide your function implementation as plain text code without additional commentary."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The function must meet the given description.",
            "The function must adhere to the specified constraints.",
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
