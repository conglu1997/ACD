class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"puzzle": "Given a 3x3 grid, fill it with numbers 1 to 9 such that each row, column, and diagonal sums to 15."},
            "2": {"puzzle": "Given a 4x4 grid with some pre-filled numbers, complete the grid such that each row, column, and both main diagonals have all numbers from 1 to 4 with no repetitions.", "pre_filled": [[1, None, None, 4], [None, 2, None, None], [None, None, 3, None], [None, 4, None, None]]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to solve the following spatial puzzle:

{t['puzzle']}"""
        if 'pre_filled' in t:
            instructions += f"\n\nPre-filled grid:\n{t['pre_filled']}"
        instructions += "\n\nProvide your solution as a list of lists, where each inner list represents a row of the grid. For example, for a 3x3 grid, your solution should look like this:\n[[1, 2, 3], [4, 5, 6], [7, 8, 9]]."
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        try:
            solution = eval(submission)
            if not isinstance(solution, list) or not all(isinstance(row, list) for row in solution):
                return 0.0

            if t['puzzle'].startswith("Given a 3x3 grid"):
                if len(solution) != 3 or any(len(row) != 3 for row in solution):
                    return 0.0
                sums = [sum(row) for row in solution] + [sum(solution[i][j] for i in range(3)) for j in range(3)] + [sum(solution[i][i] for i in range(3)), sum(solution[i][2-i] for i in range(3))]
                return 1.0 if all(s == 15 for s in sums) else 0.0

            elif t['puzzle'].startswith("Given a 4x4 grid"):
                if len(solution) != 4 or any(len(row) != 4 for row in solution):
                    return 0.0
                pre_filled_correct = True
                if 'pre_filled' in t:
                    for i in range(4):
                        for j in range(4):
                            if t['pre_filled'][i][j] is not None and t['pre_filled'][i][j] != solution[i][j]:
                                pre_filled_correct = False
                                break
                rows_valid = all(len(set(row)) == 4 for row in solution)
                cols_valid = all(len(set(solution[i][j] for i in range(4))) == 4 for j in range(4))
                diags_valid = len(set(solution[i][i] for i in range(4))) == 4 and len(set(solution[i][3-i] for i in range(4))) == 4
                return 1.0 if pre_filled_correct and rows_valid and cols_valid and diags_valid else 0.0

            return 0.0
        except Exception as e:
            return 0.0
