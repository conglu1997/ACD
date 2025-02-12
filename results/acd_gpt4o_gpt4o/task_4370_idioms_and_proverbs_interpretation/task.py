class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"idiom": "A stitch in time saves nine.", "target_language": "Spanish"},
            "2": {"proverb": "When in Rome, do as the Romans do.", "target_language": "French"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'idiom' in t:
            expression_type = "idiom"
            expression = t["idiom"]
        else:
            expression_type = "proverb"
            expression = t["proverb"]

        return f"""Your task is to interpret the following {expression_type} and provide its equivalent in {t["target_language"]}:

{expression}

Make sure your interpretation captures the meaning and cultural context of the original expression. Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should accurately capture the meaning of the original expression.",
            "The response should be culturally appropriate and equivalent in the target language."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
