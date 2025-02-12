class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"board": "r4rk1/pp2ppbp/2np1np1/q1p5/2P5/2NP1NP1/PP2PPBP/R1BQ1RK1 w - - 0 1", "solution": "Nxe5 dxe5 Bxc6"},
            "2": {"board": "r1bqkbnr/pppppppp/n7/8/3P4/8/PPP1PPPP/RNBQKBNR b KQkq - 0 1", "solution": "Nc6 d4 d5 exd5"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to solve the following chess puzzle. The board state is represented using Forsyth-Edwards Notation (FEN). Please provide the sequence of moves that lead to checkmate or a significant advantage for the player to move. Here is the board state:

{t["board"]}

Provide your response in standard algebraic notation, with each move separated by a space. Ensure the moves are valid according to standard chess rules. If no immediate checkmate is possible, aim to gain a significant material or positional advantage. The solution should be optimal and lead to the desired outcome efficiently."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should correctly solve the chess puzzle.",
            "The sequence of moves should be valid and lead to checkmate or a significant advantage.",
            "Each move should be in standard algebraic notation and separated by a space.",
            "The moves should align with the provided solutions.",
            "The solution should be optimal and lead to the desired outcome efficiently."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
