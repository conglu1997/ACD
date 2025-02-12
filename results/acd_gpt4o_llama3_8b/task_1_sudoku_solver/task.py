class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"grid": [[1, 0, 0, 0], [0, 0, 0, 2], [0, 3, 0, 0], [0, 0, 4, 0]]},
            "2": {"grid": [[0, 0, 3, 0], [0, 1, 0, 0], [0, 0, 0, 4], [2, 0, 0, 0]]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        grid = t["grid"]
        instructions = "Solve the following 4x4 Sudoku puzzle. Each row, column, and 2x2 subgrid must contain the numbers 1 to 4 exactly once. Represent the grid as a list of lists.\n"
        for row in grid:
            instructions += f"{row}\n"
        instructions += "\nSubmit your solution as a list of lists, where each inner list represents a row in the grid. For example, [[1, 2, 3, 4], [3, 4, 1, 2], [2, 3, 4, 1], [4, 1, 2, 3]]"
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        def is_valid_sudoku(grid):
            def is_valid_group(group):
                return sorted(group) == [1, 2, 3, 4]

            for row in grid:
                if not is_valid_group(row):
                    return False
            for col in range(4):
                if not is_valid_group([grid[row][col] for row in range(4)]):
                    return False
            for box_row in range(2):
                for box_col in range(2):
                    if not is_valid_group([grid[r][c] for r in range(box_row*2, box_row*2+2) for c in range(box_col*2, box_col*2+2)]):
                        return False
            return True

        try:
            solution = eval(submission)
            if not isinstance(solution, list) or len(solution) != 4 or not all(len(row) == 4 for row in solution):
                return 0.0
            return 1.0 if is_valid_sudoku(solution) else 0.0
        except:
            return 0.0
