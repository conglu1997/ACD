class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"context": "During a difficult negotiation, the CEO advised his team to 'keep their cards close to their chest.'", "task_type": "interpretation"},
            "2": {"context": "A friend is feeling down after a breakup, and you want to cheer them up with an encouraging proverb.", "task_type": "generation"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task_type"] == "interpretation":
            return """Your task is to explain the meaning of the idiomatic expression used in the following context:

{0}

Ensure that your explanation is clear, accurate, and captures the essence of the idiom. Provide your response in plain text format.""".format(t["context"])
        elif t["task_type"] == "generation":
            return """Your task is to generate an appropriate proverb or idiomatic expression for the following context:

{0}

Ensure that your response is suitable for the given context and conveys the intended message clearly. Provide your response in plain text format.""".format(t["context"])

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The explanation should accurately convey the meaning of the idiomatic expression in the given context." if t["task_type"] == "interpretation" else "The generated idiom or proverb should be appropriate for the context and convey the intended message."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
