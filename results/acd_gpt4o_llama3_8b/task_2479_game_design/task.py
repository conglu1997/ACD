class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "Space Exploration", "constraints": "The game should be an open-world adventure game with resource management elements. The player should be able to explore different planets, gather resources, and upgrade their spaceship."},
            "2": {"theme": "Medieval Fantasy", "constraints": "The game should be a role-playing game (RPG) with turn-based combat. The player should be able to choose from different character classes, embark on quests, and engage in tactical battles."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a game concept based on the following theme and constraints:

Theme: {t['theme']}
Constraints: {t['constraints']}

Ensure that the game concept is coherent, engaging, and adheres to the specified constraints. The concept should include the following sections:
1. Brief Overview: A summary of the game's setting and story.
2. Core Gameplay Mechanics: The main gameplay elements and how they function.
3. Main Objectives: The primary goals and objectives of the game.
4. Unique Features: Any distinctive features that set the game apart from others.

Submit your game concept as a plain text string with the sections clearly labeled."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The game concept should align with the provided theme and constraints.", "The concept should include a brief overview, core gameplay mechanics, main objectives, and unique features, with sections clearly labeled."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
