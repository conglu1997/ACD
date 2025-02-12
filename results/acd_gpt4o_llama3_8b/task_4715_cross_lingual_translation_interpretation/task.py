class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "text": "He spilled the beans about the surprise party, and now it's ruined.",
                "source_language": "English",
                "target_language": "French"
            },
            "2": {
                "text": "Il pleut des cordes ce soir, alors apportez un parapluie.",
                "source_language": "French",
                "target_language": "English"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Translate the given text from {t['source_language']} to {t['target_language']} and ensure that the translated text maintains the original meaning. Provide your translation as a plain text string.\n\nText: {t['text']}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The translation should be accurate and maintain the original meaning.",
            "The translation should be grammatically correct in the target language."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
