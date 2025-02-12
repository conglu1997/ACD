class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "concept": "Quantum Entanglement"
            },
            "2": {
                "concept": "General Relativity"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are given a scientific concept. Your task is to explain this concept in two different ways:

1. Explain the concept in layman's terms, making it understandable to someone without any scientific background.
2. Explain the concept in a technical manner, suitable for an expert in the field.

Concept: {t['concept']}

Submit your response in the following format:

Layman's Explanation: [Your explanation]
Technical Explanation: [Your explanation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The layman's explanation should be clear, simple, and free of technical jargon.",
            "The technical explanation should be detailed, accurate, and use appropriate terminology.",
            "Both explanations should correctly convey the concept.",
            "The response should include both explanations in the correct format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
