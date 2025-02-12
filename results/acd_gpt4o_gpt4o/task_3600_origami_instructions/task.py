class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"instructions": "Fold a square paper in half diagonally to form a triangle. Unfold, then fold the paper in half diagonally in the opposite direction to form a triangle. Unfold, then fold the paper in half horizontally to form a rectangle. Unfold, then fold the paper in half vertically to form a rectangle. Unfold."},
            "2": {"shape": "crane"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'instructions' in t:
            return f"""Your task is to interpret the following origami instructions and describe the resulting shape. Provide your description in plain text format.

Instructions: {t['instructions']}

Ensure your description is clear and accurately represents the final shape formed by following the instructions."""
        else:
            return f"""Your task is to generate origami instructions to create the following shape. Provide your instructions in plain text format.

Shape: {t['shape']}

Ensure your instructions are clear, detailed, and can be followed step-by-step to recreate the specified shape."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'instructions' in t:
            criteria = ["The description should accurately represent the final shape formed by following the instructions."]
        else:
            criteria = ["The instructions should be clear and detailed.", "The instructions should accurately describe the steps to create the specified shape."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
