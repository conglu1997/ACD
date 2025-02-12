class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"game": "Chess", "situation": "You are playing as White and it is your turn to move. The current board setup is provided below. Devise a strategy to win the game in the next five moves.\n\n[Board Setup]\n8 r n b q k b n r\n7 p p p p p p p p\n6 8\n5 8\n4 8\n3 8\n2 P P P P P P P P\n1 R N B Q K B N R\n  a b c d e f g h"},
            "2": {"game": "Poker", "situation": "You are playing Texas Hold'em and you have the following hand: Ace of Spades, King of Hearts. The community cards are: 10 of Hearts, Jack of Hearts, Queen of Hearts, 2 of Clubs, 7 of Diamonds. Devise a strategy for the next betting round to maximize your chances of winning."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to devise a winning strategy for the following game scenario. Explain your reasoning behind each move or decision clearly and effectively. Here is the game situation:\n\n{t['game']}\n\n{t['situation']}\n\nSubmit your solution in plain text format. Your response should include:\n1. Restatement of the game and situation.\n2. Detailed strategy to win the game, including specific moves or decisions.\n3. Explanation of why this strategy should be effective."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The strategy should be clear and logically ordered.", "The moves or decisions should be feasible and effective.", "The explanation should be concise and accurate.", "The strategy should consider multiple potential outcomes."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
