class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "position": "8/8/8/8/8/8/6R1/K7 w - - 0 1",
                "expected_moves": ["Rg8#"]
            },
            "2": {
                "position": "8/8/8/8/8/5K2/4R3/8 w - - 0 1",
                "expected_moves": ["Re8#"]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        position = t["position"]
        return f"""Solve the following chess puzzle by providing the sequence of moves that leads to checkmate. The position is given in FEN notation: {position}

FEN (Forsyth-Edwards Notation) describes a particular board position. For example, 'r1bqkbnr/pppppppp/2n5/8/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq - 2 3' represents the starting position of a standard chess game with some moves played. The '/' separates ranks, lowercase letters represent black pieces, uppercase letters represent white pieces, and numbers represent empty squares.

Submit your solution as a plain text string with moves separated by commas. For example: 'e2e4, e7e5, Qh5, Nf6, Qxf7#'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        expected_moves = t["expected_moves"]
        criteria = [f"The sequence of moves should be: {', '.join(expected_moves)}", "The moves should be in the correct format."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0