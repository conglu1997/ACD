class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "paradox": "The Liar Paradox: 'This statement is false.'"
            },
            "2": {
                "paradox": "The Ship of Theseus: If a ship has all of its components replaced, is it still the same ship?"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Explain the following paradox clearly and logically. Your explanation should include the origin of the paradox, why it is considered a paradox, and any notable attempts to resolve it. Ensure your explanation is at least 200 words long. Submit your response as a plain text string.

Paradox: {t['paradox']}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The explanation should be clear and logical.",
            "The explanation should include the origin of the paradox.",
            "The explanation should describe why it is considered a paradox.",
            "The explanation should mention any notable attempts to resolve the paradox.",
            "The explanation should be at least 200 words long.",
            "The explanation should logically follow through all the counterintuitive aspects of the paradox."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
