class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"phrase": "The early bird catches the worm."},
            "2": {"phrase": "A picture is worth a thousand words."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        phrase = t["phrase"]
        instructions = f"Interpret the following idiom or proverb. Provide a detailed explanation of its meaning and the context in which it might be appropriately used. Your explanation should cover the literal meaning, the figurative meaning, and typical scenarios where the phrase might be used. Additionally, provide a real-life example of a situation where this phrase would be relevant.\n\nPhrase: {phrase}\n\nSubmit your response in the following format:\nMeaning: [Your interpretation]\nContext: [Situations where it might be used]\nExample: [A real-life example]"
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The interpretation should accurately convey the figurative meaning of the idiom or proverb.", "The context should describe appropriate situations for using the phrase.", "The example should be a realistic scenario where the phrase is relevant."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
