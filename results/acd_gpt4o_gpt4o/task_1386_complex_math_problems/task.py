class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem": "Calculate the volume of a frustum of a cone with a height of 10 units, and radii of 5 units and 3 units at the base and top, respectively."},
            "2": {"problem": "Determine the eigenvalues of the following 3x3 matrix: [[4, 1, 2], [1, 3, 1], [2, 1, 3]]."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to solve the following mathematical problem:

Problem: {t["problem"]}

Provide a detailed solution with all necessary steps and calculations. Ensure that your solution is comprehensive and accurate. Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The solution should include all necessary steps.", "The calculations should be accurate.", "The final answer should be correct."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
