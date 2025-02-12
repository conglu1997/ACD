class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "Create a pattern consisting of alternating squares and circles in a 5x5 grid. Each row should alternate starting with a square in the first row and a circle in the second row."},
            "2": {"description": "Generate a pattern where triangles point upwards in the first row, downwards in the second row, and continue alternating in a 4x4 grid."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a visual pattern based on the following textual description. Ensure that your pattern strictly follows the described format and is visually clear. Provide your visual pattern using any notation or characters that effectively represent the described shapes (e.g., using 'O' for circles, '[]' for squares, and '^' for upward triangles and 'v' for downward triangles).

Description: {t['description']}

Example Format:
For a 3x3 grid with alternating 'X' and 'O':
X O X
O X O
X O X

Ensure that the characters are aligned in a grid format and clearly distinguishable. Each row should start on a new line.

Example Detailed:
For a 5x5 grid with alternating '[]' and 'O' starting with '[]':
[] O [] O []
O [] O [] O
[] O [] O []
O [] O [] O
[] O [] O []"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The pattern should match the given description.",
            "The pattern should be visually clear and correctly formatted.",
            "The characters should be aligned in a grid format and clearly distinguishable.",
            "Each row should start on a new line."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
