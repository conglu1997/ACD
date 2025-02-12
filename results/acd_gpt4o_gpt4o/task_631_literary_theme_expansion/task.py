class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"literary_work": "To Kill a Mockingbird by Harper Lee", "theme": "racial injustice"},
            "2": {"literary_work": "1984 by George Orwell", "theme": "totalitarianism"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to analyze the theme of the following literary work and creatively expand upon it in a new context:

Literary Work: {t["literary_work"]}
Theme: {t["theme"]}

First, provide a detailed analysis of how the theme is presented in the literary work. Then, create a short story or scene of at least 300 words that explores this theme in a modern or futuristic setting. Ensure that your analysis is insightful and that your creative piece effectively reflects the theme. Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The analysis should be detailed and insightful.",
            "The creative piece should effectively reflect the theme in a new context.",
            "The response should be well-structured and coherent.",
            "The creative piece should be at least 300 words long."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
