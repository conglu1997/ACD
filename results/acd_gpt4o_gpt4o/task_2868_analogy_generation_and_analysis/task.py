class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"concept": "time management", "provided_analogy": "Time management is like juggling."},
            "2": {"concept": "teamwork", "provided_analogy": "Teamwork is like a symphony orchestra."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task involves two parts:

1. Generate an analogy for the following concept: {t['concept']}. Provide a detailed explanation of how the analogy relates to the concept.

2. Analyze the provided analogy: "{t['provided_analogy']}". Discuss its accuracy and appropriateness, and suggest any improvements if necessary.

Format your response as follows:

Generated Analogy: [Your analogy]
Explanation: [Your explanation]
Analysis: [Your analysis]
Suggestions: [Your suggestions, if any]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The generated analogy should be relevant and meaningful in relation to the given concept.",
            "The explanation should clearly articulate how the analogy relates to the concept.",
            "The analysis should thoughtfully evaluate the provided analogy, discussing its strengths and weaknesses.",
            "Any suggestions for improvement should be logical and enhance the provided analogy."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
