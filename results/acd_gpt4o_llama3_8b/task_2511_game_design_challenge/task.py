class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "theme": "space exploration",
                "constraints": "The game must involve resource management and have at least three distinct types of spacecraft."
            },
            "2": {
                "theme": "medieval fantasy",
                "constraints": "The game must include character classes, a quest system, and a crafting mechanic."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a unique game based on the following thematic and functional constraints:

Theme: {t['theme']}
Constraints: {t['constraints']}

Ensure your game design includes:
1. A brief overview of the game's setting and storyline.
2. Key gameplay mechanics and how they relate to the theme and constraints.
3. Examples of in-game items, characters, or scenarios that illustrate your design.
4. Any unique features or innovations that set your game apart.

Your submission should be at least 500 words long to ensure sufficient detail.

Submit your game design as a plain text string in the following format:

Overview: [Your brief overview]
Gameplay Mechanics: [Detailed description of key mechanics]
Examples: [Examples of in-game items, characters, or scenarios]
Unique Features: [Any unique features or innovations]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The game design should be coherent and engaging.",
            "The game design should adhere to the given thematic and functional constraints.",
            "The game design should include a brief overview, key gameplay mechanics, examples, and unique features.",
            "The submission should be at least 500 words long."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
