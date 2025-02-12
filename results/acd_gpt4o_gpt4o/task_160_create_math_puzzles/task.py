class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"criteria": "Create a puzzle involving prime numbers and their properties."},
            "2": {"criteria": "Create a puzzle that involves solving a system of linear equations."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a mathematical puzzle based on the following criteria: {t["criteria"]}. Ensure that the puzzle is challenging, solvable, and adheres to the given criteria. Provide the puzzle and its solution in plain text format. The solution should include a clear explanation of the steps taken to solve the puzzle."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The puzzle should be challenging and solvable.", "The puzzle must adhere to the given criteria.", "The solution should be correct and clearly explained."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
