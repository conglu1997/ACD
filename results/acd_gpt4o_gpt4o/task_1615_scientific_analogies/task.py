class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"concept": "The process of photosynthesis in plants.", "type": "generate"},
            "2": {"analogy": "The Earth's atmosphere is like a greenhouse, trapping heat inside.", "type": "interpret"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["type"] == "generate":
            return f"""Your task is to create an analogy to explain the following scientific concept: {t["concept"]}. Make sure your analogy is creative and helps to clarify the concept. Provide your analogy in a single sentence."""
        else:
            return f"""Your task is to interpret the following scientific analogy: '{t["analogy"]}'. Explain what the analogy means in plain language and how it relates to the scientific concept it is describing. Provide your explanation in 2-3 sentences."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["type"] == "generate":
            criteria = ["The analogy should be creative and help clarify the given scientific concept."]
        else:
            criteria = ["The explanation should accurately convey the meaning of the analogy and relate it to the scientific concept."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
