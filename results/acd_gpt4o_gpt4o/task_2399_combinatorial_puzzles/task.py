class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {'puzzle_type': 'sudoku', 'puzzle': '530070000600195000098000060800060003400803001700020006060000280000419005000080079'},
            '2': {'puzzle_type': 'tsp', 'distances': [[0, 29, 20, 21, 16, 30], [29, 0, 15, 17, 18, 28], [20, 15, 0, 28, 14, 22], [21, 17, 28, 0, 25, 24], [16, 18, 14, 25, 0, 19], [30, 28, 22, 24, 19, 0]], 'start': 0}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['puzzle_type'] == 'sudoku':
            return f"""Your task is to solve the given Sudoku puzzle. Fill in the missing numbers so that each row, column, and 3x3 subgrid contains all of the digits from 1 to 9. Provide your solution in the form of a single string of 81 digits, where each digit represents a cell in the Sudoku grid, read left-to-right and top-to-bottom.

Puzzle: {t['puzzle']}"""
        elif t['puzzle_type'] == 'tsp':
            return f"""Your task is to solve the Traveling Salesman Problem (TSP) for the given set of cities. Find the shortest possible route that visits each city exactly once and returns to the starting city. Provide your solution as a list of city indices in the order they should be visited.

Distances: {t['distances']}
Start City: {t['start']}"""
        else:
            return "Unknown puzzle type."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['puzzle_type'] == 'sudoku':
            criteria = [
                'The solution must be a valid Sudoku grid, with each row, column, and 3x3 subgrid containing all digits from 1 to 9.',
                'The solution must be provided as a single string of 81 digits.'
            ]
        elif t['puzzle_type'] == 'tsp':
            criteria = [
                'The solution must be a valid route that visits each city exactly once and returns to the starting city.',
                'The solution must be provided as a list of city indices.',
                'The solution must represent the shortest possible route.'
            ]
        else:
            return 0.0
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
