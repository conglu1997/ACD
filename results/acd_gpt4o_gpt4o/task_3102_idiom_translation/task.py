class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"idiom": "Il pleut des cordes", "source_language": "French", "target_language": "English"},
            "2": {"idiom": "Die Katze im Sack kaufen", "source_language": "German", "target_language": "English"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to translate the following idiomatic expression from {t['source_language']} to {t['target_language']} and provide a clear explanation of its meaning.

Idiom: {t['idiom']}

Provide your response in the following format:

Translation: [Your translation]
Explanation: [Your explanation]

Ensure your translation is accurate and your explanation is clear and contextually appropriate."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The translation should be accurate.",
            "The explanation should be clear and contextually appropriate.",
            "The response should be in the specified format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
