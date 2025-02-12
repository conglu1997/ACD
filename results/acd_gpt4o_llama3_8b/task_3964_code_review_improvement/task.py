class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"code": "def add_numbers(a, b):\n    result = a + b\n    return result\n\n# Usage example\nprint(add_numbers(1, 2))"},
            "2": {"code": "def find_max(numbers):\n    if len(numbers) == 0:\n        return None\n    max_number = numbers[0]\n    for number in numbers:\n        if number > max_number:\n            max_number = number\n    return max_number\n\n# Usage example\nprint(find_max([1, 3, 2, 8, 5]))"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        code = t["code"]
        return f"""Review the following piece of code and suggest improvements. Focus on optimizing performance, enhancing readability, and ensuring best practices.\n\nCode:\n{code}\n\nSubmit your improved code as a plain text string in the following format:\n\nImproved Code:\n[Your improved code here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The improved code should be optimized for performance.",
            "The improved code should enhance readability.",
            "The improved code should follow best coding practices."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
