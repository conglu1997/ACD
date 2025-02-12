class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "phrase": "It's raining cats and dogs.",
                "target_language": "Spanish"
            },
            "2": {
                "phrase": "Break a leg!",
                "target_language": "French"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to translate the following idiomatic expression or culturally specific phrase into the target language while preserving its meaning and cultural context:\n\nPhrase: {t['phrase']}\nTarget Language: {t['target_language']}\n\nYour translation should adhere to the following guidelines:\n1. Convey the same meaning and sentiment as the original phrase.\n2. Be culturally appropriate and natural-sounding in the target language.\n3. Avoid literal translation if it does not preserve the idiomatic meaning.\n\nProvide your translation in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The translation conveys the same meaning and sentiment as the original phrase.",
            "The translation is culturally appropriate and natural-sounding in the target language.",
            "The translation avoids literal translation if it does not preserve the idiomatic meaning."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
