class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem": "Design a geometric puzzle where the goal is to fit a set of shapes into a given area without any overlaps.", "example_shapes": ["small triangle", "small square", "small circle"], "area": "5x5 grid", "constraints": "All shapes must fit within the grid without overlapping. Shapes cannot be rotated."},
            "2": {"problem": "Solve the following geometric puzzle: Fit the given shapes into the specified area without any overlaps.", "shapes": ["small triangle: base=2, height=1", "small square: side=1", "small circle: radius=0.5"], "area": "4x4 grid", "constraints": "All shapes must fit within the grid without overlapping. Shapes cannot be rotated."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "example_shapes" in t:
            return f"""Your task is to design a geometric puzzle based on the following constraints:

{t["problem"]}

Example shapes: {t["example_shapes"]}
Area: {t["area"]}
Constraints: {t["constraints"]}

Provide a detailed description of the puzzle, including a solution that demonstrates how the shapes fit within the given area without overlapping. Your response should include the coordinates for placing each shape in the grid.

Example response format:
Puzzle description: Design a puzzle where the goal is to fit a small triangle, small square, and small circle into a 5x5 grid.
Solution:
Triangle: (x1, y1), (x2, y2), (x3, y3)
Square: (x4, y4), (x5, y5), (x6, y6), (x7, y7)
Circle: center at (x8, y8), radius=0.5"""
        else:
            return f"""Your task is to solve the following geometric puzzle:

{t["problem"]}

Shapes: {t["shapes"]}
Area: {t["area"]}
Constraints: {t["constraints"]}

Provide a detailed solution that demonstrates how the shapes fit within the given area without overlapping. Your response should include the coordinates for placing each shape in the grid.

Example response format:
Solution:
Triangle: (x1, y1), (x2, y2), (x3, y3)
Square: (x4, y4), (x5, y5), (x6, y6), (x7, y7)
Circle: center at (x8, y8), radius=0.5"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The solution should correctly fit all shapes within the specified area.",
            "There should be no overlaps between the shapes.",
            "The solution should adhere to the given constraints.",
            "The response should include coordinates for placing each shape in the grid."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
