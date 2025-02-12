import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'source_culture': 'Japanese',
                'idiom': '猫の手も借りたい (neko no te mo karitai)',
                'literal_translation': 'I want to borrow even a cat\'s paws',
                'target_culture': 'Underwater civilization'
            },
            {
                'source_culture': 'Russian',
                'idiom': 'Когда рак на горе свистнет (Kogda rak na gore svistnet)',
                'literal_translation': 'When a lobster whistles on a mountain',
                'target_culture': 'Desert nomads'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the given idiom from {t['source_culture']} culture and create a new idiom for a fictional {t['target_culture']}. Follow these steps:

1. Idiom Analysis (150-200 words):
   a) Explain the meaning of the idiom: "{t['idiom']}" (literal translation: "{t['literal_translation']}").
   b) Discuss its cultural significance and usage in {t['source_culture']} society.
   c) Analyze the linguistic devices used (e.g., metaphor, alliteration) and their effectiveness.

2. Cross-Cultural Comparison (100-150 words):
   a) Compare this idiom to similar expressions in other cultures.
   b) Discuss how the concept might be expressed differently in various cultural contexts.

3. Fictional Culture Development (150-200 words):
   a) Describe key aspects of the fictional {t['target_culture']}, including their environment, social structure, and values.
   b) Explain how these cultural elements might influence their language and expressions.

4. New Idiom Creation (150-200 words):
   a) Propose a new idiom that could exist in the {t['target_culture']}.
   b) Provide its literal translation and explain its figurative meaning.
   c) Justify how this idiom reflects the fictional culture's characteristics.

5. Linguistic Analysis of New Idiom (100-150 words):
   a) Analyze the linguistic devices used in your created idiom.
   b) Explain how these devices contribute to the idiom's effectiveness and memorability.

6. Comparative Reflection (100-150 words):
   a) Compare your created idiom to the original {t['source_culture']} idiom.
   b) Discuss how cultural differences are reflected in these expressions.

Ensure your response demonstrates a deep understanding of linguistic principles, cultural analysis, and creative writing. Use appropriate terminology and provide clear explanations. Be creative in developing the fictional culture and new idiom while maintaining logical consistency.

Format your response with clear headings for each section and subsections labeled a, b, c as appropriate. Your total response should be between 750-1050 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately analyzes the {t['source_culture']} idiom and its cultural significance.",
            f"The fictional {t['target_culture']} is well-developed and logically consistent.",
            "The newly created idiom is creative, culturally appropriate, and linguistically interesting.",
            "The analysis demonstrates a strong understanding of linguistic principles and cultural dynamics.",
            "The response follows the specified structure and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
