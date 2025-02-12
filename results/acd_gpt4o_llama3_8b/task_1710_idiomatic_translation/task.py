class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "source_language": "English",
                "target_language": "Spanish",
                "idiom": "It's raining cats and dogs",
                "context": "The idiom is used to describe very heavy rainfall."
            },
            "2": {
                "source_language": "French",
                "target_language": "English",
                "idiom": "Coûter les yeux de la tête",
                "context": "The idiom is used to describe something very expensive. Literally, it means 'to cost the eyes from the head'."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Translate the following idiomatic expression from {t['source_language']} to {t['target_language']} while maintaining its meaning and context:

Idiom: {t['idiom']}

Context: {t['context']}

Ensure that your translation accurately reflects the idiomatic meaning in the target language, not just a literal translation. Cultural appropriateness and idiomatic accuracy are crucial.

Submit your translation as a plain text string.

Example 1:
Idiom in English: 'Kick the bucket'
Target Language: Spanish
Translation: 'Estirar la pata'
(This example shows an English idiom translated into a Spanish idiom that conveys the same meaning, which is 'to die'.)

Example 2:
Idiom in Japanese: '猿も木から落ちる'
Target Language: English
Translation: 'Even monkeys fall from trees'
(This example shows a Japanese idiom translated into an English idiom that conveys the same meaning, which is 'Everyone makes mistakes'.)

Avoid literal translations and focus on conveying the idiomatic meaning."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0
