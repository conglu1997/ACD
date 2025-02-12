import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'language_pair': ('Japanese', 'English'),
                'emotion': 'Amae (甘え)',
                'context': 'Family relationships'
            },
            {
                'language_pair': ('Spanish', 'Mandarin Chinese'),
                'emotion': 'Saudade (Portuguese)',
                'context': 'Long-distance friendships'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a multi-lingual, culturally-aware AI system for detecting and analyzing emotions in text, focusing on the following specifications:

Language Pair: {t['language_pair'][0]} and {t['language_pair'][1]}
Emotion to Analyze: {t['emotion']}
Context: {t['context']}

Your task:
1. Briefly explain the given emotion and its cultural significance (2-3 sentences).
2. Design an AI system that can detect and analyze this emotion in both languages of the given pair. Describe its key components and functioning (4-5 sentences). Include details on:
   a) Natural Language Processing techniques used
   b) Cultural knowledge integration method
   c) Emotion classification approach
3. Provide two specific examples of how your system would process and interpret emotional expressions in each language (2 examples per language).
4. Discuss how your system would handle idiomatic expressions or cultural-specific phrases related to the emotion (2-3 sentences).
5. Analyze how this system could improve cross-cultural understanding and communication (3-4 sentences).
6. Propose a novel metric for quantifying the accuracy of emotion detection across cultures (2-3 sentences).
7. Discuss potential challenges in implementing this system and how they might be addressed (2-3 sentences).
8. Explore the ethical implications of using such a system in AI-mediated communication (3-4 sentences).

Format your response as follows:

Emotion Explanation:
[Your explanation of the emotion and its cultural significance]

AI System Design:
[Your description of the AI system]

Processing Examples:
1. {t['language_pair'][0]}: [First example]
2. {t['language_pair'][0]}: [Second example]
3. {t['language_pair'][1]}: [First example]
4. {t['language_pair'][1]}: [Second example]

Handling Idiomatic Expressions:
[Your discussion on handling culture-specific phrases]

Cross-cultural Impact Analysis:
[Your analysis of potential improvements in understanding and communication]

Novel Accuracy Metric:
[Your proposed metric for quantifying emotion detection accuracy]

Implementation Challenges:
[Your discussion of challenges and potential solutions]

Ethical Implications:
[Your exploration of ethical considerations]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The explanation of the emotion and its cultural significance is accurate and insightful.",
            "The AI system design incorporates linguistic and cultural aspects in a sophisticated manner, with clear details on NLP techniques, cultural knowledge integration, and emotion classification.",
            "The processing examples demonstrate a nuanced understanding of emotional expressions in both languages.",
            "The discussion on handling idiomatic expressions shows depth in cultural understanding.",
            "The cross-cultural impact analysis is well-reasoned and considers multiple perspectives.",
            "The proposed accuracy metric is innovative and relevant to cross-cultural emotion detection.",
            "The discussion of implementation challenges and solutions is practical and innovative.",
            "The exploration of ethical implications is thorough and considers potential misuse or misinterpretation.",
            "The overall response demonstrates a deep understanding of emotions, cultural linguistics, and AI capabilities."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
