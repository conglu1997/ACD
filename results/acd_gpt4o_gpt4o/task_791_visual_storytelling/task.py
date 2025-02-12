class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {"scene_description": "A bustling medieval marketplace with merchants selling their goods, children playing, and a mysterious cloaked figure in the shadows."},
            "2": {"scene_description": "A serene forest clearing with a sparkling stream, colorful flowers, and a unicorn drinking from the water."}
        }
        assert len(tasks) == 2, "There should be exactly two tasks."
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Interpret the detailed description of the visual scene provided and generate a creative story based on it.

Scene Description: {t['scene_description']}

1. Describe the scene in your own words to set the context for your story. Ensure your description is vivid and captures all key elements.
2. Generate a creative and engaging story that takes place within the described scene. The story should have a clear beginning, middle, and end, and should make use of the elements in the scene description.

Provide your response in the following format:

Scene Description Interpretation: [Your interpretation]
Story: [Your creative story]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0
