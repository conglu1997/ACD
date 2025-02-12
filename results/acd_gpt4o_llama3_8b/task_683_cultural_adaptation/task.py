class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"text": "John invited his friends over for a Thanksgiving dinner. They enjoyed a traditional feast of turkey, stuffing, and pumpkin pie.", "target_culture": "Japan"},
            "2": {"text": "The company's annual Christmas party was a hit, with carol singing, gift exchanges, and a visit from Santa Claus.", "target_culture": "India"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Adapt the following text to fit the cultural context of {t["target_culture"]}, while maintaining the original meaning and intent:

'{t["text"]}'

Your response should consider cultural norms, traditions, and appropriate language. Submit your adaptation as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The adaptation should accurately reflect the cultural context of the target culture.",
            "The original meaning and intent of the text should be preserved.",
            "The language should be appropriate and respectful to the target culture."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
