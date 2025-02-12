class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "original_text": "The sun set over the horizon, painting the sky in hues of orange and pink.",
                "style": "Shakespearean"
            },
            "2": {
                "original_text": "A young child played joyfully in the park, laughing and chasing butterflies.",
                "style": "Gothic"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Transform the following piece of text into the specified artistic style. Ensure that the transformed text retains the original meaning but is written in a manner that reflects the given style. Here are the details:

Original Text: {t['original_text']}
Style: {t['style']}

Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The transformed text should retain the original meaning.",
            "The transformed text should reflect the specified artistic style."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
