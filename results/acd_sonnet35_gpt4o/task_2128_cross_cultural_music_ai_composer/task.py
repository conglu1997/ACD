import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        musical_combinations = [
            {
                "style1": "Indian Classical (Hindustani)",
                "style2": "West African Highlife",
                "theme": "Celebration of Life"
            },
            {
                "style1": "Chinese Opera",
                "style2": "Andean Folk Music",
                "theme": "Nature and Seasons"
            }
        ]
        return {
            "1": random.choice(musical_combinations),
            "2": random.choice(musical_combinations)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system capable of analyzing and combining musical elements from {t['style1']} and {t['style2']}, then use it to compose a new piece of music on the theme of '{t['theme']}'. Your response should include:\n\n1. Musical Analysis (250-300 words):\n   a) Analyze the key characteristics of {t['style1']}, including its rhythmic patterns, melodic structures, and typical instruments.\n   b) Analyze the key characteristics of {t['style2']}, focusing on the same elements.\n   c) Identify potential points of similarity and difference between these two musical styles.\n\n2. AI System Design (300-350 words):\n   a) Describe the architecture of your AI system for musical analysis and composition.\n   b) Explain how your system would process and represent musical elements from both styles.\n   c) Detail how your AI would generate new musical pieces that combine elements from both styles.\n   d) Discuss any novel approaches or algorithms your system uses to ensure cultural authenticity and musical coherence.\n\n3. Composition Process (250-300 words):\n   a) Outline how your AI system would approach composing a piece on the theme of '{t['theme']}'.\n   b) Explain how elements from both {t['style1']} and {t['style2']} would be incorporated.\n   c) Describe the expected structure and characteristics of the resulting composition.\n\n4. Cultural Considerations (200-250 words):\n   a) Discuss potential cultural sensitivities or challenges in combining these musical styles.\n   b) Explain how your AI system addresses these concerns to ensure respectful representation.\n   c) Describe how the system maintains cultural authenticity while creating a novel composition.\n\n5. Evaluation Methodology (150-200 words):\n   a) Propose a method to evaluate the quality and cultural authenticity of the AI-generated composition.\n   b) Suggest criteria for assessing how well the piece incorporates elements from both musical styles.\n   c) Describe how you would gather feedback from cultural experts and musicians.\n\n6. Potential Applications and Implications (150-200 words):\n   a) Discuss potential applications of your AI system in music education, cultural exchange, or the music industry.\n   b) Explore the implications of AI-generated cross-cultural music on human creativity and cultural preservation.\n\nEnsure your response demonstrates a deep understanding of musical theory, cultural aspects of music, and AI system design. Use appropriate technical terminology and provide clear explanations where necessary. Be creative in your approach while maintaining cultural sensitivity and technical feasibility.\n\nFormat your response with clear headings for each section. Your total response should be between 1300-1600 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of both {t['style1']} and {t['style2']} musical styles.",
            "The AI system design is technically sound and innovative.",
            f"The composition process effectively combines elements from both musical styles while addressing the theme of '{t['theme']}'.",
            "Cultural considerations are thoughtfully addressed, showing sensitivity and respect.",
            "The evaluation methodology is comprehensive and well-reasoned.",
            "Potential applications and implications are insightfully discussed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
