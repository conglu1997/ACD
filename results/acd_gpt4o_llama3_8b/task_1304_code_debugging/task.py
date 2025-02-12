class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"language": "Python", "code": "def add(a, b):\n    result = a - b\n    return result"},
            "2": {"language": "Python", "code": "def find_maximum(numbers):\n    max_num = 0\n    for num in numbers:\n        if num > max_num:\n            max_num = num\n    return max_num"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Identify and correct the errors in the following {t['language']} code. Ensure that the corrected code functions as intended.

Code:
{t['code']}

Submit your corrected code as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The corrected code should function as intended and not have any syntax errors."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
