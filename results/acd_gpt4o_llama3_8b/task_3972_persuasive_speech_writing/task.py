class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "topic": "The importance of renewable energy",
                "audience": "A group of high school students"
            },
            "2": {
                "topic": "The benefits of a healthy diet",
                "audience": "A community health seminar attended by adults"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Based on the following topic and audience profile, generate an original persuasive speech. Your speech should be engaging, logically structured, and tailored to the audience. Use rhetorical techniques such as ethos, pathos, and logos to strengthen your argument. Do not rely on pre-existing speeches.

Topic: {t['topic']}
Audience: {t['audience']}

Submit your speech as a plain text string in the following format:

Speech:
[Your speech here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The speech should be logically structured.",
            "The speech should use rhetorical techniques effectively.",
            "The speech should be engaging and tailored to the specified audience.",
            "The speech should be original and not rely on pre-existing speeches."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0