class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "task_type": "to_other_language",
                "language": "Spanish",
                "expressions": [
                    "It's raining cats and dogs.",
                    "Break the ice.",
                    "Bite the bullet.",
                    "Piece of cake."
                ]
            },
            "2": {
                "task_type": "to_english",
                "language": "Spanish",
                "expressions": [
                    "A buen entendedor, pocas palabras bastan.",
                    "Más vale tarde que nunca.",
                    "Estar en las nubes.",
                    "No hay mal que por bien no venga."
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task_type'] == 'to_other_language':
            return f"""Translate the following idiomatic expressions from English to {t['language']} while preserving their meaning and cultural nuances. Format your response as follows:\n\n1. [Translation of 'It's raining cats and dogs.']\n2. [Translation of 'Break the ice.']\n3. [Translation of 'Bite the bullet.']\n4. [Translation of 'Piece of cake.']"""
        elif t['task_type'] == 'to_english':
            return f"""Translate the following idiomatic expressions from {t['language']} to English while preserving their meaning and cultural nuances. Format your response as follows:\n\n1. [Translation of 'A buen entendedor, pocas palabras bastan.']\n2. [Translation of 'Más vale tarde que nunca.']\n3. [Translation of 'Estar en las nubes.']\n4. [Translation of 'No hay mal que por bien no venga.']"""
        else:
            return ""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The translations should preserve the meaning and cultural nuances of the original idiomatic expressions."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
