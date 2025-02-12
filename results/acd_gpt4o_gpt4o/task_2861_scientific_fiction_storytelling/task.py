class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"concept": "quantum entanglement", "setting": "a futuristic city"},
            "2": {"concept": "photosynthesis", "setting": "an alien planet"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to write a short story incorporating the following scientific concept and setting:

Scientific Concept: {t['concept']}
Setting: {t['setting']}

Your story should be between 300 and 500 words. Ensure that the scientific concept is accurately represented and creatively integrated into the narrative. Provide your story in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The story should accurately represent the scientific concept.",
            "The story should be creative and engaging.",
            "The story should be between 300 and 500 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
