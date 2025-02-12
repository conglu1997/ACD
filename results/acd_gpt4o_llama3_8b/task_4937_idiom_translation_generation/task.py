class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "source_language": "English",
                "target_language": "Spanish",
                "idiom": "Break the ice"
            },
            "2": {
                "source_language": "French",
                "target_language": "German",
                "idiom": "Appeler un chat un chat"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Translate the following idiomatic expression from {t['source_language']} to {t['target_language']} and provide an equivalent idiom in the target language, if one exists.

Idiom: {t['idiom']}

Submit your response as a plain text string in the following format:

Translation: [Your translation]
Equivalent Idiom: [Equivalent idiom in the target language, if one exists]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The translation should accurately reflect the meaning of the original idiom.",
            "The equivalent idiom should be culturally appropriate and convey the same meaning as the original idiom.",
            "If no equivalent idiom exists, the translation should still accurately convey the meaning of the original idiom."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
