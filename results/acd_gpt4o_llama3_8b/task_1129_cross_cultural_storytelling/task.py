class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "culture1": "Japanese",
                "culture2": "Nigerian",
                "theme": "Friendship",
                "answer": "N/A"
            },
            "2": {
                "culture1": "Italian",
                "culture2": "Indian",
                "theme": "Adventure",
                "answer": "N/A"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a story that incorporates cultural elements from the two specified cultures. Ensure the story captures the essence of both cultures and is coherent and engaging.

Cultures: {t['culture1']} and {t['culture2']}
Theme: {t['theme']}

Your story should include:
1. Characters that represent each culture.
2. Descriptions of cultural practices or traditions.
3. A plot that weaves together elements from both cultures.

Submit your story as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The story should be coherent and engaging.",
            "The story should incorporate cultural elements from both specified cultures.",
            "The story should follow the given theme."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
