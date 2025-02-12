class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"source_lang": "English", "target_lang": "Spanish", "text": "This is a sample text to be translated and reformatted. Testing complex translations can be challenging.", "format": "ALL CAPS"},
            "2": {"source_lang": "French", "target_lang": "German", "text": "Ceci est un texte d'exemple à traduire et à reformater. Tester des traductions complexes peut être difficile.", "format": "Title Case"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Translate the following text from {t['source_lang']} to {t['target_lang']} and then reformat it as specified.

Text: {t['text']}

Reformatting: {t['format']}

Expected response format:
[Translated and reformatted text]

Example:
If the source text is 'Hello, world!', translated to Spanish and reformatted as ALL CAPS, the response should be '¡HOLA, MUNDO!'

Ensure the translation is accurate and the reformatting follows the specified guidelines."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0
