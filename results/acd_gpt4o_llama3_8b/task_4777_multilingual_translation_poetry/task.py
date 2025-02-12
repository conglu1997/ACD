class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"text": "The beauty of the setting sun paints the sky in hues of orange and pink.", "languages": ["Spanish", "French", "English"]},
            "2": {"text": "The gentle breeze whispers secrets of the ancient forest.", "languages": ["German", "Italian", "English"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following task based on the given instructions:

1. Translate the following text into the specified languages in the given order: {', '.join(t['languages'])}.
2. Based on the final translated text, create a poem that captures the essence of the original message in the final language.

Text: {t['text']}

Ensure your poem is engaging, well-structured, and creative. Submit your response as a plain text string in the following format:

Translations: [Translation 1] -> [Translation 2] -> [Final Translation]
Poem: [Your poem here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The translations should follow the specified language order.", "The poem should be based on the final translated text and capture the essence of the original message.", "The poem should be engaging, well-structured, and creative."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
