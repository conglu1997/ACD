class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"concept": "Photosynthesis"},
            "2": {"concept": "Quantum Entanglement"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to identify and create metaphors to explain the following scientific concept:

Concept: {t['concept']}

1. Identify a well-known metaphor that can help explain the concept.
2. Create your own metaphor that accurately and creatively explains the concept.

Ensure your metaphors are clear, accurate, and enhance understanding of the scientific concept. Provide your response in plain text format with the following structure:

1. Identified Metaphor: [Your identified metaphor]
2. Created Metaphor: [Your created metaphor]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The identified metaphor should be well-known and relevant.",
            "The created metaphor should be creative and accurately explain the concept.",
            "Both metaphors should enhance understanding of the scientific concept.",
            "The response should demonstrate a clear understanding of the concept."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
