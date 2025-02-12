class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"shape": "triangle", "coordinates": [(0, 0), (1, 0), (0, 1)], "transformation": "rotate 90 degrees clockwise around the origin"},
            "2": {"shape": "square", "coordinates": [(0, 0), (1, 0), (1, 1), (0, 1)], "transformation": "reflect across the y-axis and then translate 2 units up"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to apply the given geometric transformation to the provided shape and describe the new coordinates of the transformed shape.

Shape: {t['shape']}
Original Coordinates: {t['coordinates']}
Transformation: {t['transformation']}

Provide the new coordinates of the shape after the transformation in the format [(x1, y1), (x2, y2), ...], maintaining the same order of points as given in the original shape."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The new coordinates should accurately reflect the specified transformation.",
            "The format of the coordinates should be correct.",
            "The transformation should be correctly applied based on geometric principles."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
