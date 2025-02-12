class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task": "Create a unique logic puzzle that has a specific solution. Provide the puzzle and its solution."},
            "2": {"task": "Solve the following logic puzzle: \n\nPuzzle: Three people (A, B, and C) each have a different favorite fruit (apple, banana, cherry). A's favorite fruit is not apple. B's favorite fruit is not banana. C's favorite fruit is not cherry. What is each person's favorite fruit?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to complete the following puzzle challenge: \n\nTask: {t["task"]}\n\nEnsure that your response is clear, logical, and provides a unique puzzle with a specific solution or a correct solution to the given puzzle. Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []
        if t["task"].startswith("Create a unique logic puzzle"):
            criteria = [
                "The puzzle should be unique and original.",
                "The puzzle should have a clear and specific solution.",
                "The solution to the puzzle should be logical and correct.",
                "The puzzle should be solvable and the solution should be provided."
            ]
        elif t["task"].startswith("Solve the following logic puzzle"):
            criteria = [
                "The solution should correctly address the puzzle.",
                "The solution should be logical and well-explained."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
