class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "emotion": "Schadenfreude",
                "source_culture": "German",
                "target_culture": "Japanese",
                "context": "Business negotiation"
            },
            "2": {
                "emotion": "Saudade",
                "source_culture": "Portuguese",
                "target_culture": "American",
                "context": "Social media interaction"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that translates complex emotional expressions across cultures, accounting for linguistic, contextual, and non-verbal cues. Then, apply your system to analyze and mediate cross-cultural communications. Focus on translating the emotion of {t['emotion']} from {t['source_culture']} culture to {t['target_culture']} culture in the context of a {t['context']}. Your response should include the following sections:

1. AI System Architecture (300-350 words):
   a) Describe the key components of your AI system for emotion translation.
   b) Explain how your system integrates linguistic analysis, cultural knowledge, and emotional intelligence.
   c) Detail how the system processes verbal and non-verbal cues to understand and translate emotions.
   d) Propose a novel algorithm for mapping emotions across cultural contexts.
   e) Include a high-level diagram or pseudocode representing the system's architecture (describe it textually).

2. Emotion Translation Process (250-300 words):
   a) Explain how your AI system would translate {t['emotion']} from {t['source_culture']} to {t['target_culture']} culture.
   b) Describe the challenges in conveying this emotion across these specific cultures.
   c) Discuss how your system accounts for the context of {t['context']}.
   d) Provide an example of how the emotion might be expressed in each culture, including verbal and non-verbal elements.

3. Cultural-Linguistic Analysis (200-250 words):
   a) Analyze the cultural and linguistic factors that influence the expression and interpretation of {t['emotion']} in both cultures.
   b) Discuss how your system addresses potential misunderstandings or misinterpretations.
   c) Explain how your AI adapts to subtle cultural nuances and context-specific emotional expressions.

4. Application in Cross-Cultural Communication (250-300 words):
   a) Describe a scenario in {t['context']} where your AI system mediates a communication involving {t['emotion']}.
   b) Explain how your system would facilitate understanding between parties from {t['source_culture']} and {t['target_culture']} cultures.
   c) Discuss potential challenges and how your system overcomes them.
   d) Provide an example dialogue or interaction, showing your system's translation and mediation process.

5. Ethical Considerations and Limitations (200-250 words):
   a) Identify potential ethical concerns related to AI-mediated emotional and cultural translation.
   b) Discuss the implications for privacy, cultural preservation, and authentic human interaction.
   c) Address the limitations of your approach and potential risks of misuse or misinterpretation.
   d) Propose guidelines for the responsible development and use of emotion-translating AI systems.

6. Evaluation and Future Directions (150-200 words):
   a) Propose methods to evaluate the accuracy and effectiveness of your emotion translation system.
   b) Suggest potential improvements or extensions to your system.
   c) Discuss how this technology could be applied to other areas of cross-cultural communication or emotional intelligence research.

Ensure your response demonstrates a deep understanding of emotional intelligence, cultural anthropology, linguistics, and artificial intelligence. Use appropriate terminology from all relevant fields and provide clear explanations where necessary. Be creative and innovative in your approach while maintaining scientific plausibility and cultural sensitivity.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of emotional intelligence, cultural anthropology, linguistics, and artificial intelligence.",
            "The AI system architecture is well-explained and scientifically plausible.",
            "The emotion translation process effectively addresses the specific emotion, cultures, and context provided.",
            "The cultural-linguistic analysis shows insight into the nuances of emotional expression across cultures.",
            "The application in cross-cultural communication is practical and well-illustrated.",
            "Ethical considerations and limitations are thoughtfully addressed.",
            "The evaluation methods and future directions are insightful and demonstrate critical thinking.",
            "The overall approach is creative and innovative while maintaining cultural sensitivity and scientific rigor.",
            "The response is well-structured, following the specified format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
