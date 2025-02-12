import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'emotion': 'conflicted optimism',
                'context': 'receiving a job offer in a new city',
                'culture': 'Western'
            },
            {
                'emotion': 'bittersweet nostalgia',
                'context': 'looking through old family photos',
                'culture': 'East Asian'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze and generate an emoji sequence to convey the complex emotional state of '{t['emotion']}' in the context of {t['context']}, considering the {t['culture']} cultural perspective. Your task has the following components:

1. Emoji Sequence:
   Create a sequence of 5-10 standard Unicode emojis that effectively communicates the given emotion and context. Present this sequence on a separate line before your analysis.

2. Analysis (250-300 words):
   a) Explain how each emoji in your sequence contributes to expressing the complex emotion.
   b) Discuss how the order and combination of emojis enhance the overall emotional message.
   c) Analyze how cultural context influences the interpretation of your emoji sequence.

3. Alternative Interpretation (150-200 words):
   Propose how your emoji sequence might be interpreted differently in a contrasting culture. Explain the reasons for these potential differences.

4. Emotional AI Application (200-250 words):
   Describe how an AI system could be designed to interpret and generate such complex emoji-based emotional expressions. Discuss potential challenges and benefits of such a system.

Ensure your response demonstrates a deep understanding of emotional nuances, cultural differences in communication, and the potential of emojis as a form of emotional expression. Be creative in your emoji usage while maintaining coherence and relevance to the given emotion and context."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The emoji sequence effectively conveys the emotion of {t['emotion']} in the context of {t['context']}.",
            "The analysis provides insightful explanations for each emoji's contribution to the overall emotional message.",
            f"The response demonstrates an understanding of {t['culture']} cultural perspective in emoji interpretation.",
            "The alternative interpretation shows a nuanced understanding of cross-cultural communication differences.",
            "The emotional AI application proposal is innovative and addresses relevant challenges and benefits.",
            "The response follows the specified format, including presenting the emoji sequence separately."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
