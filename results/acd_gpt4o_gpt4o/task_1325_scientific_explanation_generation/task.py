class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"topic": "photosynthesis"},
            "2": {"topic": "quantum entanglement"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        topic = t['topic']
        return f"""Your task is to generate a detailed explanation for the following scientific phenomenon:

Topic: {topic}

Your explanation should cover the following aspects:
1. Definition: Provide a clear and concise definition of the phenomenon.
2. Process: Explain the process or mechanism involved in the phenomenon.
3. Significance: Discuss the significance or importance of the phenomenon in its respective field.
4. Examples: Provide examples or applications of the phenomenon in real life.

Ensure that your explanation is accurate, comprehensive, and easy to understand. Provide your response in plain text format with the following structure:

1. Definition: [Your definition]
2. Process: [Your explanation of the process or mechanism]
3. Significance: [Discussion of significance]
4. Examples: [Examples or applications]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should accurately define the phenomenon.",
            "The response should explain the process or mechanism involved.",
            "The response should discuss the significance or importance of the phenomenon.",
            "The response should provide examples or applications of the phenomenon."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
