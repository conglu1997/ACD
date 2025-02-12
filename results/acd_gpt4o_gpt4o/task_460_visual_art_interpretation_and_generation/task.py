class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task_type": "interpret", "art_description": "A surreal painting depicting a melting clock over a desert landscape."},
            "2": {"task_type": "generate", "theme": "tranquility in nature"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task_type'] == 'interpret':
            return f"""Your task is to interpret the following art description and provide a detailed analysis of its meaning and elements.

Art Description: {t['art_description']}

Instructions:
1. Provide a detailed interpretation of the given art description.
2. Explain the possible symbolism, themes, and emotions conveyed by the art.
3. Ensure that your interpretation is coherent and insightful.

Your response should be in the following format:
Interpretation: [Your interpretation]"""
        elif t['task_type'] == 'generate':
            return f"""Your task is to generate a detailed description for a new piece of art based on the given theme.

Theme: {t['theme']}

Instructions:
1. Create a vivid and imaginative description of a new art piece that aligns with the given theme.
2. Ensure that your description is original and creative.
3. Provide enough detail so that someone could visualize the art based on your words.

Your response should be in the following format:
Art Description: [Your art description]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['task_type'] == 'interpret':
            criteria = ["The interpretation should be coherent and insightful.", "The interpretation should explain the possible symbolism, themes, and emotions conveyed by the art."]
        elif t['task_type'] == 'generate':
            criteria = ["The art description should align with the given theme.", "The art description should be original and creative.", "The description should provide enough detail to visualize the art."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
