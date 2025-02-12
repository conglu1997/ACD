class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "text_segment": "It was a bright cold day in April, and the clocks were striking thirteen.",
                "style": "Shakespearean"
            },
            "2": {
                "text_segment": "The sky above the port was the color of television, tuned to a dead channel.",
                "style": "Victorian"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Rewrite the following text segment in the specified literary style:

Text Segment: {t['text_segment']}

Style: {t['style']}

Ensure that your rewritten text accurately reflects the linguistic and stylistic characteristics of the specified style. Submit your response as a plain text string in the following format:

Rewritten Text: [Your rewritten text]

Example:
Original: It was a bright cold day in April, and the clocks were striking thirteen.
Style: Shakespearean
Rewritten Text: 'Twas a radiant and frigid April morn, and the clocks tolled thirteen.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The response should reflect the specified literary style.",
            "The response should accurately capture the linguistic characteristics of the style.",
            "The response should be coherent and maintain the original meaning."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
