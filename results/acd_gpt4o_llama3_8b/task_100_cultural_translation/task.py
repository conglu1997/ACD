class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"source_language": "English", "target_language": "Japanese", "content": "The early bird catches the worm, but the second mouse gets the cheese. This proverb emphasizes the timing and strategy in achieving success."},
            "2": {"source_language": "English", "target_language": "Spanish", "content": "A picture is worth a thousand words, but actions speak louder than words. This highlights the importance of actions over mere words."},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        source_language = t["source_language"]
        target_language = t["target_language"]
        content = t["content"]
        return f"""Translate the following passage from {source_language} to {target_language}, ensuring that the translation is culturally appropriate and conveys the same meaning in the context of the target language's culture. The passage to translate is: '{content}'.\n
Submit your translation as a plain text string in the following format: \nTranslation: [your translated text]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The translation should be accurate and culturally appropriate.", 
            "The meaning of the original passage should be preserved in the translation.", 
            "The translation should reflect cultural nuances of the target language."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
