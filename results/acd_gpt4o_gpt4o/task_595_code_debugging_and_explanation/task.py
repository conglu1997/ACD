class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "code": "def factorial(n):\n    if n == 0:\n        return 1\n    else:\n        return n * factorial(n - 1)\n\nprint(factorial(5))"
            },
            "2": {
                "code": "def find_max(arr):\n    if len(arr) == 0:\n        return None\n    max_val = arr[0]\n    for i in arr[1:]:\n        if i > max_val:\n            max_val = i\n    return max_val\n\nprint(find_max([1, 2, 3, 4, 5]))"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to identify and correct any errors in the given code snippet. After making the corrections, provide a detailed explanation of the changes you made and why they were necessary.

Code Snippet:\n{t['code']}\n
Your response should include:\n1. The corrected code snippet.\n2. A detailed explanation of the corrections made, including why the original code was incorrect.

Provide your response in plain text format, ensuring it is well-structured and demonstrates a deep understanding of the code."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include the corrected code snippet.",
            "The explanation should cover all corrections made and why they were necessary.",
            "The response should be well-structured and logically sound."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
