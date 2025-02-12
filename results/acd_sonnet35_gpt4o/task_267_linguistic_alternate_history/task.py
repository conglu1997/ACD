import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                'event': 'The Norman Conquest of England in 1066',
                'language': 'Old English',
                'linguistic_feature': 'case system',
                'alteration': 'Old English had lost its case system entirely before 1066'
            },
            {
                'event': 'The signing of the Treaty of Versailles in 1919',
                'language': 'French',
                'linguistic_feature': 'grammatical gender',
                'alteration': 'French had no grammatical gender'
            },
            {
                'event': 'The Cuban Missile Crisis in 1962',
                'language': 'Russian',
                'linguistic_feature': 'aspect in verbs',
                'alteration': 'Russian lacked the perfective/imperfective aspect distinction'
            },
            {
                'event': 'The formation of the European Union in 1993',
                'language': 'German',
                'linguistic_feature': 'compound words',
                'alteration': 'German did not allow the formation of compound words'
            }
        ]
        
        return {str(i+1): random.choice(scenarios) for i in range(2)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze how {t['event']} might have unfolded differently if the following linguistic alteration had occurred: {t['alteration']}.

Your response should include:

1. Brief explanation (2-3 sentences) of the original linguistic feature and its significance in {t['language']}.

2. Analysis (100-150 words) of how the altered linguistic feature might have affected communication, negotiation, or cultural understanding during the historical event.

3. A short alternate history narrative (150-200 words) describing how the event might have played out differently due to this linguistic change. Be creative but ensure your narrative is grounded in historical context and linguistic principles.

4. Reflection (2-3 sentences) on how this linguistic alteration might have affected the long-term cultural or political landscape following the event.

Ensure your response demonstrates a deep understanding of both the linguistic concepts and the historical context. Use your imagination to create a plausible and interesting alternate history scenario."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The explanation of the original linguistic feature in {t['language']} is accurate and clear.",
            "The analysis of the linguistic alteration's potential effects is thoughtful and well-reasoned.",
            "The alternate history narrative is creative, coherent, and grounded in both linguistic and historical knowledge.",
            "The reflection on long-term effects demonstrates an understanding of the interconnectedness of language, culture, and history.",
            "The overall response shows a deep understanding of linguistic principles and their potential impact on historical events."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
