class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"text": "To be, or not to be, that is the question: Whether 'tis nobler in the mind to suffer the slings and arrows of outrageous fortune, or to take arms against a sea of troubles and by opposing end them.", "target_language": "Middle English"},
            "2": {"text": "Whan that Aprille with his shoures soote The droghte of March hath perced to the roote, And bathed every veyne in swich licour Of which vertu engendred is the flour;", "target_language": "Modern English"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        text = t["text"]
        target_language = t["target_language"]
        return f"""Translate the following text to {target_language}:

Text: {text}

Ensure your translation retains the original meaning and adheres to the linguistic norms of the target language. Submit your translation as a plain text string in the following format:

Translation: [Your translation here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The translation should retain the original meaning.", "The translation should adhere to the linguistic norms of the target language."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
