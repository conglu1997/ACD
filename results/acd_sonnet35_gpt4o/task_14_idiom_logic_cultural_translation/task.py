import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        idioms = [
            "It's raining cats and dogs",
            "The early bird catches the worm",
            "Don't put all your eggs in one basket",
            "You can't have your cake and eat it too",
            "When pigs fly"
        ]
        logical_ops = ["NOT", "AND", "OR", "IF...THEN"]
        target_cultures = ["Japanese", "Russian", "Arabic", "Swahili", "Hindi"]
        
        return {
            "1": {
                "idiom": random.choice(idioms),
                "logical_op": random.choice(logical_ops),
                "target_culture": random.choice(target_cultures)
            },
            "2": {
                "idiom": random.choice(idioms),
                "logical_op": random.choice(logical_ops),
                "target_culture": random.choice(target_cultures)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"This task involves transforming an English idiom using a logical operation and then creating a culturally appropriate equivalent in another language. Follow these steps:\n\n1. Transform the English idiom '{t['idiom']}' using the logical operation '{t['logical_op']}'.\n2. Explain the meaning of your transformed idiom in 1-2 sentences.\n3. Create a new idiom in the {t['target_culture']} culture that conveys the same meaning as your transformed idiom. If you don't know the target language, create the idiom in English but ensure it reflects the values, customs, or environment of the target culture.\n4. Explain how your new idiom captures the essence of the transformed idiom and how it relates to the target culture.\n\nProvide your response in the following format:\nTransformed idiom: [Your transformed idiom]\nMeaning: [Explanation of the transformed idiom's meaning]\nNew {t['target_culture']} idiom: [Your new idiom]\nExplanation: [Your explanation]"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The transformed idiom correctly applies the given logical operation to the original idiom.",
            "The explanation of the transformed idiom's meaning is clear and accurate.",
            "The new idiom in the target culture conveys the same meaning as the transformed idiom.",
            "The new idiom reflects the values, customs, or environment of the target culture.",
            "The explanation clearly articulates how the new idiom relates to both the transformed idiom and the target culture."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
