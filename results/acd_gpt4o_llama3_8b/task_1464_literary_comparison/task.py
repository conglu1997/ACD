class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "work1": "To Kill a Mockingbird by Harper Lee",
                "work2": "1984 by George Orwell",
                "criteria": "Compare the themes of justice and morality in these two works."
            },
            "2": {
                "work1": "Pride and Prejudice by Jane Austen",
                "work2": "Wuthering Heights by Emily Brontë",
                "criteria": "Compare the portrayal of social class and relationships in these two works."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Compare the following literary works based on the given criteria:

Work 1: {t['work1']}
Work 2: {t['work2']}

Criteria: {t['criteria']}

Your response should include a detailed comparison that discusses the specified aspects of both works. Ensure your comparison is well-organized, coherent, and provides insightful analysis. Your response should be between 300 to 500 words. Submit your response as a plain text string with the following sections:

1. Introduction: [Introduce the two works and the criteria]
2. Comparison: [Provide a detailed comparison based on the criteria]
3. Conclusion: [Summarize your findings]

Example Format:

Introduction: [Your introduction here]
Comparison: [Your comparison here]
Conclusion: [Your conclusion here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The comparison should address the specified criteria.",
            "The analysis should be coherent and well-organized.",
            "The comparison should provide insights into both works."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
