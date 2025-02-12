class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {'criteria': 'Generate a geometric problem involving a triangle with sides of lengths 3, 4, and 5. Solve for the area and the angles of the triangle.'},
            '2': {'criteria': 'Generate a geometric problem involving a circle inscribed in a square with a side length of 10 units. Solve for the area of the circle and the area of the square that is not covered by the circle.'}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Generate a geometric problem based on the following criteria: {t['criteria']}\nAfter generating the problem, provide a detailed solution that includes all necessary steps and calculations. Ensure that the problem and solution are clearly presented and logically consistent. Submit your response as a plain text string in the following format:\n\nProblem: [Your generated problem]\nSolution: [Your detailed solution]"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The generated problem should accurately reflect the given criteria.", "The solution should include all necessary steps and calculations.", "The solution should be logically consistent and mathematically correct.", "The response should follow the given format and cover both the problem and solution.", "The mathematical terminology and notation should be accurate."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
