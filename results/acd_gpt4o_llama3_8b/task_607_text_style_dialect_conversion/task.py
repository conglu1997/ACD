class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "original_text": "Hey! How are you doing today? I was thinking we could grab some coffee and catch up.",
                "target_style": "Shakespearean English"
            },
            "2": {
                "original_text": "Please ensure that all the reports are submitted by the end of the day. We need to review them before the meeting tomorrow.",
                "target_style": "Southern American English Dialect"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Convert the given text into the specified style or dialect while preserving the original meaning. Ensure that the transformed text accurately reflects the target style or dialect.

Original Text:
{t['original_text']}

Target Style/Dialect:
{t['target_style']}

Format your response as follows:
Transformed Text: [Your transformed text here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The transformed text should preserve the original meaning.",
            "The transformed text should accurately reflect the specified style or dialect."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
