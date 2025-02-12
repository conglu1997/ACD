class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"puzzle": "Arrange the following shapes within a 4x4 grid without overlapping: 1 square of size 2x2, 2 rectangles of size 1x2, and 1 line of size 1x4.", "grid_size": 4},
            "2": {"puzzle": "Fit the following pieces into a 5x5 grid without overlap: 1 square of size 3x3, 1 rectangle of size 1x4, and 2 rectangles of size 1x2.", "grid_size": 5}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        puzzle = t["puzzle"]
        grid_size = t["grid_size"]
        instructions = f"""Your task is to solve the following spatial puzzle:

{puzzle}

Ensure that all shapes fit within the {grid_size}x{grid_size} grid without overlapping. Provide your solution in plain text format, specifying the position and orientation of each shape. Use the following format for each shape:

Shape [number] ([size]): Top-left corner at ([row],[column]), [orientation]

Where:
- [number] is the shape number (e.g., 1, 2, 3).
- [size] is the dimensions of the shape (e.g., 2x2, 1x2).
- [row] and [column] are the coordinates of the top-left corner of the shape.
- [orientation] specifies whether the shape is horizontal or vertical.

Example for Task 1:
Shape 1 (2x2): Top-left corner at (0,0), horizontal
Shape 2 (1x2): Top-left corner at (2,0), vertical
Shape 3 (1x2): Top-left corner at (3,2), horizontal
Shape 4 (1x4): Top-left corner at (0,3), horizontal

Your solution should clearly indicate the position and orientation of each shape within the grid. Ensure that there are no overlaps and all shapes are within the grid boundaries. Use coordinates starting from (0,0) at the top-left corner. The grid is zero-indexed."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The shapes must fit within the specified grid size.",
            "No shapes should overlap.",
            "The solution should clearly indicate the position and orientation of each shape using the specified format.",
            "All shapes must be placed within the grid boundaries."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
