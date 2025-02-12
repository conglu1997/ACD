class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"concept": "Quantum Entanglement", "audience": "a 10-year-old child who loves science"},
            "2": {"concept": "Blockchain Technology", "audience": "a senior citizen with no technical background who is curious about new technologies"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to explain the following complex concept in simple terms tailored for the given audience:

Concept: {t['concept']}
Audience: {t['audience']}

Ensure that your explanation is clear, accurate, and appropriate for the specified audience. Avoid using jargon and aim to make the explanation engaging and easy to understand. Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The explanation should be clear and accurate.", "The explanation should be appropriate for the given audience.", "The explanation should avoid technical jargon and be engaging."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
