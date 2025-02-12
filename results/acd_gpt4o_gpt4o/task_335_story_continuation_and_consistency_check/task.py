class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"story_start": "Once upon a time, in a small village at the edge of a dark forest, there lived a young girl named Lily. She was known for her bravery and curiosity. One day, she decided to explore the forest, despite the villagers' warnings..."},
            "2": {"story_start": "In a distant land, there was a kingdom where magic was a part of everyday life. The king had three sons, each with unique magical abilities. One day, the king sent his sons on a quest to find the lost artifact that could save their kingdom from a looming threat..."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Continue the following story. Ensure that your continuation is logically consistent with the given start and maintains coherence throughout the narrative. The continuation should be at least 300 words long.

Story Start: {t['story_start']}

Provide your continuation in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The continuation should be logically consistent with the given start.", "The narrative should maintain coherence throughout.", "The continuation should be at least 300 words long."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
