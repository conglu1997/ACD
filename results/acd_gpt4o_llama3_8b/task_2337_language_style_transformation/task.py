class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"text": "Once upon a time, in a land far, far away, there was a small village surrounded by beautiful mountains and lush forests. The villagers lived in peace and harmony, always helping one another.", "style_from": "fairy tale", "style_to": "news report"},
            "2": {"text": "The sun set over the horizon, casting a warm orange glow over the tranquil sea. Seagulls flew overhead, their cries echoing in the gentle evening breeze.", "style_from": "descriptive", "style_to": "poetic"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Transform the following text from {t["style_from"]} style to {t["style_to"]} style while preserving the original meaning:

Original Text: {t["text"]}

Your transformed text should maintain the original meaning but should be written in the {t["style_to"]} style. Ensure that your response is coherent, stylistically accurate, and preserves the essence of the original text. Submit your response as a plain text string.

Example 1:
Original Text (fairy tale): 'Once upon a time, in a land far, far away, there was a small village surrounded by beautiful mountains and lush forests. The villagers lived in peace and harmony, always helping one another.'
Transformed Text (news report): 'A remote village, nestled amidst scenic mountains and lush forests, is known for its peaceful and harmonious community where residents continually support each other.'

Example 2:
Original Text (descriptive): 'The sun set over the horizon, casting a warm orange glow over the tranquil sea. Seagulls flew overhead, their cries echoing in the gentle evening breeze.'
Transformed Text (poetic): 'As the sun dipped below the horizon, an amber glow embraced the serene sea. Overhead, seagulls' cries mingled with the whisper of the evening breeze.'"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The transformed text should preserve the original meaning.",
            "The transformed text should be coherent and stylistically consistent with the target style.",
            "The transformed text should be well-organized and free of grammatical errors.",
            "The transformed text should capture the essence of the original text in the new style.",
            "The transformed text should not mirror the example." 
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
