class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {
                'text': 'As she walked into the room, her heart raced with excitement. The anticipation of seeing her loved ones after so long brought a smile to her face.'
            },
            '2': {
                'text': 'He sat alone in the dark room, feeling the weight of the world on his shoulders. The crushing sense of failure and loneliness was almost unbearable.'
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Identify and describe the emotions conveyed in the following text:

Text: {t['text']}

Your response should include:
1. The primary emotion(s) conveyed.
2. A brief explanation of how the text conveys these emotions.

Ensure that your description is clear, accurate, and captures the essence of the emotions expressed in the text. Submit your response as a plain text string in the following format:

Emotion(s): [Primary emotion(s)]
Explanation: [Explanation of how the text conveys these emotions]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            'The response must include the primary emotion(s) conveyed in the text.',
            'The explanation should accurately describe how the text conveys these emotions.'
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
