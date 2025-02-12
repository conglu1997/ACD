class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "concept_1": "Black hole (Science)",
                "concept_2": "Mystery novel (Literature)"
            },
            "2": {
                "concept_1": "Symphony (Music)",
                "concept_2": "Fractal pattern (Mathematics)"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate an analogy that connects the following two concepts from different disciplines. Explain the analogy in detail, highlighting the similarities and insights gained from comparing these concepts. Your explanation should be coherent, creative, and demonstrate a deep understanding of both concepts. The analogy and explanation should be between 150 and 300 words.

Concept 1: {t['concept_1']}
Concept 2: {t['concept_2']}

Submit your analogy and explanation as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The analogy should be coherent and make logical connections between the two concepts.",
            "The explanation should demonstrate a deep understanding of both concepts.",
            "The analogy should be creative and provide unique insights.",
            "The response should be between 150 and 300 words."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
