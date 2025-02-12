class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"shapes": ["two 2x2 squares", "two right triangles with legs of length 2", "a 1x2 rectangle"], "pattern": "Create a larger square with side length 4 by combining the given shapes."},
            "2": {"shapes": ["a circle with radius 1", "an equilateral triangle with side length 2", "a square with side length 3"], "pattern": "Create a pattern where the circle is completely inside the square, and the triangle is outside both the circle and the square."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        shapes = ', '.join(t['shapes'])
        pattern = t['pattern']
        return f"""Your task is to solve the given geometric puzzle by manipulating the provided shapes to fit the specified pattern.

Shapes: {shapes}
Pattern: {pattern}

Provide your solution in plain text format, describing the final arrangement and any transformations (e.g., rotations, flips) applied to the shapes to achieve the pattern. Use clear and precise language to describe the spatial relationships and transformations.

Example response format:
1. Arrangement: The two 2x2 squares are placed side by side to form a 4x2 rectangle. The right triangles are rotated and placed at the top and bottom of the rectangle to form a 4x4 square. The 1x2 rectangle is placed in the remaining space to complete the larger square.
2. Transformations: The right triangles are rotated 90 degrees.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should clearly describe the final arrangement of the shapes.",
            "The response should specify any transformations applied to the shapes.",
            "The arrangement should satisfy the given pattern."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
