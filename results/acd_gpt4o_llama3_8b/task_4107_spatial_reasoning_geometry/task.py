class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "problem": "Consider a cube with a side length of 3 units. If a plane cuts through the cube diagonally from one vertex to the opposite vertex, what is the shape and area of the resulting cross-section? Clearly describe the shape and provide the exact area of the cross-section in square units. Note that the plane passes through the centers of the edges it intersects."
            },
            "2": {
                "problem": "You have a regular tetrahedron with edge length 4 units. If you slice the tetrahedron with a plane parallel to one of its faces and halfway between that face and the opposite vertex, what is the shape and area of the resulting cross-section? Clearly describe the shape and provide the exact area of the cross-section in square units. Assume the plane is equidistant from the three vertices of the face opposite to the vertex."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the following geometric problem:

Problem:
{t['problem']}

Submit your response as a plain text string in the following format:

Shape: [The shape of the cross-section]
Area: [The exact area of the cross-section in square units]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'cube' in t['problem']:
            criteria = [
                "The shape should be a regular hexagon.",
                "The area should be 9√3 square units."
            ]
        else:
            criteria = [
                "The shape should be an equilateral triangle.",
                "The area should be 4√3 square units."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
