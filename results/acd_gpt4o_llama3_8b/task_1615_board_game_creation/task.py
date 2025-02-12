class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "constraints": "Design a board game for 2-4 players that can be played within 30 minutes. The game should involve cards, dice, and a board with various spaces. The objective of the game should be to collect the most points by the end of the game. Include the rules for setting up the game, playing the game, and ending the game. Also, describe the components needed.",
                "requirements": "The game should be balanced, engaging, and suitable for players aged 10 and above."
            },
            "2": {
                "constraints": "Design a cooperative board game for 3-5 players that can be played within 45 minutes. The game should involve tokens, a game board with a map, and various event cards. The objective of the game should be to complete a series of missions before a timer runs out. Include the rules for setting up the game, playing the game, and ending the game. Also, describe the components needed.",
                "requirements": "The game should encourage teamwork, be challenging, and suitable for players aged 12 and above."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a board game based on the following constraints:

Constraints: {t['constraints']}

Requirements: {t['requirements']}

Ensure that your game design includes:
1. A detailed description of the game components.
2. Clear rules for setting up, playing, and ending the game.
3. Objectives and win conditions.
4. Any additional information to help understand the game mechanics.

Submit your game design as a plain text document. Your submission should be well-structured and coherent, providing enough detail for someone to understand how to play the game."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The game design should include all specified components.",
            "The rules should be clear and coherent.",
            "The game should adhere to the given constraints and requirements."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
