class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"type": "Sudoku", "grid": [[5, 3, 0, 0, 7, 0, 0, 0, 0], [6, 0, 0, 1, 9, 5, 0, 0, 0], [0, 9, 8, 0, 0, 0, 0, 6, 0], [8, 0, 0, 0, 6, 0, 0, 0, 3], [4, 0, 0, 8, 0, 3, 0, 0, 1], [7, 0, 0, 0, 2, 0, 0, 0, 6], [0, 6, 0, 0, 0, 0, 2, 8, 0], [0, 0, 0, 4, 1, 9, 0, 0, 5], [0, 0, 0, 0, 8, 0, 0, 7, 9]]},
            "2": {"type": "KenKen", "size": 4, "cages": {"1": {"cells": [[0, 0], [0, 1]], "operation": "+", "result": 3}, "2": {"cells": [[0, 2], [1, 2]], "operation": "/", "result": 2}, "3": {"cells": [[0, 3], [1, 3]], "operation": "*", "result": 6}, "4": {"cells": [[1, 0], [1, 1]], "operation": "-", "result": 1}, "5": {"cells": [[2, 0], [3, 0]], "operation": "+", "result": 4}, "6": {"cells": [[2, 2], [3, 2]], "operation": "*", "result": 6}, "7": {"cells": [[2, 3], [3, 3]], "operation": "/", "result": 2}}}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['type'] == 'Sudoku':
            return f"""Your task is to solve the following Sudoku puzzle. Fill in the grid so that each row, each column, and each 3x3 subgrid contains all the digits from 1 to 9. The initial grid is as follows:

{t['grid']}

Provide your solution as a 9x9 grid in plain text format, with each row on a new line and each number separated by a space. For example:
1 2 3 4 5 6 7 8 9
4 5 6 7 8 9 1 2 3
..."""
        elif t['type'] == 'KenKen':
            return f"""Your task is to solve the following KenKen puzzle. Fill in the grid so that each row and each column contains all the digits from 1 to {t['size']}. The cages are defined as follows:

{t['cages']}

Provide your solution as a {t['size']}x{t['size']} grid in plain text format, with each row on a new line and each number separated by a space. For example:
1 2 3 4
3 4 1 2
..."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The solution must satisfy all the constraints of the puzzle.",
            "For Sudoku, each row, column, and 3x3 subgrid must contain all the digits from 1 to 9.",
            "For KenKen, each row and column must contain all the digits from 1 to the grid size, and the values in each cage must satisfy the given arithmetic operations and results."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
