class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"concept": "Photosynthesis"},
            "2": {"concept": "Newton's First Law of Motion"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Explain the following scientific concept in simple terms that a middle school student could understand:

{t['concept']}
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The explanation should be clear, accurate, and easy to understand."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
