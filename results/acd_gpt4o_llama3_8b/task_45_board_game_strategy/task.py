class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"game": "tic_tac_toe", "board": [["X", "O", "X"], ["O", "", ""], ["", "X", "O"]]},
            "2": {"game": "chess", "board": "r1bqkbnr/pppp1ppp/2n5/4p3/4P3/2N5/PPPP1PPP/R1BQKBNR w KQkq - 2 4"},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        game = t["game"]
        board = t["board"]
        return f"""Generate a winning strategy for the following {game} scenario. Describe your strategy in detail, including the reasoning behind each move. Ensure your strategy is logical, adheres to the game rules, and aims to maximize your chances of winning. Here is the current board state:
{board}

Your strategy should include:
1. Your immediate next move.
2. Potential responses from your opponent.
3. Your follow-up moves based on possible opponent responses.

Submit your strategy as a plain text string in the following format:
Move X: [Description of move and reasoning]
Move Y: [Description of move and reasoning]
..."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The strategy should be logical and follow the rules of the game.",
            "The strategy should maximize the chances of winning.",
            "The strategy should include clear reasoning for each move.",
            "The strategy should consider potential opponent responses."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
