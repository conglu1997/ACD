class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "Create a rule-based system for a fictional card game. The card game involves four suits (Hearts, Diamonds, Clubs, Spades) and each suit has cards numbered 1-10. The game should have at least 3 distinct rules that players must follow to win.",
                "description": "Design a card game"
            },
            "2": {
                "scenario": "Interpret the following rule-based system and explain how a player can win the game. The game involves a grid with cells that can be either black or white. The rules are: 1) A player wins if they connect four black cells in a row horizontally, vertically, or diagonally. 2) A cell can be flipped from white to black if at least two of its neighbors are black. 3) A cell can be flipped from black to white if all of its neighbors are white.",
                "description": "Interpret a grid-based game"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to {t['description']} based on the following scenario.

Scenario: {t['scenario']}

Ensure your response adheres to the scenario description and provides a clear, detailed explanation or design of the rule-based system. Provide your response in plain text format.

Response Format:
1. For designing a card game: List the rules and explain how a player can win the game.
2. For interpreting a grid-based game: Describe the steps a player should follow to win the game based on the given rules."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['description'] == 'Design a card game':
            criteria = ["The response should include at least 3 distinct rules.",
                       "The rules should be clear and logically consistent.",
                       "The rules should define how a player wins the game.",
                       "The response should be original and creative."]
        else:
            criteria = ["The explanation should accurately interpret the given rules.",
                       "The explanation should describe a valid winning strategy.",
                       "The response should be clear and logically consistent."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
