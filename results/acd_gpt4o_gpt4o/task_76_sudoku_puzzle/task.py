class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task": "create"},
            "2": {"task": "solve", "puzzle": "530070000600195000098000060800060003400803001700020006060000280000419005000080079"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task"] == "create":
            return "Your task is to create a valid Sudoku puzzle. Provide the puzzle as an 81-character string representing the grid row by row, using '0' for empty cells. Ensure it has a unique solution. For example, a valid submission might look like '530070000600195000098000060800060003400803001700020006060000280000419005000080079'."
        elif t["task"] == "solve":
            return f"Your task is to solve the following Sudoku puzzle. Provide the solution as an 81-character string representing the grid row by row. The puzzle is: {t['puzzle']}"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["task"] == "create":
            criteria = [
                "The puzzle should be a valid Sudoku grid.",
                "The puzzle should have a unique solution.",
                "The puzzle should be provided as an 81-character string.",
                "The puzzle should use '0' for empty cells."
            ]
        elif t["task"] == "solve":
            criteria = [
                "The solution should be a valid completed Sudoku grid.",
                "The solution should be provided as an 81-character string."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
