class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"source_lang": "English", "target_lang": "Spanish", "text": "Once upon a time, in a land far away, a young prince embarked on a journey to find a magical artifact."},
            "2": {"language": "French", "theme": "perseverance"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "text" in t:
            source_lang = t["source_lang"]
            target_lang = t["target_lang"]
            text = t["text"]
            return f"""Translate the following text from {source_lang} to {target_lang}:

Text: {text}

Ensure the translation is accurate and culturally appropriate. Submit your translation as a plain text string."""
        else:
            language = t["language"]
            theme = t["theme"]
            return f"""Generate a culturally appropriate proverb or idiom in {language} based on the theme of '{theme}'.

Ensure the proverb or idiom reflects the theme accurately and is commonly understood in the target culture. Submit your response as a plain text string.

Example: For the theme of 'perseverance' in English, an appropriate proverb might be: 'When the going gets tough, the tough get going.'"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "text" in t:
            criteria = ["The translation should be accurate.", "The translation should be culturally appropriate."]
        else:
            criteria = ["The proverb or idiom should be culturally appropriate.", "The proverb or idiom should accurately reflect the theme."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
