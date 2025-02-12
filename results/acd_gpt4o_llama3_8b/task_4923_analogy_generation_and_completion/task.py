class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "concept": "time",
                "task_type": "generate"
            },
            "2": {
                "incomplete_analogy": "Bird is to sky as fish is to ___",
                "task_type": "complete"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task_type"] == "generate":
            return f"""Generate a creative and meaningful analogy based on the given concept. Ensure that the analogy is original and clearly demonstrates the relationship between the elements being compared.

Concept:
{t['concept']}

Submit your response as a plain text string in the following format:

Analogy: [Your analogy here]
Explanation: [Your explanation of the analogy here]"""
        elif t["task_type"] == "complete":
            return f"""Complete the following analogy by identifying the correct relationship between the given pairs of words or phrases.

Incomplete Analogy:
{t['incomplete_analogy']}

Submit your response as a plain text string in the following format:

Completion: [Your completion here]
Explanation: [Your explanation of the relationship here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = []
        if t["task_type"] == "generate":
            validation_criteria = ["The analogy must be original and meaningful.", "The explanation must clearly demonstrate the relationship between the elements being compared."]
        elif t["task_type"] == "complete":
            validation_criteria = ["The completion must correctly identify the relationship between the given pairs of words or phrases.", "The explanation must clearly demonstrate the understanding of the relationship."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
