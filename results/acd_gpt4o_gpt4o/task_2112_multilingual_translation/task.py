class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"source_language": "English", "target_language": "Spanish", "text": "The quick brown fox jumps over the lazy dog. This sentence contains every letter of the English alphabet."},
            "2": {"source_language": "French", "target_language": "German", "text": "Les enfants jouent dans le parc sous le ciel bleu et ensoleillé. C'est une belle journée."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to translate the following text from {t['source_language']} to {t['target_language']}. Ensure that the translation preserves the original meaning, context, and nuances of the text.

Source Text:
{t['text']}

Provide your translation in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The translation should accurately reflect the original meaning, context, and nuances.",
            "The translation should be grammatically correct in the target language.",
            "Idiomatic expressions should be appropriately translated.",
            "The translation should maintain the same tone and style as the source text."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
