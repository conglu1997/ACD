class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"concept": "Quantum Entanglement"},
            "2": {"concept": "Black Hole"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        concept = t["concept"]
        return f"""Compose a poem that accurately and creatively represents the following scientific concept:

Concept: {concept}

Your poem should capture the essence of the concept, demonstrating both technical understanding and creative expression. Aim for a balance between scientific accuracy and poetic beauty. Submit your poem as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The poem should accurately represent the given scientific concept.", "The poem should demonstrate creative expression and poetic quality."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
