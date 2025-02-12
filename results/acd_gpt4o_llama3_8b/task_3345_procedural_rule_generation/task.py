class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "game_theme": "Space Exploration",
                "components": {
                    "spaceships": "Used by players to explore the galaxy.",
                    "planets": "Locations to explore and gather resources.",
                    "resources": "Materials collected from planets.",
                    "missions": "Tasks that players complete for points."
                },
                "objective": "Explore the galaxy, gather resources, and complete missions to earn points. The player with the most points at the end of the game wins."
            },
            "2": {
                "game_theme": "Medieval Kingdom",
                "components": {
                    "castles": "Structures that players build and upgrade.",
                    "knights": "Units sent on quests to gain treasures.",
                    "treasures": "Valuable items collected from quests.",
                    "quests": "Missions that knights undertake for treasures."
                },
                "objective": "Build your kingdom, send out knights on quests, and collect treasures. The player with the most powerful kingdom at the end of the game wins."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        components = '\n'.join([f"{k}: {v}" for k, v in t['components'].items()])
        return f"""Generate a complete set of procedural instructions for a board game with the following theme and components:

Theme: {t['game_theme']}
Components:
{components}

Objective: {t['objective']}

Your instructions should include the following sections:
1. Game Setup: Describe how to set up the game, including the initial arrangement of components and any preliminary steps required.
2. Game Mechanics: Explain the rules and how the game is played, detailing the actions players can take, the sequence of play, and how components are used.
3. Winning Conditions: Specify how a player wins the game, including any end-game triggers and how to determine the winner.

Example response format:
Game Setup: [Your description here]
Game Mechanics: [Your description here]
Winning Conditions: [Your description here]

Ensure that your instructions are clear, coherent, and logically consistent. The instructions should be detailed enough for someone to understand and play the game without additional information. Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The game setup instructions should be clear, complete, and include the initial arrangement of components.",
            "The game mechanics should be logically consistent, detailed, and cover all player actions and sequence of play.",
            "The winning conditions should be clearly defined, achievable, and include end-game triggers.",
            "The overall instructions should be coherent, follow the given theme, and be detailed enough for someone to understand and play the game without additional information."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
