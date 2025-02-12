class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"dilemma": "Alex and Jamie are roommates. Alex likes to play loud music while studying, but Jamie needs quiet to concentrate. Both are preparing for important exams and feel stressed. How should they resolve this conflict?"},
            "2": {"dilemma": "Maria and John are coworkers. Maria feels that John is taking credit for her work on a recent project. John, on the other hand, believes he has contributed significantly and deserves recognition. How should they address this situation?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        dilemma = t["dilemma"]
        instructions = f"""Your task is to interpret the following social dilemma and provide a thoughtful resolution considering the perspectives of all parties involved:

Dilemma: {dilemma}

Ensure that your resolution is fair, empathetic, and takes into account the feelings and needs of each individual involved. Provide your response in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The resolution should address the perspectives of all parties involved.",
            "The resolution should be empathetic and fair.",
            "The resolution should provide a practical solution to the dilemma."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
