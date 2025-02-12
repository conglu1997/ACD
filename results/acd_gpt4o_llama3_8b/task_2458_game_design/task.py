class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "Fantasy Adventure", "constraints": "The game should include a quest system, character customization, and a multiplayer mode. It should be suitable for players aged 12 and above."},
            "2": {"theme": "Sci-Fi Survival", "constraints": "The game should focus on resource management, base building, and have a single-player campaign. It should include elements of exploration and combat."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a new game based on the following theme and constraints:

Theme: {t['theme']}
Constraints: {t['constraints']}

Ensure that your game design is creative, engaging, and meets all the specified constraints. Describe the key features, gameplay mechanics, and narrative elements of the game. Submit your design as a plain text string in the following format:

- Game Title: [Your game title]
- Key Features: [Describe the key features in detail, ensuring all constraints are met]
- Gameplay Mechanics: [Explain the gameplay mechanics and how they fit the theme and constraints]
- Narrative Elements: [Describe the narrative elements and story arcs]

Example:
- Game Title: Quest of the Elders
- Key Features: Quest system, character customization, multiplayer mode suitable for players aged 12 and above
- Gameplay Mechanics: Players embark on quests to gain experience and loot, customize their characters, and team up with others in a multiplayer mode
- Narrative Elements: The story follows a group of young adventurers on a journey to save their realm from an ancient evil"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The game design should meet all the specified constraints.",
            "The game design should be creative and engaging.",
            "The submission should follow the provided format.",
            "The key features should be detailed and relevant.",
            "The gameplay mechanics should clearly explain how they fit the theme and constraints.",
            "The narrative elements should be well-described and coherent.",
            "All constraints must be explicitly addressed in the submission."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
