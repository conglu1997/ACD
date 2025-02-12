class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "task_type": "generate",
                "constraints": "Generate a valid Sudoku puzzle with a unique solution. The puzzle should have at least 25 pre-filled numbers."
            },
            "2": {
                "task_type": "solve",
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
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task_type'] == 'generate':
            return f"""Generate a valid Sudoku puzzle with a unique solution based on the following constraints:

Constraints: {t['constraints']}

Your submission should be a 9x9 grid in plain text format, with each row on a new line and numbers separated by spaces. Use 0 to represent empty cells. Ensure the puzzle has at least 25 pre-filled numbers and exactly one solution. Submit your response as a plain text string in the format:

1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9
...
1 2 3 4 5 6 7 8 9"""
        else:
            return f"""Solve the given Sudoku puzzle. Ensure that your solution is valid according to Sudoku rules.

Puzzle:
{TaskFamily.format_puzzle(t['puzzle'])}

Submit your solution as a 9x9 grid in plain text format, with each row on a new line and numbers separated by spaces. Ensure that your solution is a valid Sudoku grid and follows all Sudoku rules. Submit your response as a plain text string in the format:

1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9
...
1 2 3 4 5 6 7 8 9"""

    @staticmethod
    def format_puzzle(puzzle: list[list[int]]) -> str:
        return '\n'.join(' '.join(map(str, row)) for row in puzzle)

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['task_type'] == 'generate':
            criteria = ["The puzzle should have exactly one solution.", "The puzzle should have at least 25 pre-filled numbers.", "The submission should be in the correct format."]
        else:
            criteria = ["The solution should be a valid Sudoku grid.", "The solution should follow all Sudoku rules.", "The submission should be in the correct format."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
