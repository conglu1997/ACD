import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'event': 'The invention of the printing press in 15th century Europe',
                'alternative': 'The printing press is invented in China during the Song Dynasty (960-1279 CE)',
                'domains': ['technology', 'culture', 'politics']
            },
            {
                'event': 'The American Revolution (1765-1783)',
                'alternative': 'The American colonies remain under British rule',
                'domains': ['politics', 'economics', 'social structures']
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the following historical event and its alternative outcome:

Original Event: {t['event']}
Alternative Scenario: {t['alternative']}

Your task is to:

1. Briefly describe the actual historical outcome and its major consequences (100-150 words).

2. Explore the alternative scenario, considering its immediate effects and long-term consequences across three time periods: short-term (0-50 years), medium-term (50-200 years), and long-term (200+ years). Focus on the following domains: {', '.join(t['domains'])}. (400-500 words)

3. Compare and contrast the actual and alternative timelines, highlighting key divergences and potential similarities. (150-200 words)

4. Propose one unexpected or counterintuitive outcome of the alternative scenario and explain your reasoning. (100-150 words)

Ensure your analysis is grounded in historical facts and plausible causality. Be creative in your alternative history, but maintain logical consistency. Use specific examples and avoid broad generalizations.

Format your response with clear headings for each section, and include the word count for each section in parentheses at the end. Your total response should be between 750-1000 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response follows the required format, including word counts for each section, and adheres to the overall word count guidelines.",
            "The analysis demonstrates a strong understanding of the historical event and its consequences, supported by specific examples.",
            "The alternative scenario is explored creatively yet plausibly across the specified time periods and domains, showing a clear cause-and-effect relationship.",
            "The comparison between actual and alternative timelines is insightful, well-reasoned, and highlights significant divergences and similarities.",
            "The unexpected outcome is truly counterintuitive, supported by logical reasoning, and demonstrates creative thinking.",
            "The overall response shows depth of historical knowledge, interdisciplinary analysis, and adherence to the principles of alternative history."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
