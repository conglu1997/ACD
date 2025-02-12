import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "emotion": "Schadenfreude",
                "origin": "German",
                "target_culture": "Japanese",
                "reason": "to explore the contrast between a culture known for emotional restraint and a complex emotion involving pleasure at others' misfortune"
            },
            {
                "emotion": "Saudade",
                "origin": "Portuguese",
                "target_culture": "Inuit",
                "reason": "to examine how a concept of nostalgic longing translates to a culture with a very different environment and lifestyle"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that translates the abstract emotional concept of {t['emotion']} (originating from {t['origin']} culture) for the {t['target_culture']} culture. This pairing was chosen {t['reason']}. Then, use your system to analyze and compare how this emotion might be expressed in both cultures. Your response should include:

1. Emotional Concept Analysis (200-250 words):
   a) Define and explain the emotional concept of {t['emotion']}.
   b) Discuss its cultural significance in the {t['origin']} culture.
   c) Analyze the cognitive and linguistic components that contribute to this emotion.

2. AI System Design (250-300 words):
   a) Outline the architecture of your AI system for emotional concept translation.
   b) Explain how your system incorporates principles of cognitive linguistics and emotional intelligence.
   c) Describe the process of translating emotional concepts across cultures, including any novel approaches or algorithms.
   d) Discuss how your system accounts for cultural context and nuances in emotional expression.

3. Translation and Cultural Adaptation (200-250 words):
   a) Use your AI system to translate {t['emotion']} into a conceptually equivalent emotion or set of emotions in the {t['target_culture']} culture.
   b) Explain the reasoning behind this translation, including any challenges or limitations.
   c) Discuss how the translated concept might be expressed linguistically and behaviorally in the {t['target_culture']} culture.

4. Comparative Analysis (200-250 words):
   a) Compare and contrast the expression and understanding of this emotion in both cultures.
   b) Analyze any similarities or differences in the cognitive or linguistic structures used to represent this emotion.
   c) Discuss how these differences might impact cross-cultural communication and understanding.

5. Ethical and Practical Implications (150-200 words):
   a) Discuss potential ethical considerations in translating and comparing emotional concepts across cultures.
   b) Explore practical applications of your AI system in fields such as diplomacy, international business, or mental health.
   c) Propose a method to validate the accuracy and cultural sensitivity of your system's translations.

Ensure your response demonstrates a deep understanding of cognitive linguistics, emotional intelligence, and cross-cultural communication. Use appropriate terminology and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility and cultural sensitivity.

Format your response with clear headings for each section. Your total response should be between 1000-1250 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the emotional concept and its cultural significance.",
            "The AI system design is innovative, incorporating principles of cognitive linguistics and emotional intelligence.",
            "The translation and cultural adaptation of the emotion is well-reasoned and culturally sensitive.",
            "The comparative analysis provides insightful observations about the similarities and differences in emotional expression between the two cultures.",
            "The discussion of ethical and practical implications is thoughtful and considers multiple perspectives.",
            "The overall response is creative, scientifically plausible, and demonstrates strong interdisciplinary knowledge integration."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
