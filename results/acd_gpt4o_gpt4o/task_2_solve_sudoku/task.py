class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
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
                "puzzle": [
                    [0, 0, 0, 2, 6, 0, 7, 0, 1],
                    [6, 8, 0, 0, 7, 0, 0, 9, 0],
                    [1, 9, 0, 0, 0, 4, 5, 0, 0],
                    [8, 2, 0, 1, 0, 0, 0, 4, 0],
                    [0, 0, 4, 6, 0, 2, 9, 0, 0],
                    [0, 5, 0, 0, 0, 3, 0, 2, 8],
                    [0, 0, 9, 3, 0, 0, 0, 7, 4],
                    [0, 4, 0, 0, 5, 0, 0, 3, 6],
                    [7, 0, 3, 0, 1, 8, 0, 0, 0]
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        puzzle = t["puzzle"]
        instructions = """Your task is to solve the following Sudoku puzzle and provide the completed grid. Replace the zeros (0s) with the correct numbers to ensure that each row, each column, and each 3x3 subgrid contain all of the digits from 1 to 9.

Submit your completed grid as a list of lists, where each inner list represents a row of the grid.

Sudoku Puzzle:
"""
        for row in puzzle:
            instructions += " ".join(map(str, row)) + "\n"
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "Each row, column, and 3x3 subgrid must contain all of the digits from 1 to 9.",
            "The completed grid must match the original grid where the cells were not zero."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
