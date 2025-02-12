class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"concept": "Quantum Superposition", "target_audience": "A Medical Doctor"},
            "2": {"concept": "Blockchain Technology", "target_audience": "A Historian"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Explain the following complex concept in terms that are understandable to the specified target audience:

Concept: {t['concept']}
Target Audience: {t['target_audience']}

Ensure that your explanation is clear, uses appropriate analogies, and avoids unnecessary jargon. The explanation should be informative and accessible to someone with expertise in the target audience's field. Submit your explanation as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The explanation should be clear, use appropriate analogies, and avoid unnecessary jargon.", "The explanation should be informative and accessible to someone with expertise in the target audience's field."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
