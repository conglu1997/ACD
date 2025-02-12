class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "initial_shape": "triangle",
                "initial_coordinates": [(0,0), (1,0), (0,1)],
                "transformations": ["rotate 90 degrees clockwise", "translate right by 3 units"]
            },
            "2": {
                "initial_shape": "square",
                "initial_coordinates": [(0,0), (1,0), (1,1), (0,1)],
                "transformations": ["reflect over the y-axis", "translate up by 2 units"]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Describe the final position and orientation of the shape after applying the following transformations in order:

Initial Shape: {t['initial_shape']}
Initial Coordinates: {t['initial_coordinates']}
Transformations: {', '.join(t['transformations'])}

Your description should include the final coordinates of each vertex and the orientation of the shape. Submit your response as a plain text string in the format: 'Coordinates: [(x1, y1), (x2, y2), ...], Orientation: [description]'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The description should include the final coordinates of each vertex.",
            "The description should include the final orientation of the shape.",
            "The description should accurately reflect the result of applying the transformations in the correct order."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
