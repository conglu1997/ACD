import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        pivotal_moments = [
            {
                'event': 'Industrial Revolution',
                'period': '18th-19th century',
                'key_aspect': 'Technological advancement'
            },
            {
                'event': 'French Revolution',
                'period': '1789-1799',
                'key_aspect': 'Political upheaval'
            },
            {
                'event': 'World War II',
                'period': '1939-1945',
                'key_aspect': 'Global conflict'
            },
            {
                'event': 'Moon Landing',
                'period': '1969',
                'key_aspect': 'Space exploration'
            }
        ]
        return {str(i+1): moment for i, moment in enumerate(random.sample(pivotal_moments, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create and analyze an alternative historical timeline based on a significant change to the {t['event']} ({t['period']}), focusing on the aspect of {t['key_aspect']}. Then, evaluate the ethical implications of this change. Your task has four parts:

1. Historical Alteration (150-200 words):
   a) Briefly describe the actual historical event and its significance.
   b) Propose a plausible and significant alteration to this event.
   c) Explain how this change could have occurred and its immediate consequences.

2. Alternative Timeline (250-300 words):
   a) Describe how history might have unfolded differently over the next 50-100 years due to your proposed change.
   b) Focus on major global developments in politics, technology, society, and culture.
   c) Highlight at least three specific events or trends that would be significantly different in this timeline.

3. Comparative Analysis (200-250 words):
   a) Compare and contrast your alternative timeline with actual history.
   b) Analyze the long-term implications of the changes, considering both positive and negative outcomes.
   c) Discuss how this alternative history might have affected the present day (assume the present is 2023).

4. Ethical Evaluation (200-250 words):
   a) Identify and explain at least three major ethical issues arising from your alternative timeline.
   b) Discuss the moral implications of the historical change itself.
   c) Evaluate whether this alternative timeline would be ethically preferable to actual history, considering utilitarian and deontological perspectives.

Ensure your response demonstrates a deep understanding of historical events, cause-and-effect relationships, and ethical reasoning. Be creative in your alternate history while maintaining plausibility and internal consistency. Use appropriate historical terminology and provide clear explanations for your ethical judgments.

Format your response with clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately describes the {t['event']} and proposes a plausible alteration.",
            "The alternative timeline is creative, internally consistent, and considers multiple aspects of historical development.",
            "The comparative analysis demonstrates a strong understanding of cause-and-effect relationships in history.",
            "The ethical evaluation identifies relevant moral issues and considers multiple ethical perspectives.",
            "The response is well-structured, using clear headings for each section as specified.",
            "The writing demonstrates a high level of historical knowledge, creative thinking, and ethical reasoning."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
