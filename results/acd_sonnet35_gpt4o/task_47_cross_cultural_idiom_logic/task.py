import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'source_language': 'Spanish',
                'target_language': 'English',
                'idiom': 'Estar en las nubes',
                'literal_translation': 'To be in the clouds',
                'meaning': 'To be distracted or not paying attention',
                'logical_operation': 'negate'
            },
            {
                'source_language': 'Japanese',
                'target_language': 'English',
                'idiom': '猫の手も借りたい',
                'literal_translation': 'Want to borrow even a cat\'s paws',
                'meaning': 'To be extremely busy',
                'logical_operation': 'intensify'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are given an idiomatic expression from {t['source_language']}. Your task is to interpret, translate, and logically transform this expression.

1. Idiom: {t['idiom']}
   Literal translation: {t['literal_translation']}
   Meaning: {t['meaning']}

2. Translate the meaning of this idiom into an equivalent {t['target_language']} expression. This doesn't have to be an existing idiom, but it should convey the same meaning in a culturally appropriate way for {t['target_language']} speakers.

3. Apply the logical operation '{t['logical_operation']}' to the meaning of the original idiom. Then, create a new expression in {t['target_language']} that reflects this logically transformed meaning. Ensure that your new expression is creative and culturally sensitive.

4. Explain the logical transformation you applied and how your new expression reflects this change in meaning.

Provide your response in the following format:

Equivalent expression: [Your translation]
Logically transformed expression: [Your new expression]
Explanation: [Your explanation]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The equivalent expression accurately conveys the meaning of the original idiom in {t['target_language']}.",
            f"The logically transformed expression correctly applies the '{t['logical_operation']}' operation to the original meaning.",
            "The new expressions are creative and culturally appropriate.",
            "The explanation clearly describes the logical transformation and how it's reflected in the new expression."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
