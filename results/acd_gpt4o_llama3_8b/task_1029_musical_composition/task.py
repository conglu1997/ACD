class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "joy", "emotion": "happy", "composition": "C D E F G A B C | C D E F G A B C | C D E F G A B C | C D E F G A B C"},
            "2": {"theme": "melancholy", "emotion": "sad", "composition": "C E G E C | C E G E C | C E G E C | C E G E C"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        theme = t['theme']
        emotion = t['emotion']
        composition = t['composition']
        return f"""Task 1: Generate a short piece of music (in ABC notation) based on the following theme and emotion.

Theme: {theme}
Emotion: {emotion}

Your composition should be creative and reflect the given theme and emotion. Ensure it is at least 8 bars long. Submit your composition as a plain text string in ABC notation format.

Task 2: Identify the musical structure of the following composition.

Composition: {composition}

Describe the structure in terms of musical phrases, repetitions, and patterns. Ensure your description is at least 50 words long. Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0
