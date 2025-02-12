class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "code_snippet": "def factorial(n):\n    if n == 0:\n        return 1\n    else:\n        return n * factorial(n - 1)"
            },
            "2": {
                "code_snippet": "def is_prime(num):\n    if num <= 1:\n        return False\n    for i in range(2, int(num ** 0.5) + 1):\n        if num % i == 0:\n            return False\n    return True"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the following code snippet and write a new code snippet that achieves the same functionality without directly copying the original code.

Code Snippet:
{t['code_snippet']}

Submit your new code snippet as a plain text string in the following format:

New Code Snippet:
[your code here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The new code snippet should achieve the same functionality as the original code snippet.",
            "The new code snippet should not directly copy the original code snippet.",
            "The new code snippet should be syntactically correct and executable.",
            "The new code snippet should be written in a different style or use different constructs compared to the original."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
