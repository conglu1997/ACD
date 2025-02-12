class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"concept": "Quantum Entanglement"},
            "2": {"concept": "CRISPR-Cas9 Gene Editing"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Simplify the following scientific concept into layman's terms: {t["concept"]}. Your explanation should be clear, concise, and accessible to someone with no background in the subject. Avoid using technical jargon and ensure that your explanation captures the essence of the concept. Submit your response as a plain text string in the following format:
Explanation: [Your explanation here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The explanation should be clear and accessible to a layperson.", "The explanation should avoid technical jargon.", "The explanation should capture the essence of the concept."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
