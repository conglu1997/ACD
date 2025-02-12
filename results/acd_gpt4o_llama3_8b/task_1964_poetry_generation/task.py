class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "theme": "nature",
                "emotion": "tranquility",
                "additional_criteria": ["The poem should evoke a sense of peace and serenity.", "The poem should have a natural flow and rhythm."]
            },
            "2": {
                "theme": "love",
                "emotion": "longing",
                "additional_criteria": ["The poem should evoke a sense of yearning and desire.", "The poem should be expressive and vivid."]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a poem based on the following theme and emotion:

Theme: {t['theme']}
Emotion: {t['emotion']}

Your poem should be coherent, meaningful, and emotionally impactful. Ensure that it has a natural flow and rhythm. Submit your response as a plain text string in the following format:

Poem:
[Your poem]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = t.get('additional_criteria', [])
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
