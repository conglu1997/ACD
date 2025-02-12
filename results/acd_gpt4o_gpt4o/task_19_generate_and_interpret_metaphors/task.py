class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "A challenging situation at work where someone feels overwhelmed.", "type": "generate"},
            "2": {"metaphor": "The world is a stage, and we are merely players.", "type": "interpret"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["type"] == "generate":
            return f"""Your task is to create a metaphor for the following scenario: {t["scenario"]}. Make sure your metaphor is creative and captures the essence of the situation. Provide your metaphor in a single sentence."""
        else:
            return f"""Your task is to interpret the following metaphor: '{t["metaphor"]}'. Explain what the metaphor means in plain language. Provide your explanation in 2-3 sentences."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["type"] == "generate":
            criteria = ["The metaphor should be creative and capture the essence of the given scenario."]
        else:
            criteria = ["The explanation should accurately convey the meaning of the metaphor in plain language."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
