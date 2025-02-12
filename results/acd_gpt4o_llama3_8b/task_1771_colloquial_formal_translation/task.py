class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {'criteria': 'Translate the following colloquial expression into formal language: "Gonna grab some grub".'},
            '2': {'criteria': 'Translate the following formal sentence into colloquial language: "He expressed his dissatisfaction with the service provided."'}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Translate the given expression based on the following criteria: {t['criteria']}\nEnsure that the translation maintains the original meaning while accurately reflecting the target language register. The translation should be coherent, natural-sounding, and contextually appropriate. Submit your translation as a plain text string."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The translation should maintain the original meaning.", "The translation should be in the correct language register (colloquial or formal).", "The translation should be coherent, natural-sounding, and contextually appropriate."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
