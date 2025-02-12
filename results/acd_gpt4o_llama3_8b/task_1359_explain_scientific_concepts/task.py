class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "concept": "Quantum Entanglement"
            },
            "2": {
                "concept": "CRISPR-Cas9 Gene Editing"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Explain the following scientific concept in detail:

Concept: {t['concept']}

Your explanation should include:
1. A clear and concise definition of the concept.
2. An explanation of the underlying principles and mechanisms.
3. Real-world examples or applications of the concept.
4. Ensure that your explanation is accurate, coherent, and easy to understand for someone with a basic scientific background.
5. Use appropriate scientific terminology and avoid oversimplification.

Submit your explanation as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The explanation should include a clear and concise definition of the concept.",
            "The explanation should cover the underlying principles and mechanisms accurately.",
            "The explanation should provide real-world examples or applications of the concept.",
            "The explanation should be coherent, well-structured, and easy to understand for someone with a basic scientific background.",
            "The explanation should use appropriate scientific terminology and avoid oversimplification."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
