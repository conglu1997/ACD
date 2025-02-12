class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"shape": "an L-shape made of 4 squares in a 3x3 grid (2 squares forming the base and 2 squares forming the vertical leg)", "rotation": "90 degrees clockwise"},
            "2": {"shape": "a T-shape made of 5 squares with the base in the center (3 squares forming the horizontal bar and 2 squares forming the vertical leg)", "rotation": "180 degrees"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to mentally rotate the given geometric shape by the specified amount and describe its new orientation. Ensure your description is clear enough for someone to mentally visualize the new orientation. Use the following format for your response:

New Orientation: [Your description]

Shape: {t['shape']}
Rotation: {t['rotation']}

Example: If the shape was an 'L-shape made of 4 squares in a 2x2 grid' and the rotation was '90 degrees clockwise', the response could be 'New Orientation: The shape now looks like an inverted L in a 2x2 grid, with the vertical leg on the right and the base at the top.'"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The description should accurately reflect the new orientation of the shape after the specified rotation.",
            "The description should be clear and easy to visualize.",
            "The response should use the format 'New Orientation: [Your description]'."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
