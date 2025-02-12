class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"grid_size": 5, "row_clues": [[1], [3], [1, 1], [3], [1]], "col_clues": [[1], [2], [3], [2], [1]]},
            "2": {"grid_size": 5, "row_clues": [[3], [1, 1], [3], [1], [1]], "col_clues": [[1], [3], [1, 1], [3], [1]]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        grid_size = t['grid_size']
        row_clues = t['row_clues']
        col_clues = t['col_clues']
        return f"""Solve the following nonogram puzzle by filling in the grid according to the given row and column clues.

Grid Size: {grid_size}x{grid_size}

Row Clues: {row_clues}
Column Clues: {col_clues}

Submit your solution as a string representing the grid, with '1' for filled cells and '0' for empty cells, row by row without spaces.
For example, for a 2x2 grid where the first row is completely filled and the second row is completely empty, submit '1100'.

Ensure your submission string is exactly {grid_size * grid_size} characters long."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from itertools import groupby

        def is_valid_solution(grid_size, row_clues, col_clues, grid):
            # Check rows
            for i, clue in enumerate(row_clues):
                row = grid[i]
                groups = [len(list(g)) for k, g in groupby(row) if k == '1']
                if groups != clue:
                    return False
            # Check columns
            for j, clue in enumerate(col_clues):
                col = ''.join(grid[i][j] for i in range(grid_size))
                groups = [len(list(g)) for k, g in groupby(col) if k == '1']
                if groups != clue:
                    return False
            return True

        grid_size = t['grid_size']
        row_clues = t['row_clues']
        col_clues = t['col_clues']
        grid = [submission[i:i+grid_size] for i in range(0, len(submission), grid_size)]

        if len(submission) != grid_size * grid_size:
            return 0.0

        if is_valid_solution(grid_size, row_clues, col_clues, grid):
            return 1.0
        else:
            return 0.0
