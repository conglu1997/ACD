class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"text": "The quick brown fox jumps over the lazy dog.", "languages": ["Spanish", "French"]},
            "2": {"text": "To be or not to be, that is the question.", "languages": ["German", "Italian"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to translate the following text into the specified languages and then synthesize a new sentence based on the translated versions.

Text: {t["text"]}
Languages: {', '.join(t["languages"])}

Instructions:
1. Translate the text into each of the specified languages. Ensure the translations are contextually appropriate.
2. Create a new sentence that combines key elements from each translated version. The new sentence should make coherent sense in English.
3. Provide the translations and the synthesized sentence in the following format:

Original Text: {t["text"]}
Translations: [language1]: [translation1], [language2]: [translation2]
Synthesized Sentence: [your new sentence]

Example:
Original Text: "The quick brown fox jumps over the lazy dog."
Translations: Spanish: "El rápido zorro marrón salta sobre el perro perezoso.", French: "Le rapide renard brun saute par-dessus le chien paresseux."
Synthesized Sentence: "The quick brown fox jumps over the lazy dog in a swift manner."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The translations should accurately and contextually convey the meaning of the original text.",
            "The synthesized sentence should incorporate key elements from each translated version and make coherent sense in English.",
            "The response should maintain the specified format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
