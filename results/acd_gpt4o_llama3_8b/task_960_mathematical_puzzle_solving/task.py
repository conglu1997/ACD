class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "type": "Sudoku",
                "puzzle": [
                    [5, 3, 0, 0, 7, 0, 0, 0, 0],
                    [6, 0, 0, 1, 9, 5, 0, 0, 0],
                    [0, 9, 8, 0, 0, 0, 0, 6, 0],
                    [8, 0, 0, 0, 6, 0, 0, 0, 3],
                    [4, 0, 0, 8, 0, 3, 0, 0, 1],
                    [7, 0, 0, 0, 2, 0, 0, 0, 6],
                    [0, 6, 0, 0, 0, 0, 2, 8, 0],
                    [0, 0, 0, 4, 1, 9, 0, 0, 5],
                    [0, 0, 0, 0, 8, 0, 0, 7, 9]
                ]
            },
            "2": {
                "type": "Nonogram",
                "rows": [[4], [1, 1], [3], [1, 1], [4]],
                "cols": [[4], [1, 1], [3], [1, 1], [4]]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["type"] == "Sudoku":
            return f"""Solve the following Sudoku puzzle. The puzzle is represented as a 9x9 grid, where '0' represents an empty cell. Fill in the empty cells so that each row, column, and 3x3 subgrid contains the digits 1 to 9 exactly once.

Puzzle:
{chr(10).join(' '.join(map(str, row)) for row in t['puzzle'])}

Submit your solution as a 9x9 grid of digits, with each row on a new line, and digits separated by spaces. For example:
1 2 3 4 5 6 7 8 9
...
"""
        elif t["type"] == "Nonogram":
            return f"""Solve the following Nonogram (also known as Picross). The puzzle is represented by a list of row and column constraints, where each constraint specifies the lengths of contiguous blocks of filled cells in that row or column. Produce a 5x5 grid where '1' represents a filled cell and '0' represents an empty cell.

Row constraints: {', '.join(map(str, t['rows']))}
Column constraints: {', '.join(map(str, t['cols']))}

Submit your solution as a 5x5 grid of '0' and '1' characters, with each row on a new line, and characters separated by spaces. For example:
1 0 0 1 1
0 1 1 0 0
...
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["type"] == "Sudoku":
            validation_criteria = [
                "The solution should be a valid 9x9 Sudoku grid.",
                "Each row, column, and 3x3 subgrid should contain the digits 1 to 9 exactly once.",
                "The solution should be formatted as a 9x9 grid with each row on a new line and digits separated by spaces."
            ]
        elif t["type"] == "Nonogram":
            validation_criteria = [
                "The solution should be a valid 5x5 Nonogram grid.",
                "The grid should satisfy the given row and column constraints.",
                "The solution should be formatted as a 5x5 grid with each row on a new line and characters ('0' and '1') separated by spaces."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
