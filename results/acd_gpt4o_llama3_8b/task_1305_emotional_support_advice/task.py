class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "A friend just lost their job and feels hopeless. They have been struggling to find a new job for the past six months and are starting to doubt their self-worth."
            },
            "2": {
                "scenario": "A student is feeling overwhelmed by their final exams and is considering dropping out. They have been studying non-stop for weeks but feel like they are not making any progress and are afraid of failing."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Provide emotional support and advice to someone in the following scenario:

Scenario: {t['scenario']}

Your response should be empathetic, supportive, and offer constructive advice to help the person cope with their situation. Ensure that your response is sensitive to the person's feelings and provides practical suggestions for moving forward. Aim to write a response that is between 100 to 200 words. Submit your response as a plain text string.

Example response format:
Supportive Message: [Your supportive message here]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The response should be empathetic and supportive.",
            "The response should validate the person's feelings.",
            "The response should offer practical advice for coping with the situation.",
            "The response should be sensitive to the person's feelings.",
            "The response should be well-organized and easy to understand.",
            "The response should be between 100 to 200 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
