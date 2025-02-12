class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"statement": "If it rains and it is cold, then the ground will be wet and slippery.", "direction": "to_logic"},
            "2": {"statement": "(P ∧ (Q ∨ R)) → (¬S ∧ T)", "direction": "to_natural"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['direction'] == 'to_logic':
            return f"""Your task is to translate the following natural language statement into a formal logic expression:

Statement: {t['statement']}

Use standard logical symbols such as ∧ (and), ∨ (or), ¬ (not), → (implies), and ↔ (if and only if). Provide your response in plain text format."""
        else:
            return f"""Your task is to translate the following formal logic expression into a natural language statement:

Expression: {t['statement']}

Ensure that your translation is clear, precise, and faithful to the original logical expression. Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['direction'] == 'to_logic':
            criteria = [
                "The formal logic expression should correctly represent the natural language statement.",
                "The expression should use standard logical symbols."
            ]
        else:
            criteria = [
                "The natural language statement should correctly interpret the formal logic expression.",
                "The statement should be clear and precise."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
