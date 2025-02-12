class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "type": "to_symbolic",
                "statement": "If it rains, it is cold, and people forget their umbrellas, then the ground will be wet, and people will get wet and wear coats."
            },
            "2": {
                "type": "to_natural",
                "expression": "(P ∧ ¬Q) ∨ (R → (S ∧ T))"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['type'] == 'to_symbolic':
            return f"""Convert the following natural language statement into a symbolic logic expression:

Statement: {t['statement']}

Use standard symbolic logic notation such as '¬' for NOT, '∧' for AND, '∨' for OR, '→' for IMPLIES, and '↔' for IFF (if and only if). Ensure your response is syntactically correct and logically accurate. Submit your response as a plain text string in the format: [Symbolic Logic Expression].

Example: 'If it rains, then the ground will be wet.' should be converted to 'P → Q'."""
        else:
            return f"""Convert the following symbolic logic expression into a natural language statement:

Expression: {t['expression']}

Ensure your translation is clear, grammatically correct, and accurately reflects the meaning of the symbolic logic expression. Submit your response as a plain text string in the format: [Natural Language Statement].

Example: 'P ∧ Q → R' should be converted to 'If P and Q, then R'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['type'] == 'to_symbolic':
            validation_criteria = ["The response should use standard symbolic logic notation and accurately represent the given natural language statement."]
        else:
            validation_criteria = ["The response should accurately reflect the meaning of the symbolic logic expression in clear natural language."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
