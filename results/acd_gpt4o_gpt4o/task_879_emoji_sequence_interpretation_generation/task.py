class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "birthday celebration", "interpretation": False},
            "2": {"emoji_sequence": "🎉🎂🎁🎈😊", "interpretation": True}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['interpretation']:
            return f"""Your task is to interpret the following sequence of emojis:

Emoji Sequence: {t['emoji_sequence']}

Provide a clear, step-by-step explanation of the meaning conveyed by the emojis. Ensure your explanation is detailed and easy to understand. Your response should be between 50 and 100 words and provided in plain text format."""
        else:
            return f"""Your task is to generate a sequence of emojis based on the following theme:

Theme: {t['theme']}

Your emoji sequence should be clear, detailed, and creatively embody the theme. The sequence should be between 4 and 8 emojis long. Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['interpretation']:
            criteria = ["The explanation should accurately interpret the given emoji sequence.", "The explanation should be detailed and easy to understand.", "The response should be between 50 and 100 words."]
        else:
            criteria = ["The generated emoji sequence should be clear and detailed.", "The emoji sequence should creatively embody the given theme.", "The sequence should be between 4 and 8 emojis long."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
