class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"game": "Chess", "scenario": "You are playing as white. Provide a strategy for the opening moves, focusing on control of the center and piece development. Your opponent is known to favor the Sicilian Defense. You should aim to reach a position that maximizes your control of the board by move 10."},
            "2": {"game": "Poker", "scenario": "You are playing Texas Hold'em and are dealt a pair of Jacks. Provide a strategy for the pre-flop, flop, turn, and river stages, considering you are in a late position with aggressive players at the table. Your goal is to maximize your winnings while minimizing risks."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a strategy for the given game scenario:

Game: {t["game"]}
Scenario: {t["scenario"]}

Your response should include:
1. A detailed explanation of the strategy.
2. The reasoning behind each strategic decision, addressing potential moves of your opponent and how you would respond.

Submit your response as a plain text string in the following format:

Strategy: [Your detailed strategy]
Reasoning: [Your reasoning for each decision, addressing potential opponent moves]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include a detailed strategy for the given game scenario.",
            "The response should include reasoning for each strategic decision, addressing potential opponent moves.",
            "The strategy should aim to reach the specified goal in the scenario (e.g., control of the board by move 10 in chess)."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
