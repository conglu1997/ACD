class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task_type": "interpret", "music_description": "A lively piece with a fast tempo, featuring a dominant violin melody and rhythmic accompaniment by piano."},
            "2": {"task_type": "generate", "theme": "melancholy"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task_type'] == 'interpret':
            return f"""Your task is to interpret the following musical description and provide a detailed analysis of its elements and the emotions it conveys.

Music Description: {t['music_description']}

Instructions:
1. Provide a detailed interpretation of the given musical description, focusing on elements such as melody, harmony, rhythm, and instrumentation.
2. Explain the possible emotions, themes, and imagery conveyed by the music.
3. Ensure that your interpretation is coherent and insightful.

Your response should be in the following format:
Interpretation: [Your interpretation]"""
        elif t['task_type'] == 'generate':
            return f"""Your task is to generate a detailed description for a new musical composition based on the given theme.

Theme: {t['theme']}

Instructions:
1. Create a vivid and imaginative description of a new musical piece that aligns with the given theme, focusing on elements such as melody, harmony, rhythm, and instrumentation.
2. Ensure that your description is original and creative.
3. Provide enough detail so that someone could imagine the music based on your words.

Your response should be in the following format:
Music Description: [Your music description]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['task_type'] == 'interpret':
            criteria = ["The interpretation should be coherent and insightful.", "The interpretation should explain the possible emotions, themes, and imagery conveyed by the music.", "The interpretation should focus on elements such as melody, harmony, rhythm, and instrumentation."]
        elif t['task_type'] == 'generate':
            criteria = ["The music description should align with the given theme.", "The music description should be original and creative.", "The description should provide enough detail to imagine the music.", "The description should focus on elements such as melody, harmony, rhythm, and instrumentation."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
