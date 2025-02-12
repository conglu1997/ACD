class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "sentence": "The quick brown fox, which was not only quick but also very brown, jumped over the lazy dog that was not very active and quite lazy, lying in the sun."
            },
            "2": {
                "sentence": "In the event that it rains on the day of the picnic, we will have to not only cancel it and reschedule it for another day but also inform all the participants about the change in plans when the weather is more appropriate for outdoor activities."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze and improve the following sentence for clarity and conciseness while preserving its original meaning:

{t['sentence']}

Ensure that your revised sentence is clear, concise, and retains the original meaning. Submit your revised sentence as a plain text string."
        """

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The revised sentence should be clear.",
            "The revised sentence should be concise.",
            "The revised sentence should preserve the original meaning."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
