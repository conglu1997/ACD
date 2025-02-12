class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task": "refactor", "code": "def calculate_sum(numbers):\n    total = 0\n    for num in numbers:\n        total += num\n    return total\n\n# Example usage:\n# result = calculate_sum([1, 2, 3, 4, 5])\n# Expected output: 15"},
            "2": {"task": "debug", "code": "def find_max(numbers):\n    max_val = None\n    for num in numbers:\n        if max_val is None or num > max_val:\n            max_val = num\n    return max_val.lower()\n\n# Example usage:\n# result = find_max([1, 2, 3, 4, 5])\n# Expected output: 5"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task"] == "refactor":
            return f"Your task is to refactor the following code to improve its efficiency and readability. Ensure that the refactored code maintains the same functionality as the original.\n\nOriginal Code:\n{t['code']}\n\nSubmit your refactored code in plain text format."
        elif t["task"] == "debug":
            return f"Your task is to debug the following code to correct any errors it might have. Ensure that the corrected code maintains the intended functionality.\n\nOriginal Code:\n{t['code']}\n\nSubmit your debugged code in plain text format."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["task"] == "refactor":
            criteria = [
                "The refactored code should be more efficient.",
                "The refactored code should be more readable.",
                "The refactored code should maintain the same functionality as the original."
            ]
        elif t["task"] == "debug":
            criteria = [
                "The debugged code should be free of errors.",
                "The debugged code should maintain the intended functionality.",
                "The debugged code should handle edge cases appropriately."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
