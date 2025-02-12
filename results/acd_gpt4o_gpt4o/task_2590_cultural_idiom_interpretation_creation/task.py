class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"idiom": "A stitch in time saves nine.", "context": "Explain the meaning of this idiom in the context of preventive maintenance. Your response should be 2-3 sentences long and clearly explain how the idiom applies to the context."},
            "2": {"context": "Create a new idiom that conveys the importance of teamwork in achieving difficult goals. Your idiom should be original, and you should provide a brief explanation (2-3 sentences) of its meaning and how it fits the context."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'idiom' in t:
            return f"Interpret the following idiom and explain its meaning in the given context: '{t['idiom']}'. Context: {t['context']}"
        else:
            return f"Create a new idiom that fits the following context: '{t['context']}'"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'idiom' in t:
            criteria = ["The explanation should accurately convey the meaning of the idiom in the given context."]
        else:
            criteria = ["The created idiom should be original, meaningful, and fit the provided context."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
