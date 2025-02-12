class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"type": "grid_puzzle", "puzzle": "530070000600195000098000060800060003400803001700020006060000280000419005000080079"},
            "2": {"type": "verbal_puzzle", "puzzle": "Knights always tell the truth, and knaves always lie. You meet two inhabitants: A and B. A says 'We are both knights.' B says 'A is a knave.' What are A and B?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["type"] == "grid_puzzle":
            puzzle = t["puzzle"]
            return f"""Solve the following grid-based logical puzzle (similar to Sudoku). Fill in the missing numbers so that each row, column, and 3x3 subgrid contains all the digits from 1 to 9 without repetition. Provide the solved grid in a 9x9 format using '.' for blanks and a detailed explanation of your solving process:

Puzzle: {puzzle}

Solution: [Solved grid in a 9x9 format using '.' for blanks]
Explanation: [Your detailed solving process]"""
        elif t["type"] == "verbal_puzzle":
            puzzle = t["puzzle"]
            return f"""Solve the following logical puzzle. Determine the identities of the inhabitants based on the given statements. Provide your answer and a step-by-step explanation of your reasoning:

Puzzle: {puzzle}

Answer: [Your answer]
Explanation: [Your detailed step-by-step reasoning]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["type"] == "grid_puzzle":
            criteria = [
                "The solved grid must be correct, with each row, column, and 3x3 subgrid containing all digits from 1 to 9 without repetition.",
                "The explanation should describe the steps taken to solve the puzzle in detail."
            ]
        elif t["type"] == "verbal_puzzle":
            criteria = [
                "The answer must correctly identify the inhabitants as knights or knaves based on the given statements.",
                "The explanation should provide a clear, detailed step-by-step reasoning process."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
