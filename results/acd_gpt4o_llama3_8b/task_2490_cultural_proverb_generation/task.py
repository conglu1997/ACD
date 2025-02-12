class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"culture": "Japanese", "proverb": "A frog in a well does not know the ocean."},
            "2": {"culture": "African", "proverb": "If you want to go fast, go alone. If you want to go far, go together."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        culture = t["culture"]
        proverb = t["proverb"]
        return f"""Interpret the following proverb from {culture} culture and generate a new proverb that fits the same cultural context.

Proverb: {proverb}

Your interpretation should include:
1. Explanation of the meaning of the proverb.
2. The cultural context and significance of the proverb.

Then, generate a new proverb or idiom that could fit within the same cultural context. Ensure your response is culturally appropriate, logically coherent, and clearly articulated. Submit your response in the following format:

Interpretation: [Your interpretation]
New Proverb: [Your new proverb]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The interpretation should accurately explain the meaning of the given proverb.",
            "The cultural context and significance should be well-explained.",
            "The new proverb should be culturally appropriate and logically coherent.",
            "The response should be clearly articulated and follow the specified format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
