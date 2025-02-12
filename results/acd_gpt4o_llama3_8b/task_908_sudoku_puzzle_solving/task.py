class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {
                'puzzle': '53--7----\n6--195---\n-98----6-\n8---6---3\n4--8-3--1\n7---2---6\n-6----28-\n---419--5\n----8--79'
            },
            '2': {
                'puzzle': '-5-3--7--\n6---195--\n-98----6-\n8---6---3\n4--8-3--1\n7---2---6\n-6----28-\n---419--5\n----8--79'
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the following Sudoku puzzle by filling in the missing numbers. Ensure that each row, column, and 3x3 subgrid contains all digits from 1 to 9 without repetition. Submit your solution as a plain text string with each row on a new line, and use '-' to represent empty cells.

Puzzle:
{t['puzzle']}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = ["The solution should correctly fill in the missing numbers.", "Each row, column, and 3x3 subgrid must contain all digits from 1 to 9 without repetition."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
