class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"code": "def factorial(n):\n    if n == 0:\n        return 1\n    else:\n        return n * factorial(n-1)", "modification": "Modify the code to use an iterative approach instead of recursion."},
            "2": {"code": "def find_max(arr):\n    max_val = arr[0]\n    for num in arr:\n        if num > max_val:\n            max_val = num\n    return max_val", "modification": "Modify the code to handle an empty array input by returning None."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Explain the given code snippet and then modify it based on the specified requirement.\n\nCode Snippet:\n{t['code']}\n\nModification Requirement:\n{t['modification']}\n\nSubmit your explanation and modified code as a plain text string in the following format:\n\nExplanation: [Your explanation]\n\nModified Code:\n[Your modified code]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The explanation should accurately describe how the given code works.",
            "The modified code should meet the specified requirement.",
            "The modified code should be syntactically correct and logically sound."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
