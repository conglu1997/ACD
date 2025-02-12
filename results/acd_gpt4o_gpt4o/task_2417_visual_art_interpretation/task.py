class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task_type": "interpret", "image_description": "A surreal painting by Salvador Dalí depicting melting clocks draped over various objects in a dream-like landscape.", "question": "Describe the possible themes and emotions conveyed by this artwork."},
            "2": {"task_type": "narrative", "image_description": "A serene landscape painting by Claude Monet featuring a water lily pond with a Japanese bridge.", "question": "Write a short story inspired by this painting."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task_type"] == "interpret":
            instructions = f"""Your task is to interpret the given visual art piece and describe the possible themes and emotions it conveys. Use the description of the artwork to inform your interpretation.

Artwork Description: {t['image_description']}

Question: {t['question']}

Provide your response in plain text format. Ensure your interpretation is thoughtful, detailed, and captures the essence of the artwork. Your response should be structured as follows:

Response: The artwork conveys a sense of..."""
        else:
            instructions = f"""Your task is to write a short story inspired by the given visual art piece. Use the description of the artwork to inform your narrative.

Artwork Description: {t['image_description']}

Question: {t['question']}

Ensure that your story is creative, coherent, and captures the essence of the artwork. Provide your response in plain text format. Your story should be structured as follows:

Story: Once upon a time..."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["task_type"] == "interpret":
            criteria = ["The response should thoughtfully describe the themes and emotions conveyed by the artwork.", "The interpretation should be detailed and capture the essence of the artwork."]
        else:
            criteria = ["The story should be creative and coherent.", "The narrative should capture the essence of the artwork."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
