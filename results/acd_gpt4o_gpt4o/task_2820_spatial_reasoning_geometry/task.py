class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {'problem': 'Given a list of coordinates representing vertices of a polygon, determine if it is a convex polygon. Coordinates are given in the format [(x1, y1), (x2, y2), ..., (xn, yn)]. The solution should handle negative coordinates and different polygon orientations correctly. Additionally, ensure to handle cases where the polygon has more than four vertices.', 'example': '[(0, 0), (2, 0), (2, 2), (0, 2)] -> True (This is a square, which is a convex polygon).'},
            '2': {'problem': 'You have a 3D cube with a side length of 4 units. Calculate the number of 1x1x1 unit cubes that are fully visible on the surface of the cube. Consider that each face of the cube is a 4x4 grid, and some cubes are shared between adjacent faces. Ensure your solution excludes internal cubes and counts only those visible on the surface.', 'example': 'Consider each face of the cube and the arrangement of the 1x1x1 unit cubes to determine the total visible surface cubes.'}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to solve the given geometric problem using spatial reasoning and geometric understanding. Make sure your solution is clear, well-structured, and correct.

Problem: {t['problem']}

Example: {t['example']}

Provide your response in plain text format, including any calculations or code you write as part of your solution."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The solution should correctly solve the problem.", "Any provided code should be syntactically correct and functional.", "The explanation should be clear and logically sound."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
