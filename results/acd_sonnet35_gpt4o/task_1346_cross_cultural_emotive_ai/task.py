class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "source_culture": "Japanese",
                "target_culture": "Brazilian",
                "emotion": "Gratitude",
                "context": "Professional setting"
            },
            "2": {
                "source_culture": "Bedouin",
                "target_culture": "Finnish",
                "emotion": "Grief",
                "context": "Family gathering"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of analyzing and generating culturally-appropriate emotional expressions in text and non-verbal cues, then apply it to the following scenario:

Source Culture: {t['source_culture']}
Target Culture: {t['target_culture']}
Emotion to Express: {t['emotion']}
Context: {t['context']}

Your task has the following parts:

1. Emotional Expression Analysis Framework (200-250 words):
   a) Explain the cognitive and linguistic processes involved in understanding and expressing emotions across cultures.
   b) Describe how your AI system would implement these processes.
   c) Discuss how emotional expressions differ between {t['source_culture']} and {t['target_culture']} cultures, considering linguistic, cultural, and non-verbal factors.
   d) Provide at least one concrete example of how the given emotion is typically expressed in each culture.

2. AI System Architecture (200-250 words):
   a) Provide a high-level overview of your AI system's architecture.
   b) Detail the components for natural language processing, cultural knowledge representation, emotional content analysis, and non-verbal cue interpretation.
   c) Explain how the system handles context-dependent emotional expressions and cultural nuances.

3. Application to the Given Scenario (250-300 words):
   a) Generate a culturally appropriate emotional expression in the target culture that conveys the given emotion within the specified context. Include both verbal and non-verbal aspects.
   b) Provide a detailed explanation of the generated expression, including its cultural significance and potential variations.
   c) Describe the system's process for creating this expression, including any challenges encountered.
   d) Provide an example of a similar emotional expression in the source culture and explain how it differs, considering both verbal and non-verbal elements.

4. Emotion Recognition and Interpretation (150-200 words):
   a) Describe how your AI system would recognize and interpret emotional expressions from the source culture, including both verbal and non-verbal cues.
   b) Address potential challenges in cultural and linguistic differences in emotion recognition.
   c) Provide an example of a difficult-to-translate emotional expression from the source culture and explain how your system would handle it.

5. Evaluation and Refinement (150-200 words):
   a) Propose a method for evaluating the appropriateness and effectiveness of the generated emotional expressions, including both verbal and non-verbal aspects.
   b) Describe how your AI system would improve its process based on feedback from native speakers and cultural experts.
   c) Suggest a specific metric for measuring the system's performance in cross-cultural emotional expression generation and interpretation.

6. Ethical and Societal Implications (100-150 words):
   a) Discuss potential ethical implications and societal impacts of an AI system capable of generating and interpreting cross-cultural emotional expressions.
   b) Address the importance of emotional authenticity and cultural sensitivity in this process.
   c) Consider potential misuse or misinterpretation of such a system and propose safeguards.

Ensure your response demonstrates a deep understanding of cognitive science, linguistics, cultural studies, and AI system design. Be creative and innovative while maintaining scientific rigor and cultural sensitivity. Your total response should be between 1050-1350 words.

Format your response with clear headings for each section (e.g., '1. Emotional Expression Analysis Framework:', '2. AI System Architecture:', etc.). Use appropriate subheadings where necessary to organize your thoughts clearly. Provide concrete examples and specific details throughout your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response provides a comprehensive and scientifically sound framework for analyzing emotional expressions across cultures, including specific differences between the source and target cultures, with concrete examples for each.",
            "The AI system architecture is well-designed and addresses the complexities of cross-cultural emotional expression generation and interpretation, including both verbal and non-verbal aspects, with clear explanations of how it handles context and cultural nuances.",
            "The generated emotional expression for the given scenario is culturally appropriate, linguistically accurate, and effectively conveys the intended emotion within the specified context, including both verbal and non-verbal elements. A relevant example from the source culture is also provided and compared.",
            "The approach to emotion recognition and interpretation demonstrates a nuanced understanding of the challenges in cross-cultural communication, including a specific example of a difficult-to-translate emotional expression, addressing both verbal and non-verbal aspects.",
            "The proposed evaluation method and refinement process are robust and likely to improve the system's performance, with a specific metric suggested for measuring cross-cultural emotional expression generation and interpretation.",
            "The discussion of ethical and societal implications is thoughtful and considers multiple perspectives, including the importance of emotional authenticity and cultural sensitivity, with proposed safeguards against misuse.",
            "The overall response demonstrates creativity, interdisciplinary knowledge, and a deep understanding of the complexities involved in cross-cultural emotional AI systems, including both verbal and non-verbal aspects of communication.",
            "The response follows the specified format with clear headings and appropriate organization, addressing all sub-points in each section, and provides concrete examples and specific details throughout."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
