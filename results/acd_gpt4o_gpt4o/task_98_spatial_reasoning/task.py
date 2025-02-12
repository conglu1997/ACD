class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "Determine the number of faces, edges, and vertices of a given 3D shape: a dodecahedron."},
            "2": {"description": "Calculate the area of a triangle with sides of length 5, 6, and 7 using Heron's formula."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the following geometric problem. Provide your answer in the specified format:

{t['description']}

Format: [Answer]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The answer should be in the correct format and accurate."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
