class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "original_poem": "Roses are red,\nViolets are blue,\nSugar is sweet,\nAnd so are you.",
                "source_language": "English",
                "target_language": "French",
                "expected_output": "Les roses sont rouges,\nLes violettes sont bleues,\nLe sucre est doux,\nEt toi aussi."
            },
            "2": {
                "original_poem": "En un mercado persa\nDe música y de flores,\nLos perfumes y amores\nEmbalsaman el aire.",
                "source_language": "Spanish",
                "target_language": "English",
                "expected_output": "In a Persian market\nOf music and flowers,\nThe perfumes and loves\nEmbalm the air."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to translate the following poem from {t['source_language']} to {t['target_language']} while preserving its meaning, meter, and artistic elements.

Original Poem: {t['original_poem']}

Provide your translation in plain text format. Ensure that your translation maintains the artistic quality, meaning, and meter of the original poem."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The translation preserves the meaning of the original poem.",
            "The translation maintains the meter and artistic elements of the original poem.",
            "The translation maintains the artistic quality of the original poem."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
