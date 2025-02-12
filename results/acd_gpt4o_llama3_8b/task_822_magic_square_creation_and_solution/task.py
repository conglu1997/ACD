class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task": "create"},
            "2": {"task": "solve", "grid": [[2, 7, 6], [9, 5, 1], [4, 3, 0]]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task"] == "create":
            return "Create a 3x3 magic square. A magic square is a grid of numbers where the sum of each row, column, and diagonal is the same. Submit your magic square as a list of lists, where each inner list represents a row in the grid. For example, [[2, 7, 6], [9, 5, 1], [4, 3, 8]]."
        elif t["task"] == "solve":
            grid = t["grid"]
            instructions = "Solve the following 3x3 magic square puzzle. Fill in the missing number (represented by 0) such that the sum of each row, column, and diagonal is the same. Submit your solution as a list of lists, where each inner list represents a row in the grid.\n"
            for row in grid:
                instructions += f"{row}\n"
            return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        def is_valid_magic_square(grid):
            target_sum = sum(grid[0])
            for row in grid:
                if sum(row) != target_sum:
                    return False
            for col in range(3):
                if sum(grid[row][col] for row in range(3)) != target_sum:
                    return False
            if sum(grid[i][i] for i in range(3)) != target_sum or sum(grid[i][2-i] for i in range(3)) != target_sum:
                return False
            return True

        try:
            solution = eval(submission)
            if not isinstance(solution, list) or len(solution) != 3 or not all(len(row) == 3 for row in solution):
                return 0.0
            return 1.0 if is_valid_magic_square(solution) else 0.0
        except:
            return 0.0
