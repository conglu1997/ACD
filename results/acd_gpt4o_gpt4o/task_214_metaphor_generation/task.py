class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"concept": "time"},
            "2": {"concept": "knowledge"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a metaphor based on the following concept. After generating the metaphor, provide an explanation of its meaning and how it relates to the concept.

Concept: {t['concept']}

Your response should include:
1. A creative and original metaphor that captures the essence of the given concept.
2. A clear and concise explanation of the metaphor's meaning.
3. An explanation of how the metaphor relates to the given concept.

Ensure your metaphor is inventive and your explanation is comprehensive. Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include a creative and original metaphor that captures the essence of the given concept.",
            "The explanation of the metaphor's meaning should be clear and concise.",
            "The explanation should clearly relate the metaphor to the given concept."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
