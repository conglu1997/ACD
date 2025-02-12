class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"puzzle": "You have a 3x3 grid with numbers 1 to 8 and an empty space. The numbers are shuffled as follows: [1, 2, 3, 4, 5, ' ', 6, 7, 8]. Your task is to move the numbers around to arrange them in ascending order with the empty space at the end. Provide the sequence of moves in plain text format, where each move is represented by the number you move into the empty space."},
            "2": {"puzzle": "You have a 4x4 grid with numbers 1 to 15 and an empty space. The numbers are shuffled as follows: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, ' ', 14, 15]. Your task is to move the numbers around to arrange them in ascending order with the empty space at the end. Provide the sequence of moves in plain text format, where each move is represented by the number you move into the empty space."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to solve the given puzzle by deducing the correct sequence of moves to reach the solution. Here is the puzzle:

Puzzle: {t['puzzle']}

Move the numbers around to arrange them in ascending order with the empty space at the end. Provide the sequence of moves in plain text format, where each move is represented by the number you move into the empty space.

Example: If the initial configuration is [1, 2, 3, 4, 5, ' ', 6, 7, 8] and you move the number 6 into the empty space, then the number 7, your response should be: 6, 7."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The solution should correctly solve the puzzle by arranging the numbers in ascending order with the empty space at the end.", "The sequence of moves should be clear and logical."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
