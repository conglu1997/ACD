class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"data": [2, 4, 8, 16, 32], "pattern": "Each number is double the previous one."},
            "2": {"data": [1, 1, 2, 3, 5, 8, 13], "pattern": "Each number is the sum of the two preceding ones (Fibonacci sequence)."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Identify the pattern or sequence in the following set of data: {t['data']}. Explain the pattern clearly and concisely. Submit your response in the following format:
Pattern: [Your explanation here]

Your explanation should describe the rule or formula that generates the sequence."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        pattern = t['pattern']
        criteria = [f"The explanation must clearly identify the pattern as: {pattern}", "The explanation must be logically consistent with the data provided."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
