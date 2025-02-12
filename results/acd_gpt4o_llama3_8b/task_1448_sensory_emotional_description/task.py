class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scene": "A bustling city market at sunset", "emotions": ["excitement", "wonder"]},
            "2": {"scene": "A quiet beach at dawn", "emotions": ["peace", "nostalgia"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        scene = t["scene"]
        emotions = ', '.join(t["emotions"])
        return f"""Describe the following scene in a way that evokes the specified sensory perceptions and emotions:

Scene: {scene}
Emotions to evoke: {emotions}

Your description should include vivid sensory details (sights, sounds, smells, etc.) and convey the specified emotions effectively. Submit your description as a plain text string in the following format:

Description: [Your description]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The description should include vivid sensory details.", "The description should evoke the specified emotions."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
