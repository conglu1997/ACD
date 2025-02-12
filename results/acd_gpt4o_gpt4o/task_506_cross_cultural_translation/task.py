class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"text": "The early bird catches the worm.", "target_language": "Spanish", "target_culture": "Spain"},
            "2": {"text": "A penny saved is a penny earned.", "target_language": "Chinese", "target_culture": "China"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to translate the given text into the target language and adapt it to fit the cultural context of the target audience.

Text: {t['text']}
Target Language: {t['target_language']}
Target Culture: {t['target_culture']}

Your response should include:
1. The translated text in the target language.
2. An explanation of how the translation was adapted to fit the cultural context.
Ensure your translation is accurate and culturally appropriate."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The translation should be accurate and in the target language.",
            "The adaptation should fit the cultural context of the target audience.",
            "The explanation should be clear and justify the cultural adaptation."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
