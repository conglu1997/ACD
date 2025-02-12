class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"source_language": "English", "target_language": "French", "paragraph": "In the heart of the bustling city, there stood an ancient library. Its shelves were lined with books that told stories of old, each page whispering secrets of the past. People from all walks of life would come to find solace in its quiet corners, lost in the world of words."},
            "2": {"source_language": "English", "target_language": "Japanese", "paragraph": "The advancements in renewable energy technologies have sparked a revolution. Solar panels, wind turbines, and electric vehicles are becoming increasingly common, paving the way for a sustainable future. Governments and corporations alike are investing heavily in green energy initiatives."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Translate the following paragraph from {t['source_language']} to {t['target_language']}. Ensure that the translation maintains the original meaning, tone, context, and idiomatic expressions. Paragraph: '{t['paragraph']}'. Submit your translation as a plain text string.\n\nExample format: \nTranslation: [Your translated text here]"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The translation should accurately convey the original meaning.",
            "The translation should maintain the tone of the original paragraph.",
            "The translation should preserve the context.",
            "The translation should include appropriate idiomatic expressions where necessary."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
