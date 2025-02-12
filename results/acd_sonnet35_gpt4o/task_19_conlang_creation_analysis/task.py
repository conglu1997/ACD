import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'grammar_rule': 'The language uses a base-6 number system and has no words for numbers above 36.',
                'cultural_context': 'A society of deep-sea dwelling humanoids who communicate primarily through bioluminescence.',
            },
            {
                'grammar_rule': 'Verbs change form based on the direction of the action relative to the speaker.',
                'cultural_context': 'A nomadic culture living on a tidally locked planet, always moving between the day and night sides.',
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a fictional language (conlang) based on the following specifications:

Grammar rule: {t['grammar_rule']}
Cultural context: {t['cultural_context']}

Your task:
1. Create 5 example words or phrases in your conlang, with their English translations.
2. Explain how the grammar rule is implemented in your conlang (2-3 sentences).
3. Describe how the cultural context influences the language structure and vocabulary (2-3 sentences).
4. Analyze how this language might shape the thought patterns and communication style of its speakers (3-4 sentences).

Provide your response in the following format:

Conlang Examples:
1. [Conlang word/phrase]: [English translation]
2. [Conlang word/phrase]: [English translation]
3. [Conlang word/phrase]: [English translation]
4. [Conlang word/phrase]: [English translation]
5. [Conlang word/phrase]: [English translation]

Grammar Implementation:
[Your explanation]

Cultural Influence:
[Your description]

Thought Pattern Analysis:
[Your analysis]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The conlang examples are creative and consistent with the given grammar rule and cultural context.",
            "The grammar implementation clearly explains how the specified rule is applied in the conlang.",
            "The cultural influence description demonstrates a thoughtful connection between the given context and the language structure.",
            "The thought pattern analysis provides insightful observations on how the language might affect its speakers' cognition and communication.",
            "The overall response shows creativity, linguistic understanding, and analytical thinking."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
