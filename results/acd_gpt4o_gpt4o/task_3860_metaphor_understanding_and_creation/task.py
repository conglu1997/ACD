class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"metaphor": "Time is a thief."},
            "2": {"metaphor": "Knowledge is a double-edged sword."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return (
            f"Interpret the meaning of the following metaphor and create a new metaphor based on a specified theme.\n\n"
            f"Metaphor: {t['metaphor']}\n\n"
            "1. Interpret the given metaphor and explain its meaning in your own words. Ensure your explanation is clear, accurate, and contextually appropriate.\n"
            "2. Create a new metaphor based on the theme 'love'. The new metaphor should be original, coherent, and culturally appropriate.\n\n"
            "Provide your response in the following format:\n"
            "Interpretation: [Your interpretation]\n"
            "New Metaphor: [Your new metaphor]\n"
            "Explanation: [Explanation of your new metaphor]"
        )

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The interpretation should be clear, accurate, and contextually appropriate.",
            "The new metaphor should be original, coherent, and culturally appropriate.",
            "The explanation of the new metaphor should be clear and relevant to the theme of love."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0