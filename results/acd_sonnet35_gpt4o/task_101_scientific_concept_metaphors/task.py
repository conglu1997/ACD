class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "concept": "Quantum Entanglement",
                "field": "Quantum Physics"
            },
            "2": {
                "concept": "Epigenetics",
                "field": "Molecular Biology"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a detailed metaphor for the scientific concept of {t['concept']} from the field of {t['field']}. Your response should include:

1. A creative and vivid metaphor (3-5 sentences) that accurately represents the key aspects of the scientific concept. The metaphor should be original and not a commonly used analogy for this concept.
2. An explanation (100-150 words) of how your metaphor relates to the scientific concept, highlighting at least three specific parallels between elements of your metaphor and aspects of the concept.
3. A brief discussion (50-75 words) of the strengths and limitations of your metaphor in conveying the scientific concept, including at least one strength and one limitation.

Ensure that your metaphor is both scientifically accurate and accessible to a general audience. Be creative while maintaining the integrity of the scientific concept. Do not use technical jargon without explanation."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The metaphor accurately represents at least three key aspects of {t['concept']}.",
            "The metaphor is original and not a commonly used analogy for this concept.",
            "The explanation clearly links at least three elements of the metaphor to specific aspects of the scientific concept.",
            "The response discusses at least one strength and one limitation of the metaphor.",
            "The metaphor is creative and vivid while maintaining scientific accuracy.",
            "The response avoids unexplained technical jargon and is accessible to a general audience."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
