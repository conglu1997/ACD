class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"text": "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness..."},
            "2": {"text": "All happy families are alike; each unhappy family is unhappy in its own way."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Interpret the following excerpt from literature. Identify and explain the literary devices used and the main themes presented in the text. Provide a detailed analysis that demonstrates a deep understanding of the text. Submit your response as a plain text string in the following format:

Excerpt: '{t["text"]}'

Analysis: [Your detailed analysis]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The analysis should identify and explain the literary devices used.",
            "The analysis should identify and explain the main themes presented in the text.",
            "The analysis should be detailed and demonstrate a deep understanding of the text."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
