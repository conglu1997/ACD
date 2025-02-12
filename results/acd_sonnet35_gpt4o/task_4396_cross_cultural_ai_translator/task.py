import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultural_concepts = [
            'Hygge (Danish)',
            'Wabi-sabi (Japanese)',
            'Ubuntu (Zulu)',
            'Schadenfreude (German)',
            'Saudade (Portuguese)',
            'Jugaad (Hindi)',
            'Guanxi (Chinese)',
            'Mana (Polynesian)'
        ]
        target_languages = [
            'English',
            'Spanish',
            'French',
            'Arabic',
            'Russian',
            'Swahili'
        ]
        linguistic_features = [
            'metaphors',
            'idioms',
            'proverbs',
            'semantic fields'
        ]
        
        return {
            "1": {
                "concept": random.choice(cultural_concepts),
                "target_language": random.choice(target_languages),
                "linguistic_feature": random.choice(linguistic_features)
            },
            "2": {
                "concept": random.choice(cultural_concepts),
                "target_language": random.choice(target_languages),
                "linguistic_feature": random.choice(linguistic_features)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that analyzes and translates the complex cultural concept of {t['concept']} into {t['target_language']}, with a focus on preserving and adapting {t['linguistic_feature']}. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for cross-cultural concept analysis and translation.
   b) Explain how your system integrates linguistic analysis with cultural and historical context.
   c) Detail the process of translating and adapting {t['linguistic_feature']} across cultures.
   d) Include a high-level diagram or pseudocode snippet illustrating a key process in your system.

2. Cultural and Linguistic Analysis (200-250 words):
   a) Analyze the cultural and linguistic nuances of {t['concept']} in its original context.
   b) Explain how your system would identify and process relevant {t['linguistic_feature']} related to this concept.
   c) Discuss challenges in preserving the original meaning while adapting to the target culture.

3. Translation and Adaptation Process (200-250 words):
   a) Describe how your system would translate {t['concept']} into {t['target_language']}.
   b) Explain your approach to adapting {t['linguistic_feature']} to maintain cultural relevance.
   c) Provide an example of how a specific aspect of {t['concept']} might be translated and adapted.

4. Evaluation and Refinement (150-200 words):
   a) Propose a method for evaluating the accuracy and cultural appropriateness of the translation.
   b) Describe how your system would incorporate feedback to improve future translations.
   c) Discuss potential biases in your system and how they might be mitigated.

5. Ethical Considerations (150-200 words):
   a) Analyze the ethical implications of using AI for cross-cultural communication and translation.
   b) Discuss potential risks of misinterpretation or cultural appropriation.
   c) Propose guidelines for responsible use of your AI system in real-world applications.

6. Broader Implications and Future Directions (150-200 words):
   a) Discuss how your system could contribute to cross-cultural understanding and communication.
   b) Propose two potential extensions or applications of your system in fields such as diplomacy, education, or global business.
   c) Suggest areas for future research in AI-driven cross-cultural analysis and translation.

Ensure your response demonstrates a deep understanding of linguistics, cultural anthropology, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific and cultural sensitivity.

Format your response with clear headings for each section. Your total response should be between 1100-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The system architecture clearly explains how it integrates linguistic analysis with cultural and historical context for translating {t['concept']}.",
            f"The cultural and linguistic analysis demonstrates a deep understanding of {t['concept']} and its associated {t['linguistic_feature']}.",
            f"The translation and adaptation process provides a clear and culturally sensitive approach to rendering {t['concept']} in {t['target_language']}.",
            "The response addresses ethical considerations and proposes guidelines for responsible use of the AI system.",
            "The broader implications and future directions section suggests innovative yet plausible applications and areas for future research.",
            "The overall response demonstrates interdisciplinary knowledge integration and creative problem-solving in cross-cultural AI translation."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
