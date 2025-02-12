class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"proverb": "The early bird catches the worm.", "culture": "English"},
            "2": {"proverb": "A journey of a thousand miles begins with a single step.", "culture": "Chinese"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to explain the meaning and cultural significance of the given proverb. Provide a detailed explanation that covers the literal meaning, the intended figurative meaning, and any relevant cultural context. Here is the proverb:\n\nProverb: {t['proverb']}\nCulture: {t['culture']}\n\nSubmit your response in the following format:\nLiteral Meaning: [Your explanation]\nFigurative Meaning: [Your explanation]\nCultural Significance: [Your explanation of the cultural context]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The explanation should accurately convey the literal meaning of the proverb.", "The explanation should accurately convey the figurative meaning of the proverb.", "The explanation of the cultural context should be well-explained and relevant."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
