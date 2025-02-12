class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "board_state": "8/8/8/8/8/8/6k1/5R1K w - - 0 1",
                "goal": "Checkmate in 2 moves"
            },
            "2": {
                "board_state": "8/8/8/8/8/5k2/5R2/7K w - - 0 1",
                "goal": "Checkmate in 3 moves"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to formulate a strategy to achieve the given goal in the chess endgame scenario. The board state is provided in FEN format.

Goal: {t['goal']}

Board State: {t['board_state']}

You are playing as white. Provide a step-by-step plan detailing your moves in plain text format. Ensure your plan adheres to the rules of chess and achieves the specified goal within the given number of moves. Your response should include:
1. Each move in standard chess notation.
2. A brief explanation of your strategy and rationale for each move.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The moves should be valid according to the rules of chess.",
            "The moves should achieve the specified goal within the given number of moves.",
            "The explanation should demonstrate a clear strategy and rationale for each move.",
            "The response should use standard chess notation for each move."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
