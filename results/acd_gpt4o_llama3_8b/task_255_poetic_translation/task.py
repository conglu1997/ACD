class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "original_poem": "En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero, adarga antigua, rocín flaco y galgo corredor.",
                "source_language": "Spanish",
                "target_language": "English"
            },
            "2": {
                "original_poem": "Sous le pont Mirabeau coule la Seine, et nos amours, faut-il qu'il m'en souvienne, la joie venait toujours après la peine.",
                "source_language": "French",
                "target_language": "English"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Translate the following poem from {t['source_language']} to {t['target_language']}. Ensure that the translation preserves the original meaning, tone, and artistic elements of the poem.

Original Poem:
{t['original_poem']}

Submit your translation as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = ["The translation should preserve the original meaning of the poem.", "The translation should maintain the tone and artistic elements of the original poem.", "The translation should be coherent and fluent in the target language."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
