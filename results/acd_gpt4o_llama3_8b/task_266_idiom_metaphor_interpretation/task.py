class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "expression": "Kick the bucket"
            },
            "2": {
                "expression": "Burn the midnight oil"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Interpret the given idiom or metaphor and explain its meaning in a clear and concise manner. Ensure that your explanation is between 30-50 words. Submit your explanation as a plain text string.\n\nExpression: {t['expression']}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The explanation should accurately reflect the meaning of the idiom or metaphor.",
            "The explanation should be clear and concise.",
            "The explanation should be between 30-50 words."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
