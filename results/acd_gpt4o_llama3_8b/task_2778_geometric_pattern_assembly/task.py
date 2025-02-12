class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "pieces": [
                    "square", "triangle", "circle"
                ],
                "target_pattern": "a house with a triangular roof and a circular window"
            },
            "2": {
                "pieces": [
                    "rectangle", "circle", "triangle"
                ],
                "target_pattern": "a rocket with a triangular nose and circular windows"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        pieces = ', '.join(t["pieces"])
        target_pattern = t["target_pattern"]
        return f"""Assemble the following geometric shapes into the specified pattern:

Pieces: {pieces}
Target Pattern: {target_pattern}

Submit your solution as a plain text string describing the arrangement of pieces. Each piece should be listed with its position and orientation in the format:

Piece: [shape], Position: [x, y], Orientation: [angle]

Example:
Piece: square, Position: [0, 0], Orientation: [0 degrees]
Piece: triangle, Position: [0, 1], Orientation: [90 degrees]
Piece: circle, Position: [1, 0], Orientation: [0 degrees]

Ensure that your arrangement clearly forms the target pattern and that each piece is placed logically according to the description."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The solution should correctly form the specified pattern.", "The arrangement of pieces should be logically consistent and follow the given instructions."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
