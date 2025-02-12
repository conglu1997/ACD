class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"code": "def add_numbers(a, b):\n    return a - b\n\nresult = add_numbers(5, 3)\nprint(result)", "bug": "The function should add the numbers, not subtract them."},
            "2": {"code": "def find_maximum(numbers):\n    if not numbers:\n        return None\n    max_num = numbers[0]\n    for num in numbers[1:]:\n        if num > max_num:\n            max_num = num\n    return max_num\n\nresult = find_maximum([])\nprint(result)", "bug": "The function does not handle empty lists correctly and will return None instead of indicating an error."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        code = t["code"]
        return f"""Identify and explain the bug in the following piece of code:\n\n{code}\n\nProvide a clear and complete explanation of what the bug is, why it occurs, and suggest a possible fix. Submit your explanation as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The explanation should clearly identify the bug.",
            "The explanation should accurately describe why the bug occurs.",
            "The explanation should be concise, coherent, and complete.",
            "The explanation should suggest a possible fix for the bug."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
