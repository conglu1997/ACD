class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"concept": "Quantum Entanglement", "context": "Science"},
            "2": {"concept": "Social Media", "context": "Technology"},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create an analogy to explain the following concept in a creative and coherent manner: {t["concept"]}

Context: {t["context"]}

Your analogy should be:
1. Clear and easy to understand for someone unfamiliar with the concept.
2. Imaginative and creative.
3. Logically sound and clearly related to the concept.

Submit your response as a plain text string in the following format:

Analogy: [Your analogy]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The analogy should be imaginative and creative.", "The analogy should help explain the concept clearly for someone unfamiliar with it.", "The analogy should be logically sound and clearly related to the concept."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
