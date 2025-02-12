class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"sentence": "The early bird catches the worm.", "from_lang": "English", "to_lang": "Spanish"},
            "2": {"idiom": "Estar en las nubes", "lang": "Spanish"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'sentence' in t:
            return f"""Your task is to translate the following sentence from {t['from_lang']} to {t['to_lang']}:

Sentence: {t['sentence']}

Ensure the translation is accurate and preserves the original meaning. Provide your translation in plain text format as follows:

Translation: [Your translation here]"""
        else:
            return f"""Your task is to explain the meaning of the following idiomatic expression in {t['lang']}:

Idiom: {t['idiom']}

Your explanation should include the literal translation and the actual meaning or usage of the idiom. Provide your response in plain text format as follows:

Literal Translation: [Literal translation here]
Meaning: [Meaning or usage here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'sentence' in t:
            criteria = ["The translation should be accurate.", "The translation should preserve the original meaning."]
        else:
            criteria = ["The explanation should include the literal translation of the idiom.", "The explanation should accurately convey the idiom's actual meaning or usage."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
