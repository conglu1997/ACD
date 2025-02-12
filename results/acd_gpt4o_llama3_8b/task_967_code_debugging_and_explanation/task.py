class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "code": "def calculate_factorial(n):\n    if n == 0:\n        return 1\n    elif n > 0:\n        return n * calculate_factorial(n - 1)\n    else:\n        return 'Invalid input'\n\nprint(calculate_factorial(5))\nprint(calculate_factorial(-3))",
                "bug_description": "The function is supposed to calculate the factorial of a number, but it's not handling negative inputs correctly."
            },
            "2": {
                "code": "def find_max(lst):\n    if not lst:\n        return None\n    max_val = lst[0]\n    for val in lst[1:]:\n        if val > max_val:\n            max_val = val\n    return max_val\n\nprint(find_max([3, 5, 2, 4, 1]))\nprint(find_max([]))",
                "bug_description": "The function is supposed to find the maximum value in a list, but it's not handling empty lists correctly."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Identify and fix the bug in the following code snippet. Provide a detailed explanation of the bug and how you fixed it. Ensure your explanation is clear and demonstrates a deep understanding of the code and the bug.

Code: {t['code']}

Bug Description: {t['bug_description']}

Submit your response as a plain text string in the following format:
Fixed Code: [Your fixed code]
Explanation: [Your detailed explanation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = ["The code should be correctly fixed.", "The explanation should be clear and demonstrate understanding of the bug and the fix."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
