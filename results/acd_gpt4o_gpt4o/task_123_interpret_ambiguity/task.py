class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"statement": "I saw the man with the telescope.", "context": "You are in a park where people are stargazing."},
            "2": {"statement": "The chicken is ready to eat.", "context": "You are in a kitchen where dinner is being prepared."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Interpret the following ambiguous statement and provide a clear, contextually appropriate response based on the given context.

Statement: {t['statement']}
Context: {t['context']}

Provide your interpretation in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0
