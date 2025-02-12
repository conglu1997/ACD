class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "code_snippet": "def find_max(numbers):\n    max_num = None\n    for n in numbers:\n        if max_num is None or n > max_num:\n            max_num = n\n    return max_num\n\n# Example usage\nprint(find_max([3, 5, 7, 2, 8]))  # Expected output: 8\n# Note: Check the logic for finding the maximum number."
            },
            "2": {
                "code_snippet": "def factorial(n):\n    if n == 0:\n        return 1\n    else:\n        return n * factorial(n - 1)\n\n# Example usage\nprint(factorial(5))  # Expected output: 120\n# Note: Ensure the factorial calculation is correct for positive integers."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Identify and fix any bugs in the following code snippet. Then, explain the functionality of the corrected code.

Code Snippet:
{t['code_snippet']}

Submit your corrected code and explanation as a plain text string in the following format:

Corrected Code:
[Your corrected code here]

Explanation:
[Your explanation here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = ["The corrected code should be syntactically correct and run without errors.", "The explanation should accurately describe the functionality of the corrected code."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
