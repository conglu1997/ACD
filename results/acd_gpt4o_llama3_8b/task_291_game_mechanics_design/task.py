class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "theme": "A fantasy role-playing game set in a medieval world. Players can choose different character classes, explore dungeons, and battle mythical creatures.",
                "constraints": "The game should have a unique combat system that differentiates it from existing games."
            },
            "2": {
                "theme": "A sci-fi space exploration game where players can pilot spaceships, discover new planets, and interact with alien civilizations.",
                "constraints": "The game should include a resource management mechanic that is crucial for survival and progression."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design game mechanics for a hypothetical video game based on the following theme and constraints:

Theme: {t['theme']}

Constraints: {t['constraints']}

Ensure your design includes detailed descriptions of the core mechanics, how they work, and how they enhance the gameplay experience. Submit your response as a plain text string with the following sections:

1. Core Mechanics: [Describe the core mechanics in detail, including the unique aspects.]
2. Implementation: [Explain how these mechanics will be implemented in the game, including possible algorithms or systems required.]
3. Gameplay Enhancement: [Discuss how these mechanics enhance the gameplay experience, providing specific examples of player interactions.]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = ["The design should include detailed descriptions of the core mechanics, their implementation, and how they enhance the gameplay experience.", "The submission should address the unique aspects specified in the constraints."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
