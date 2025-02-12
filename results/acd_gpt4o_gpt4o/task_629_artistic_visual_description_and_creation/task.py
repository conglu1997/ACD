class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "A bustling cityscape at sunset", "description": False},
            "2": {"art_description": "A serene landscape with a flowing river, towering mountains in the background, and a small wooden cabin by the riverbank. The sky is painted in hues of orange and pink as the sun sets behind the mountains.", "description": True}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['description']:
            return f"""Your task is to describe the following piece of visual art in detail:

Description: {t['art_description']}

Provide a clear, step-by-step explanation of the visual elements described. Ensure your explanation is detailed and easy to understand. Provide your response in plain text format."""
        else:
            return f"""Your task is to generate a detailed description of an imagined artwork based on the following theme:

Theme: {t['theme']}

Your description should be clear, detailed, and imaginative. Aim to create a vivid image of the artwork that embodies the theme. Ensure your description is at least 100 words. Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['description']:
            criteria = ["The explanation should accurately describe the given visual elements.", "The explanation should be detailed and easy to understand."]
        else:
            criteria = ["The generated description should be clear and detailed.", "The description should embody the given theme.", "The description should be at least 100 words."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
