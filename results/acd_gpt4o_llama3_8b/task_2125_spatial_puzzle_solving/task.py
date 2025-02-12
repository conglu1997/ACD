class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"puzzle": "Arrange the following Tetris-like pieces to completely fill a 4x4 grid: L-shape, T-shape, and two I-shapes."},
            "2": {"puzzle": "Place the numbers 1 to 9 in a 3x3 grid such that each row, column, and diagonal sums to 15."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        puzzle = t["puzzle"]
        return f"""Solve the following spatial puzzle:

{puzzle}

Provide your solution in a clear and logical format. For grid-based puzzles, represent the grid using a 2D array or matrix format. Ensure that there are no empty spaces or repeated numbers in your solution. Example format for a 4x4 grid:
[[0, 0, 0, 0],
 [0, 0, 0, 0],
 [0, 0, 0, 0],
 [0, 0, 0, 0]]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        try:
            submission_grid = eval(submission)
            if t["puzzle"].startswith("Arrange the following Tetris-like pieces"):
                # Check if the grid is completely filled with no empty spaces
                if len(submission_grid) == 4 and all(len(row) == 4 for row in submission_grid) and all(all(cell != 0 for cell in row) for row in submission_grid):
                    return 1.0
                else:
                    return 0.0
            elif t["puzzle"].startswith("Place the numbers 1 to 9 in a 3x3 grid"):
                # Check if the grid is 3x3 and contains numbers 1 to 9 with no repeats
                if len(submission_grid) == 3 and all(len(row) == 3 for row in submission_grid):
                    flattened_grid = [cell for row in submission_grid for cell in row]
                    if sorted(flattened_grid) == list(range(1, 10)):
                        # Check if each row, column, and diagonal sums to 15
                        rows = all(sum(row) == 15 for row in submission_grid)
                        cols = all(sum(submission_grid[i][j] for i in range(3)) == 15 for j in range(3))
                        diag1 = sum(submission_grid[i][i] for i in range(3)) == 15
                        diag2 = sum(submission_grid[i][2-i] for i in range(3)) == 15
                        if rows and cols and diag1 and diag2:
                            return 1.0
                return 0.0
        except:
            return 0.0
