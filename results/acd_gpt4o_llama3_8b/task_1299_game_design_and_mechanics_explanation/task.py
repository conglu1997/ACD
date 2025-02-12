class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"type": "board game", "theme": "space exploration"},
            "2": {"type": "card game", "theme": "medieval fantasy"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a simple {t['type']} with the theme '{t['theme']}'. Describe the game's mechanics, rules, and objectives in detail. Your description should include:
1. The objective of the game.
2. The rules of the game.
3. The mechanics of how the game is played.
4. Any special features or unique aspects of the game.

Ensure that the game is engaging, easy to understand, and fun to play. Creativity and originality will be highly valued. Submit your response as a plain text string in the following format:

Game Objective: [Your description of the game's objective]
Game Rules: [Detailed rules of the game]
Game Mechanics: [Description of how the game is played]
Special Features: [Any unique aspects of the game]

Example:
Game Objective: The objective of the game is to reach the center of the galaxy by collecting resources and avoiding obstacles.
Game Rules: Each player takes turns rolling a dice to move their spaceship forward. Players can collect resources by landing on resource planets. Obstacles like black holes can send players back.
Game Mechanics: Players roll a dice to move. Resource planets give players resource cards that can be used to move extra spaces or avoid obstacles. Black holes send players back to the start.
Special Features: The game includes special event cards that can change the course of the game, such as wormholes that teleport players to different parts of the board."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The game should have a clear and engaging objective.",
            "The rules should be detailed and easy to understand.",
            "The mechanics should explain how the game is played clearly.",
            "Any special features or unique aspects should be well-described.",
            "The response should follow the specified format.",
            "The game should demonstrate creativity and originality."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
