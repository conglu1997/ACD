class TaskFamily:
    from typing import Optional

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"puzzle_type": "Sudoku", "difficulty": "medium"},
            "2": {"puzzle_type": "Sudoku", "difficulty": "hard"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a {t['difficulty']} {t['puzzle_type']} puzzle and provide its solution. The puzzle should be valid and solvable. Submit your response in the following format:

Puzzle:
[The generated puzzle in a 9x9 grid format with '0' for empty cells]

Solution:
[The solved puzzle in a 9x9 grid format]

Example:
Puzzle:
5 3 0 0 7 0 0 0 0
6 0 0 1 9 5 0 0 0
0 9 8 0 0 0 0 6 0
8 0 0 0 6 0 0 0 3
4 0 0 8 0 3 0 0 1
7 0 0 0 2 0 0 0 6
0 6 0 0 0 0 2 8 0
0 0 0 4 1 9 0 0 5
0 0 0 0 8 0 0 7 9

Solution:
5 3 4 6 7 8 9 1 2
6 7 2 1 9 5 3 4 8
1 9 8 3 4 2 5 6 7
8 5 9 7 6 1 4 2 3
4 2 6 8 5 3 7 9 1
7 1 3 9 2 4 8 5 6
9 6 1 5 3 7 2 8 4
2 8 7 4 1 9 6 3 5
3 4 5 2 8 6 1 7 9"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        def is_valid_sudoku(board: list[list[int]]) -> bool:
            def is_valid_unit(unit: list[int]) -> bool:
                unit = [i for i in unit if i != 0]
                return len(unit) == len(set(unit))

            for row in board:
                if not is_valid_unit(row):
                    return False
            for col in zip(*board):
                if not is_valid_unit(col):
                    return False
            for i in range(0, 9, 3):
                for j in range(0, 9, 3):
                    if not is_valid_unit([board[x][y] for x in range(i, i+3) for y in range(j, j+3)]):
                        return False
            return True

        try:
            puzzle_str, solution_str = submission.split("Solution:")
            puzzle = [[int(num) for num in line.split()] for line in puzzle_str.strip().split("\n")]
            solution = [[int(num) for num in line.split()] for line in solution_str.strip().split("\n")]
        except Exception as e:
            return 0.0

        if not is_valid_sudoku(solution):
            return 0.0

        for i in range(9):
            for j in range(9):
                if puzzle[i][j] != 0 and puzzle[i][j] != solution[i][j]:
                    return 0.0

        return 1.0
