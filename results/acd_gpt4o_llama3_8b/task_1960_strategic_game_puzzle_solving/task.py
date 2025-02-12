class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"game": "chess", "position": "rnbqkb1r/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq - 0 2", "solution": "d7d5"},
            "2": {"game": "sudoku", "grid": "5 3 . . 7 . . . .\n6 . . 1 9 5 . . .\n. 9 8 . . . . 6 .\n8 . . . 6 . . . 3\n4 . . 8 . 3 . . 1\n7 . . . 2 . . . 6\n. 6 . . . . 2 8 .\n. . . 4 1 9 . . 5\n. . . . 8 . . 7 9"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["game"] == "chess":
            return f"""Solve the following chess puzzle. The current position is given in Forsyth-Edwards Notation (FEN): {t["position"]}. Your task is to find the best move for Black. Provide your move in standard algebraic notation (e.g., e7e5)."""
        elif t["game"] == "sudoku":
            return f"""Solve the following Sudoku puzzle. The current grid is given below, where a dot (.) represents an empty cell:
{t["grid"]}
Provide the completed grid with each row separated by a newline, and each cell separated by a space."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        if t["game"] == "chess":
            return 1.0 if submission == t["solution"] else 0.0
        elif t["game"] == "sudoku":
            import numpy as np
            def is_valid_sudoku(grid):
                for i in range(9):
                    row = grid[i]
                    col = grid[:, i]
                    box = grid[i//3*3:(i//3+1)*3, i%3*3:(i%3+1)*3]
                    if len(set(row)) != len(row) or len(set(col)) != len(col) or len(set(box.flatten())) != len(box.flatten()):
                        return False
                return True
            try:
                solved_grid = np.array([list(map(int, row.split())) for row in submission.strip().split('\n')])
                return 1.0 if is_valid_sudoku(solved_grid) else 0.0
            except Exception:
                return 0.0
