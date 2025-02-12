class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "source_concept": "time",
                "target_concept": "river",
                "task_type": "generation"
            },
            "2": {
                "source_concept": "knowledge",
                "target_concept": "tree",
                "task_type": "generation"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a creative analogy that draws a meaningful parallel between the following concepts. Ensure that your analogy is insightful and highlights a significant similarity between the two concepts. Submit your analogy as a plain text string.

Source Concept: {t['source_concept']}
Target Concept: {t['target_concept']}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The analogy should draw a meaningful parallel between the source and target concepts.",
            "The analogy should be creative and insightful.",
            "The analogy should be coherent and clearly articulated."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
