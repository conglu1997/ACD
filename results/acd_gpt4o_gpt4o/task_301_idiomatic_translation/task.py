class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {'expression': "It's raining cats and dogs.", 'source_language': 'English', 'target_language': 'Spanish'},
            '2': {'expression': 'Die Katze im Sack kaufen.', 'source_language': 'German', 'target_language': 'English'}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to translate the following idiomatic expression from {t['source_language']} to {t['target_language']}. Ensure that the translation preserves the meaning and cultural context of the original expression.

Expression: {t['expression']}

Provide your translation in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The translation should preserve the meaning of the original idiomatic expression.", "The translation should be appropriate in the cultural context of the target language."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
