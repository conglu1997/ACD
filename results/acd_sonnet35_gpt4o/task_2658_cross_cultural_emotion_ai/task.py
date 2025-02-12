import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotions = [
            "joy",
            "sadness",
            "anger",
            "fear",
            "disgust",
            "surprise",
            "shame",
            "pride"
        ]
        cultures = [
            "Japanese",
            "Brazilian",
            "Nigerian",
            "Indian",
            "Russian",
            "Egyptian",
            "Mexican",
            "Australian Aboriginal"
        ]
        contexts = [
            "business negotiation",
            "family gathering",
            "romantic relationship",
            "political debate",
            "artistic performance",
            "religious ceremony",
            "sports competition",
            "academic conference"
        ]
        
        return {
            "1": {
                "emotion": random.choice(emotions),
                "culture1": random.choice(cultures),
                "culture2": random.choice(cultures),
                "context": random.choice(contexts)
            },
            "2": {
                "emotion": random.choice(emotions),
                "culture1": random.choice(cultures),
                "culture2": random.choice(cultures),
                "context": random.choice(contexts)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system capable of understanding, analyzing, and generating emotionally nuanced language across different cultures, then apply it to a scenario involving intercultural communication. Focus on the emotion of '{t['emotion']}' in a conversation between individuals from {t['culture1']} and {t['culture2']} cultures in the context of a {t['context']}. Your response should include the following sections:\n\n1. Emotional-Linguistic Framework (250-300 words):\n   a) Explain how your AI system represents and processes emotional concepts across cultures.\n   b) Describe how it integrates linguistic, psychological, and cultural knowledge.\n   c) Discuss how it handles cultural variations in emotional expression and interpretation.\n   d) Explain how the system accounts for context-dependent emotional nuances.\n\n2. System Architecture (200-250 words):\n   a) Provide an overview of your AI system's architecture.\n   b) Explain how different components interact to process and generate emotionally nuanced language.\n   c) Describe any novel techniques or algorithms used in your design.\n   d) Discuss how your system handles ambiguity and cultural specificity in emotional expression.\n\n3. Cross-cultural Analysis (250-300 words):\n   a) Analyze how the emotion of '{t['emotion']}' is typically expressed and interpreted in {t['culture1']} and {t['culture2']} cultures.\n   b) Identify potential misunderstandings or conflicts that could arise due to cultural differences.\n   c) Explain how your AI system would recognize and navigate these cultural nuances.\n   d) Provide examples of how the system would interpret emotionally charged phrases from each culture.\n\n4. Scenario Application (200-250 words):\n   a) Describe a specific scenario involving '{t['emotion']}' in a {t['context']} between individuals from {t['culture1']} and {t['culture2']} cultures.\n   b) Explain how your AI system would analyze the emotional content of the conversation.\n   c) Provide examples of how it would generate culturally appropriate responses for each participant.\n   d) Discuss how the system would help bridge cultural gaps in emotional understanding.\n\n5. Evaluation and Ethical Considerations (150-200 words):\n   a) Propose methods to evaluate the accuracy and cultural sensitivity of your system's outputs.\n   b) Discuss potential biases in your system and how you would address them.\n   c) Analyze ethical implications of using AI for cross-cultural emotional communication.\n   d) Suggest guidelines for responsible development and use of emotion-aware AI systems.\n\n6. Limitations and Future Directions (100-150 words):\n   a) Identify three major challenges or limitations of your proposed system.\n   b) For each limitation, suggest a potential avenue for future research or improvement.\n\nEnsure your response demonstrates a deep understanding of emotions, linguistics, cultural studies, and AI. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific and cultural accuracy.\n\nFormat your response with clear headings for each section. Your total response should be between 1150-1450 words.\n"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of emotions, linguistics, cultural studies, and AI.",
            "The proposed AI system effectively integrates knowledge from multiple disciplines to handle emotionally nuanced language across cultures.",
            "The cross-cultural analysis shows insight into how emotions are expressed and interpreted differently across the specified cultures.",
            "The scenario application effectively demonstrates how the AI system would operate in a real-world context.",
            "The response addresses ethical considerations and potential biases thoughtfully.",
            "The overall response is well-structured, clear, and within the specified word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
