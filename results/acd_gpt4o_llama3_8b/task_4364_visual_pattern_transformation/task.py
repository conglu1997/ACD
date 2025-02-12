class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"initial_pattern": "X O X\nO X O\nX O X", "transformation": "rotate 90 degrees clockwise"},
            "2": {"initial_pattern": "X X O\nX O X\nO X X", "transformation": "reflect horizontally"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        initial_pattern = t['initial_pattern']
        transformation = t['transformation']
        return f"Given the following initial pattern represented textually, describe the pattern after applying the specified transformation.\n\nInitial Pattern:\n{initial_pattern}\nTransformation: {transformation}\n\nSubmit your response as a plain text string in the following format:\n\nTransformed Pattern:\n[Your transformed pattern here]\n\nEnsure your transformed pattern maintains the original structure and alignment. Clearly indicate the rows and columns by separating them with line breaks (\n). The pattern should not contain any extra characters or lines."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The transformed pattern should accurately reflect the specified transformation.",
            "The transformed pattern should maintain the structure and alignment of the original pattern.",
            "The pattern should be clearly divided into rows with line breaks.",
            "The pattern should not contain any extra characters or lines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
