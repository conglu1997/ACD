class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"source_language": "English", "target_language": "Spanish", "text": "John was as busy as a bee, running around like a chicken with its head cut off, trying to get everything ready for the big wedding."},
            "2": {"source_language": "English", "target_language": "Japanese", "text": "The early bird catches the worm, but the second mouse gets the cheese."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Translate the following text from {t['source_language']} into {t['target_language']}, and adapt any cultural references to make sense for the target audience. Ensure the translation is accurate, natural, and culturally appropriate. Pay special attention to idiomatic expressions and adapt them to equivalent expressions in the target language. Here is the text:

'{t['text']}'

Submit your translated and adapted text as a plain text string in the following format:
Translation: [Your translated text here]

Example:
If you were translating the phrase 'It's raining cats and dogs' from English to Spanish, you might adapt it to 'Está lloviendo a cántaros', which is an equivalent idiomatic expression in Spanish."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The translation should be accurate and natural.",
            "Idiomatic expressions should be adapted to equivalent expressions in the target language.",
            "Cultural references should be appropriately adapted for the target audience.",
            "The overall text should be culturally appropriate and make sense in the target language."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
