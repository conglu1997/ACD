class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"sequence": [2, 4, 8, 16]},
            "2": {"sequence": [1, 1, 2, 3, 5, 8]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        sequence = t['sequence']
        return f"""Identify the next element in the following sequence: {sequence}. Explain the pattern you used to determine the next element. Ensure your explanation is clear and demonstrates your understanding of the pattern.

Submit your response as a plain text string in the following format:
'Next Element: [Your next element] Explanation: [Your explanation]'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The explanation should clearly demonstrate the pattern used.",
            "The next element should be correctly identified based on the pattern."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
