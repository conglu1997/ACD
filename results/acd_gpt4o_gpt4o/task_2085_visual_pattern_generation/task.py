class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"constraints": "Generate a 5x5 grid pattern where no two adjacent cells (horizontally, vertically, or diagonally) have the same symbol. Use the symbols 'X' and 'O'."},
            "2": {"constraints": "Generate an 8x8 checkerboard pattern using the symbols 'A' and 'B'. The pattern should alternate symbols in both rows and columns."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a visual pattern based on the following constraints:

{t["constraints"]}

Provide your pattern in plain text format, using spaces to separate the symbols in each row. Ensure each row is on a new line. Ensure that your pattern adheres to the specified constraints. Example format for a 3x3 grid:

X O X
O X O
X O X

Make sure your pattern is visually coherent and follows the rules given in the constraints."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The pattern must adhere to the given constraints.",
            "The pattern must be visually coherent and correctly formatted.",
            "The pattern must use the specified symbols.",
            "No two adjacent cells should have the same symbol (for Task 1).",
            "The pattern should alternate symbols in both rows and columns (for Task 2)."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
