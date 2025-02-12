class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"game_state": "Player A has a knight on e5 and a pawn on d4. Player B has a bishop on f6. It's Player A's turn. What is the best move for Player A?"},
            "2": {"game_state": "Player A has a rook on a1 and a queen on h5. Player B has a king on e8 and a pawn on e7. It's Player A's turn. What is the best move for Player A?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the current game state and determine the best move for the player whose turn it is. Consider the rules of chess and the positions of each piece on the board. Provide your move in the following format using standard chess notation:

Move: [Your move in standard notation, e.g., Nf3, Rxh1]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The move should follow the rules of chess.", "The move should be the best possible given the game state."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
