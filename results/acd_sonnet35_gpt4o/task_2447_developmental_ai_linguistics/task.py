import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        language_features = ['phonology', 'syntax', 'semantics', 'pragmatics']
        developmental_stages = ['infant', 'toddler', 'preschool', 'school-age']
        social_contexts = ['family', 'peer', 'educational', 'cultural']
        learning_mechanisms = ['statistical learning', 'rule-based learning', 'social learning', 'embodied cognition']
        
        return {
            "1": {
                "feature": random.choice(language_features),
                "stage": random.choice(developmental_stages),
                "context": random.choice(social_contexts),
                "mechanism": random.choice(learning_mechanisms)
            },
            "2": {
                "feature": random.choice(language_features),
                "stage": random.choice(developmental_stages),
                "context": random.choice(social_contexts),
                "mechanism": random.choice(learning_mechanisms)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system that simulates human language acquisition, focusing on the critical period hypothesis and the role of social interaction in language development. Your system should specifically address the acquisition of {t['feature']} during the {t['stage']} stage, emphasizing the {t['context']} context and utilizing {t['mechanism']}. Your response should include:\n\n1. System Architecture (250-300 words):\n   a) Describe the key components of your AI system for language acquisition.\n   b) Explain how your system integrates principles from cognitive science, linguistics, and developmental psychology.\n   c) Discuss how your system addresses the critical period hypothesis in language acquisition.\n   d) Include a simple diagram of your system architecture using ASCII art or Unicode characters.\n\n2. Language Acquisition Process (200-250 words):\n   a) Explain how your AI system acquires {t['feature']} during the {t['stage']} stage.\n   b) Describe how {t['mechanism']} is implemented in your system.\n   c) Discuss how your system handles the challenges of language acquisition specific to this developmental stage.\n\n3. Social Interaction Modeling (200-250 words):\n   a) Detail how your system models and utilizes social interaction in the {t['context']} context for language learning.\n   b) Explain how this social component enhances the language acquisition process.\n   c) Describe any challenges in modeling social interaction and how your system addresses them.\n\n4. Evaluation and Comparison (200-250 words):\n   a) Propose methods to evaluate your system's language acquisition performance.\n   b) Compare your AI system's language acquisition process to human language acquisition.\n   c) Discuss any limitations of your system in replicating human language learning.\n\n5. Ethical Considerations (150-200 words):\n   a) Discuss potential ethical implications of using AI systems to model child language acquisition.\n   b) Address any privacy concerns related to data collection for training your system.\n   c) Propose guidelines for responsible development and use of such AI systems in research and education.\n\n6. Future Directions (150-200 words):\n   a) Suggest two potential extensions or improvements to your system.\n   b) Discuss how these advancements might impact our understanding of human language acquisition.\n   c) Propose a novel experiment that could further explore the relationship between AI and human language development.\n\nEnsure your response demonstrates a deep understanding of language acquisition theories, developmental psychology, and AI technologies. Use appropriate technical terminology and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility.\n\nFormat your response with clear headings for each section, numbered as above. Your total response should be between 1150-1450 words. Stay within the specified word count for each section.\n\nFor the system architecture diagram, use ASCII art or Unicode characters to create a clear and informative representation. The diagram should be no larger than 20 lines by 80 characters."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of language acquisition theories, particularly in relation to {t['feature']} during the {t['stage']} stage.",
            f"The AI system design effectively incorporates {t['mechanism']} and models social interaction in the {t['context']} context.",
            "The proposed system architecture is innovative and well-explained, with a clear integration of cognitive science, linguistics, and developmental psychology principles.",
            "The evaluation methods and comparison to human language acquisition are thorough and insightful.",
            "The ethical considerations are thoughtfully discussed, and the proposed guidelines are comprehensive.",
            "The suggested future directions and novel experiment are creative and relevant to advancing the field.",
            "The response shows a high level of interdisciplinary integration across cognitive science, linguistics, developmental psychology, and artificial intelligence.",
            "The writing is clear, well-structured, and uses technical terminology appropriately."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
