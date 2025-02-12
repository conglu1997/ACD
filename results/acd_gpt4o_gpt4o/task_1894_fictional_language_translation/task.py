class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"source_language": "English", "target_language": "Klingon", "text": "To boldly go where no one has gone before."},
            "2": {"source_language": "Elvish (Sindarin)", "target_language": "English", "text": "Elrond Peredhel"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Your task is to translate the following text from {t['source_language']} to {t['target_language']}:\n\n{t['text']}\n\nEnsure that your translation is accurate and maintains the semantic meaning of the original text. Provide your translation in plain text format."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The translation should be accurate.",
            "The translation should maintain the semantic meaning of the original text.",
            "The translation should be contextually appropriate."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0