class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "Space Exploration", "player_count": 2, "age_range": "8+"},
            "2": {"theme": "Medieval Kingdoms", "player_count": 4, "age_range": "12+"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to design a simple board game based on the following details:

Theme: {t['theme']}
Player Count: {t['player_count']}
Age Range: {t['age_range']}

Please include the following elements in your design:

1. Objective: What is the goal of the game?
2. Components: List and describe the components required to play the game (e.g., board, cards, tokens).
3. Setup: How do players set up the game before starting?
4. Rules: Describe the rules of the game, including how players take turns, how they can win, and any special actions or conditions.
5. Example Turn: Provide an example of a single turn to illustrate how the game is played. For example, describe the actions a player might take during their turn, the possible outcomes, and how the game state changes.

Ensure that your game is suitable for the specified player count and age range, and that the rules are clearly explained and easy to follow."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The game design should include all required elements (objective, components, setup, rules, example turn).",
                    "The game should be suitable for the specified player count and age range.",
                    "The rules should be clearly explained and easy to follow.",
                    "The game should be engaging and thematic.",
                    "The example turn should clearly illustrate the gameplay."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
