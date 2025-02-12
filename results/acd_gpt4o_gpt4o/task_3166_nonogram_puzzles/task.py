class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"rows": [[2], [1, 1], [2]], "cols": [[1], [2], [1, 1], [2], [1]]},
            "2": {"rows": [[1], [3], [1, 1], [3], [1]], "cols": [[1], [1, 1], [3], [1, 1], [1]]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to solve the following nonogram puzzle. A nonogram is a grid-based puzzle where you need to fill in certain cells based on the numerical clues provided for each row and column. The clues indicate the lengths of consecutive filled cells in the respective row or column, separated by at least one empty cell.

Row Clues: {t['rows']}
Column Clues: {t['cols']}

Provide your solution as a grid of 0s and 1s, where 1 indicates a filled cell and 0 indicates an empty cell. Each row in the grid should be represented as a separate line of 0s and 1s. Ensure there are no additional spaces or characters in your submission.

Example format:
0 1 0
1 1 1
0 1 0
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The grid must match the numerical clues for both rows and columns.", "The solution must be formatted as specified in the instructions, with rows separated by newline characters and no additional spaces or characters.", "The submission must contain the exact number of rows and columns as the clues provided."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
