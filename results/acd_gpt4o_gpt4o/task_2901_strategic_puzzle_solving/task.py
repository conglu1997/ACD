class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"puzzle": "In a 2x2 grid, you need to move a single 'X' from the bottom-left corner to the top-right corner. You can move up, down, left, or right, but you cannot move 'X' into the same cell twice. What's the sequence of moves?"},
            "2": {"puzzle": "In a 3x3 grid, move a single 'O' from the top-left corner to the bottom-right corner. You can only move diagonally and cannot pass through the same cell twice. What's the sequence of moves?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        puzzle = t["puzzle"]
        instructions = f"""Your task is to solve the following puzzle by planning a sequence of moves. Ensure that your solution is logically sound and adheres to the rules provided in the puzzle.

Puzzle: {puzzle}

Provide your solution in the following format:
Move Sequence: [List of moves in the format (from_row, from_col) -> (to_row, to_col)]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The solution should be logically sound.",
            "The sequence of moves should adhere to the rules of the puzzle."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
