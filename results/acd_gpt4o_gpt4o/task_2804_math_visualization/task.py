class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "problem": "Find the intersection points of the parabola y = x^2 and the line y = 2x + 3.",
                "visualization_task": "Describe the visual representation of the parabola and the line, and their intersection points on the Cartesian plane."
            },
            "2": {
                "problem": "Solve the system of equations: 3x + 2y = 6 and x - y = 2.",
                "visualization_task": "Describe the visual representation of the solution to the system of equations on the Cartesian plane."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        problem = t["problem"]
        visualization_task = t["visualization_task"]
        instructions = f"""Your task is to solve the following mathematical problem and describe its visual representation:

Problem: {problem}

After solving the problem, provide a detailed description of how the solution can be visualized. Your description should include the shapes and positions of any relevant graphs, lines, or points on the Cartesian plane. Ensure your explanation is clear and coherent, and accurately reflects the mathematical solution.

Response format:
1. Solution to the problem
2. Visual description of the solution"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The submission should include a correct solution to the mathematical problem.", "The visual description should accurately reflect the solution and be clearly described."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
