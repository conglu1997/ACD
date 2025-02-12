class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "A large stone tablet from ancient Mesopotamia, inscribed with a code of laws, one of the oldest deciphered writings of significant length in the world. It is known for its detailed legal codes covering various aspects of daily life and justice."},
            "2": {"description": "A famous painting by Leonardo da Vinci, depicting a woman with an enigmatic expression, widely considered a masterpiece of the Italian Renaissance. It is renowned for its sophisticated use of sfumato and its mysterious background."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        description = t["description"]
        return f"""Identify the cultural artifact based on the following description and explain its historical significance and societal impact.

Description: {description}

Provide your response in the following format:
1. Name of Artifact: [Your identification of the artifact]
2. Historical Significance: [Your detailed explanation of its historical significance]
3. Societal Impact: [Your analysis of its impact on society]

Ensure your response is detailed and culturally accurate."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should correctly identify the cultural artifact.", "The response should accurately describe the historical significance.", "The analysis of the societal impact should be insightful and culturally accurate."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
