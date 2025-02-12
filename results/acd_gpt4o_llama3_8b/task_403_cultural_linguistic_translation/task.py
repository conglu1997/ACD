class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "phrase": "To let the cat out of the bag. This means to reveal a secret inadvertently.",
                "source_language": "English",
                "target_language": "Spanish"
            },
            "2": {
                "phrase": "To burn the midnight oil. This means to work late into the night.",
                "source_language": "English",
                "target_language": "French"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Translate the following culturally specific phrase or idiom from {t['source_language']} to {t['target_language']} while preserving its original meaning:

Phrase: {t['phrase']}

Your translation should accurately reflect the cultural context and idiomatic meaning of the original phrase. Do not provide a literal translation. Submit your translation as a plain text string in the format:

Translation: [Your translation here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = ["The translation should accurately reflect the cultural context.", "The translation should preserve the idiomatic meaning of the original phrase.", "The translation should not be literal."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
