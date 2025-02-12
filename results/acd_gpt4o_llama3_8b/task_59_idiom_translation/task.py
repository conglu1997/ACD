class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"idiom": "It's raining cats and dogs.", "from_lang": "English", "to_lang": "Spanish"},
            "2": {"idiom": "Tomber dans les pommes.", "from_lang": "French", "to_lang": "English"},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Translate the following idiom from {t["from_lang"]} to {t["to_lang"]} and explain its cultural context:

Idiom: {t["idiom"]}

Ensure your translation captures the idiomatic meaning and not just the literal words. Provide a brief explanation of the cultural or historical context of the idiom. Submit your response as a plain text string in the following format:

Translation: [Your Translation]
Cultural Context: [Your Explanation]

Both parts of your response are crucial for a successful completion of the task."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The translation should capture the idiomatic meaning.",
            "The cultural context explanation should be accurate and relevant.",
            "The response should follow the format: Translation: [Your Translation] Cultural Context: [Your Explanation]"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
