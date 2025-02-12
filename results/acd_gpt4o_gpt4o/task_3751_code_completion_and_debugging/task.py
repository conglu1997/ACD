class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "incomplete_code": "def factorial(n):\n    if n == 0:\n        return 1\n    else:\n        return n * factorial("
            },
            "2": {
                "buggy_code": "def is_prime(num):\n    if num <= 1:\n        return False\n    for i in range(2, num):\n        if num % i == 0,\n            return False\n    return True\n\nprint(is_prime(4))  # Should return False"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "incomplete_code" in t:
            return (
                "Your task is to complete the following partially written code snippet. "
                "Ensure that the completed code is functional and meets the intended purpose. "
                "Provide the complete code in plain text format."
                f'\n\nIncomplete Code: {t["incomplete_code"]}'
            )
        elif "buggy_code" in t:
            return (
                "Your task is to debug the following code snippet. "
                "Ensure that the corrected code is functional and meets the intended purpose. "
                "Provide the corrected code in plain text format."
                f'\n\nBuggy Code: {t["buggy_code"]}'
            )
        return ""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []
        if "incomplete_code" in t:
            criteria = [
                "The completed code should be functional and meet the intended purpose."
            ]
        elif "buggy_code" in t:
            criteria = [
                "The corrected code should be functional and meet the intended purpose."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
