import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        expressions = [
            {"language": "English", "expression": "It's raining cats and dogs", "meaning": "It's raining very heavily"},
            {"language": "French", "expression": "Avoir le cafard", "meaning": "To feel down or depressed"},
            {"language": "Japanese", "expression": "猫の手も借りたい", "meaning": "To be extremely busy"},
            {"language": "Spanish", "expression": "Estar como pez en el agua", "meaning": "To feel completely comfortable or at ease"},
            {"language": "German", "expression": "Ich verstehe nur Bahnhof", "meaning": "I don't understand anything"}
        ]
        target_languages = ["English", "French", "Japanese", "Spanish", "German"]
        
        tasks = {}
        for i in range(1, 3):
            source = random.choice(expressions)
            target = random.choice([lang for lang in target_languages if lang != source["language"]])
            tasks[str(i)] = {"source": source, "target": target}
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Translate the {t['source']['language']} idiomatic expression '{t['source']['expression']}' (which means '{t['source']['meaning']}') into {t['target']}. Your translation should preserve the cultural essence and meaning of the original expression while adapting it to be culturally relevant and natural-sounding in the target language. Provide your response in the following format:\n\nTranslation: [Your translated expression in {t['target']}]\n\nExplanation: [Explain how your translation preserves the meaning and cultural essence of the original expression, and how it is adapted to be culturally relevant in the target language]"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The translation preserves the meaning of the original expression",
            "The translation is culturally relevant and natural-sounding in the target language",
            "The explanation clearly articulates how the translation preserves meaning and cultural essence",
            "The response demonstrates creativity and linguistic adaptability"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
