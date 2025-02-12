class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"grid": [[1, 2, 4], [8, 16, 32], [64, 128, 256]]},
            "2": {"sequence": [1, 1, 2, 3, 5, 8, 13]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "grid" in t:
            return f"""Your task is to identify the pattern in the following grid of numbers and describe it in detail:

{t["grid"]}

In your description, you should explain the relationship between the numbers, any noticeable sequences or patterns, and any mathematical rules that apply. Ensure your explanation is clear and logical. Provide your response in plain text format. Structure your response as follows:

1. Identified Pattern: [Your identified pattern]
2. Explanation: [Detailed explanation of the pattern]"""
        elif "sequence" in t:
            return f"""Your task is to identify the pattern in the following sequence of numbers and describe it in detail:

{t["sequence"]}

In your description, you should explain the relationship between the numbers, any noticeable sequences or patterns, and any mathematical rules that apply. Ensure your explanation is clear and logical. Provide your response in plain text format. Structure your response as follows:

1. Identified Pattern: [Your identified pattern]
2. Explanation: [Detailed explanation of the pattern]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "grid" in t:
            criteria = [
                "The explanation should identify the pattern in the grid.",
                "The explanation should describe the relationship between the numbers.",
                "The explanation should be clear and logical.",
            ]
        elif "sequence" in t:
            criteria = [
                "The explanation should identify the pattern in the sequence.",
                "The explanation should describe the relationship between the numbers.",
                "The explanation should be clear and logical.",
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
