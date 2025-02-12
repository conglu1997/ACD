class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "shapes": [
                    "small_triangle_1",
                    "small_triangle_2",
                    "medium_triangle",
                    "large_triangle_1",
                    "large_triangle_2",
                    "square",
                    "parallelogram"
                ],
                "figure": "square"
            },
            "2": {
                "shapes": [
                    "small_triangle_1",
                    "small_triangle_2",
                    "medium_triangle",
                    "large_triangle_1",
                    "large_triangle_2",
                    "square",
                    "parallelogram"
                ],
                "figure": "triangle"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the following tangram puzzle by arranging the provided shapes to form the specified figure:

Shapes: {', '.join(t['shapes'])}
Figure: {t['figure']}

Describe your solution as a sequence of steps detailing how to position each shape to form the figure. Include details such as the position (e.g., top-left, bottom-right), orientation (e.g., rotated 90 degrees clockwise), and relative placement (e.g., adjacent to the square) of each shape. Submit your solution as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The solution should correctly describe how to arrange the provided shapes to form the specified figure.",
            "The description should be detailed enough to understand the final arrangement of shapes.",
            "The response should be coherent and logically sequenced."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
