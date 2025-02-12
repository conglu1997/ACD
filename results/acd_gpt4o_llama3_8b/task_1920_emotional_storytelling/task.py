class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"emotion": "joy", "theme": "reunion", "event": "unexpected meeting at a park"},
            "2": {"emotion": "sorrow", "theme": "loss", "event": "finding a memento in an old drawer"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a short story that evokes the following emotion and theme:

Emotion: {t['emotion']}
Theme: {t['theme']}
Event: {t['event']}

Your story should be emotionally impactful and should clearly convey the given emotion, theme, and event. Use descriptive language to bring the story to life. The story should be between 200 and 500 words long.

Submit your story as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [f"The story should evoke a sense of {t['emotion']}.", f"The story should clearly convey the theme of {t['theme']}.", f"The story should include the event: {t['event']}.", "The story should be between 200 and 500 words long."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
