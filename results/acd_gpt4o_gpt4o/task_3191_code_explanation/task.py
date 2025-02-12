class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"code": "def factorial(n):\n    if n == 0 or n == 1:\n        return 1\n    else:\n        return n * factorial(n - 1)"},
            "2": {"code": "def quicksort(arr):\n    if len(arr) <= 1\n        return arr\n    pivot = arr[len(arr) // 2]\n    left = [x for x in arr if x < pivot]\n    middle = [x for x in arr if x == pivot]\n    right = [x for x in arr if x > pivot]\n    return quicksort(left) + middle + quicksort(right)"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to explain the following piece of code step-by-step in plain language. Make sure your explanation is clear, accurate, and easy to understand for someone without a strong programming background.

Code:
{t['code']}

Instructions:
1. Break down the code into smaller parts or steps.
2. Explain what each part or step does in simple terms.
3. Ensure your explanation is coherent and covers the entire code.

Provide your explanation in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The explanation should accurately describe what each part of the code does.",
            "The language used should be simple and easy to understand.",
            "The explanation should cover the entire code provided."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
