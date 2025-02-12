class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"emoji_sentence": "👩‍🎓📚➡️🏆", "synthetic_examples": ["🏠+🍕=❤️ -> Home plus pizza equals love.", "🌧️🌈=😊 -> Rain plus rainbow equals happiness."]},
            "2": {"emoji_sentence": "🚀🌕👨‍🚀👩‍🚀", "synthetic_examples": ["🌟🔭👀=✨ -> Star plus telescope equals wonder.", "🔥🍲=😋 -> Fire plus soup equals delicious."]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        examples = '\n'.join(t.get('synthetic_examples', []))
        return f"Translate the following emoji sentence into plain text: {t['emoji_sentence']}\nExample translations:\n{examples}"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The translation should accurately represent the meaning of the emoji sentence."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
