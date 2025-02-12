class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task_type": "create", "theme": "harvest celebration"},
            "2": {"task_type": "interpret", "ritual_description": "During the Festival of Lights, the community gathers at the central square. They light lanterns and release them into the sky while singing traditional songs. This ritual symbolizes the triumph of light over darkness and the renewal of hope."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task_type'] == 'create':
            return f"""Your task is to create a detailed description of a fictional cultural ritual based on the given theme.

Theme: {t['theme']}

Instructions:
1. Create a vivid and imaginative description of a cultural ritual that aligns with the given theme.
2. Ensure that your description is original and culturally coherent.
3. Provide enough detail so that someone could visualize the ritual and understand its significance.

Your response should be in the following format:
Ritual Description: [Your ritual description]"""
        elif t['task_type'] == 'interpret':
            return f"""Your task is to interpret the following description of a fictional cultural ritual and provide a detailed analysis of its meaning and elements.

Ritual Description: {t['ritual_description']}

Instructions:
1. Provide a detailed interpretation of the given ritual description.
2. Explain the possible symbolism, themes, and cultural significance conveyed by the ritual.
3. Ensure that your interpretation is coherent and insightful.

Your response should be in the following format:
Interpretation: [Your interpretation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['task_type'] == 'create':
            criteria = ["The ritual description should align with the given theme.", "The ritual description should be original and culturally coherent.", "The description should provide enough detail to visualize the ritual and understand its significance."]
        elif t['task_type'] == 'interpret':
            criteria = ["The interpretation should be coherent and insightful.", "The interpretation should explain the possible symbolism, themes, and cultural significance conveyed by the ritual."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
