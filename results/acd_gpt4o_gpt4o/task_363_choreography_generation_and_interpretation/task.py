class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "joyful celebration", "interpretation": False},
            "2": {"instructions": "Step forward with the right foot, raise both arms above the head, spin 360 degrees clockwise, jump with both feet together.", "interpretation": True}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['interpretation']:
            return f"""Your task is to interpret the following set of choreographic instructions:

Instructions: {t['instructions']}

Provide a clear, step-by-step explanation of the movements described in the instructions. Ensure your explanation is detailed and easy to understand. Provide your response in plain text format."""
        else:
            return f"""Your task is to generate a series of choreographic instructions based on the following theme:

Theme: {t['theme']}

Your instructions should be clear, detailed, and easy to follow. Aim to create a sequence of movements that embodies the theme. The sequence should be between 4 and 8 steps long and should be at least 50 words. Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['interpretation']:
            criteria = ["The explanation should accurately interpret the given choreographic instructions.", "The explanation should be detailed and easy to understand."]
        else:
            criteria = ["The generated instructions should be clear and detailed.", "The instructions should embody the given theme.", "The sequence should be between 4 and 8 steps long.", "The instructions should be at least 50 words."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
