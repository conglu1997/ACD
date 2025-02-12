class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "expression": "(P ∧ Q) → R",
                "manipulation_type": "convert_to_cnf"
            },
            "2": {
                "expression": "∀x (P(x) → Q(x))",
                "manipulation_type": "negate"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Manipulate the following formal logic expression based on the specified manipulation type. Provide the resulting expression in plain text format.\n\nExpression: {t['expression']}\nManipulation Type: {t['manipulation_type']}\n\nPlease submit your response in the following format:\nResulting Expression: [Your manipulated expression here]\n"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The submission should correctly follow the manipulation type specified.",
            "The resulting expression should be a valid logical expression.",
            "The manipulation should maintain logical equivalence where applicable."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
