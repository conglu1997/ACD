import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "emotion_set": "Plutchik's wheel of emotions",
                "linguistic_style": "Poetry",
                "target_language": "English",
                "application_scenario": "Mental health chatbot"
            },
            {
                "emotion_set": "Lövheim cube of emotion",
                "linguistic_style": "Prose",
                "target_language": "Mandarin Chinese",
                "application_scenario": "Cross-cultural negotiation AI"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system that encodes and decodes emotional content in text using a novel emotional representation system based on {t['emotion_set']}. Then, analyze its performance on {t['linguistic_style']} in {t['target_language']}. Your response should include:\n\n1. Emotional Encoding System (250-300 words):\n   a) Describe your novel emotional representation system based on {t['emotion_set']}.\n   b) Explain how your system encodes complex emotional states.\n   c) Discuss how your encoding accounts for cultural variations in emotional expression.\n\n2. AI Architecture (200-250 words):\n   a) Outline the key components of your AI system for encoding and decoding emotions in text.\n   b) Explain how your system processes linguistic input to identify and encode emotions.\n   c) Describe how your system generates text with specific emotional content.\n\n3. Performance Analysis (200-250 words):\n   a) Analyze how your system performs in encoding and decoding emotions in {t['linguistic_style']}.\n   b) Discuss any challenges specific to {t['target_language']} and how your system addresses them.\n   c) Provide an example of how your system would encode and decode a complex emotional state in {t['linguistic_style']}.\n\n4. Application Scenario (150-200 words):\n   a) Explain how your system could be applied in a {t['application_scenario']}.\n   b) Discuss potential benefits and limitations of using your system in this scenario.\n   c) Address any ethical considerations related to this application.\n\n5. Comparative Analysis (150-200 words):\n   a) Compare your emotional encoding system to existing methods of sentiment analysis or emotion detection in text.\n   b) Discuss potential advantages and limitations of your approach.\n\n6. Future Directions (100-150 words):\n   a) Propose two potential improvements or extensions to your system.\n   b) Suggest a novel research question that could be explored using your emotional encoding system.\n\nEnsure your response demonstrates a deep understanding of emotional intelligence, linguistics, and AI principles. Be creative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.\n\nFormat your response with clear headings for each section. Your total response should be between 1050-1350 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a novel and well-explained emotional representation system based on {t['emotion_set']}.",
            f"The AI architecture effectively addresses the challenges of encoding and decoding emotions in {t['linguistic_style']} and {t['target_language']}.",
            f"The performance analysis includes a specific example of encoding and decoding a complex emotional state in {t['linguistic_style']}.",
            f"The application of the system to a {t['application_scenario']} is well-reasoned and considers ethical implications.",
            "The comparative analysis demonstrates a deep understanding of existing emotion detection methods and the advantages of the proposed system.",
            "The response shows creativity and innovation while maintaining scientific plausibility.",
            "The proposed future directions and research questions are novel and relevant to the field of emotional AI."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
