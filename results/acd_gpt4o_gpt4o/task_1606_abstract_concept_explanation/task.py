class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"concept": "time"},
            "2": {"concept": "justice"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to explain the following abstract concept using analogies and examples:

Concept: {t['concept']}

Your explanation should be clear, creative, and help a layperson understand the concept. Use at least one distinct analogy and one distinct example in your explanation.

Please provide your response in the following format:

Explanation: <your explanation>
Analogy: <your analogy>
Example: <your example>"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        # Define criteria for evaluation
        criteria = [
            "The explanation should be clear and understandable to a layperson.",
            "The explanation should include at least one distinct analogy.",
            "The explanation should include at least one distinct example.",
            "The analogy and example should be relevant and help explain the concept.",
            "The analogy and example should not be the same or overlap significantly."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
