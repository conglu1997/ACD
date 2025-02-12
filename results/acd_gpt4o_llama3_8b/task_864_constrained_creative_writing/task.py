class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"constraints": "Include a talking cat, a mysterious key, and set the story in a futuristic city.", "style": "Noir detective"},
            "2": {"constraints": "Involve a time-traveling historian, an ancient artifact, and set the story in medieval Europe.", "style": "Fantasy adventure"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        constraints = t['constraints']
        style = t['style']
        return f"Generate a short story based on the following constraints: {constraints}. The story should be written in the style of {style}. Ensure that the story is coherent, engaging, and adheres to the given constraints and style. Submit your story as a plain text string."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The story should be coherent and engaging.",
            "The story should adhere to the given constraints (characters, setting, elements).",
            "The story should be written in the specified style."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
