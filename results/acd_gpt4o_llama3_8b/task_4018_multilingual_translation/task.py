class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "source_language": "English",
                "target_language": "Spanish",
                "sentence": "The quick brown fox jumps over the lazy dog."
            },
            "2": {
                "source_language": "French",
                "target_language": "German",
                "sentence": "Le chat noir dort sur le canapé."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Translate the following sentence from {t['source_language']} to {t['target_language']} while maintaining contextual accuracy and grammatical correctness.

Sentence: {t['sentence']}

Submit your translation as a plain text string in the following format:

Translation: [Your translation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        # Additional criteria for translation evaluation
        validation_criteria = [
            "The translation should maintain the original sentence's context.",
            "The translation should be grammatically correct.",
            "The translation should accurately reflect the meaning of the original sentence."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
