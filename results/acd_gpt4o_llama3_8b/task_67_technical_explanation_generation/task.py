class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"concept": "Quantum Computing"},
            "2": {"concept": "Blockchain"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        concept = t["concept"]
        return f"""Explain the concept of '{concept}' in a way that a layperson with no technical background can understand. Ensure that your explanation is clear, concise, and avoids technical jargon. Your explanation should help the reader grasp the basic idea and significance of the concept. Submit your explanation as a plain text string in a single paragraph."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The explanation should be clear and concise.",
            "The explanation should avoid technical jargon.",
            "The explanation should accurately convey the basic idea and significance of the concept."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
