class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"puzzle_description": "A 3x3 grid where numbers 1 to 9 must be placed such that each row, column, and diagonal sums to 15.", "constraints": "Each number must be unique and used exactly once."},
            "2": {"puzzle_description": "A 4x4 grid where numbers 1 to 16 must be arranged so that adjacent numbers are not consecutive.", "constraints": "Each number must be unique and used exactly once."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the following visual-spatial puzzle based on the given description and constraints:

Puzzle Description: {t['puzzle_description']}

Constraints: {t['constraints']}

Submit your solution as a plain text string in the form of a comma-separated list of numbers representing the grid from top-left to bottom-right. For example, a 3x3 grid solution could look like: '2,7,6,9,5,1,4,3,8'. A 4x4 grid solution could look like: '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16'. Ensure that your solution adheres to the constraints and correctly solves the puzzle.

Example:
For a 3x3 grid: '2,7,6,9,5,1,4,3,8'
For a 4x4 grid: '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16'"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The solution must meet the constraints specified in the puzzle description.",
            "The numbers must be arranged correctly to solve the puzzle.",
            "The solution must be presented in the specified format."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
