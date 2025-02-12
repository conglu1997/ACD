class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "text": "We are pleased to inform you that your application has been accepted. Congratulations on this achievement! We look forward to seeing your contributions.",
                "style": "formal",
                "tone": "enthusiastic"
            },
            "2": {
                "text": "The project deadline has been moved up to next week. Make sure to prioritize it accordingly and inform your team about the changes.",
                "style": "informal",
                "tone": "urgent"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Transform the following text to match the specified writing style and tone:\n\nOriginal Text: {t['text']}\n\nStyle: {t['style']}\nTone: {t['tone']}\n\nSubmit your transformed text as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The transformed text must match the specified writing style.",
            "The transformed text must reflect the specified tone.",
            "The transformed text must remain coherent and appropriate for the context.",
            "The transformed text must be a nuanced adaptation, not a simple rephrasing."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
