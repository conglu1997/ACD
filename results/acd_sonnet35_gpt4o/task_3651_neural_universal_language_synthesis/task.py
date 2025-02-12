import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        linguistic_features = [
            "Phonological patterns",
            "Syntactic structures",
            "Semantic concepts",
            "Pragmatic principles"
        ]
        neural_regions = [
            "Broca's area",
            "Wernicke's area",
            "Angular gyrus",
            "Inferior frontal gyrus"
        ]
        return {
            "1": {
                "linguistic_feature": random.choice(linguistic_features),
                "neural_region": random.choice(neural_regions)
            },
            "2": {
                "linguistic_feature": random.choice(linguistic_features),
                "neural_region": random.choice(neural_regions)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a theoretical framework for synthesizing a universal language based on common neural patterns across diverse linguistic groups, then propose an AI system to implement and test this language. Focus on the linguistic feature of {t['linguistic_feature']} and the neural region {t['neural_region']}. Your response should include the following sections:\n\n1. Theoretical Framework (300-350 words):\n   a) Explain how {t['linguistic_feature']} could be used as a basis for a universal language element.\n   b) Describe how neural activity in {t['neural_region']} relates to this linguistic feature across different languages.\n   c) Propose a method for identifying common neural patterns associated with this feature.\n   d) Discuss how these common patterns could be translated into a universal language element.\n\n2. Universal Language Design (250-300 words):\n   a) Outline the key principles of your universal language based on neural patterns.\n   b) Explain how your language incorporates the specific element derived from {t['linguistic_feature']}.\n   c) Describe how this language element would be represented and processed in {t['neural_region']}.\n   d) Discuss potential advantages and challenges of this approach to language design.\n\n3. AI System Architecture (300-350 words):\n   a) Propose an AI system capable of implementing and testing your universal language.\n   b) Describe the key components and functionalities of your AI system.\n   c) Explain how the system would process and generate the language element based on {t['linguistic_feature']}.\n   d) Discuss how the AI would simulate or interface with neural activity in {t['neural_region']}.\n\n4. Experimental Design (250-300 words):\n   a) Propose an experiment to test the effectiveness of your universal language and AI system.\n   b) Describe the methodology, including participant selection, procedures, and data collection.\n   c) Explain how you would measure the language's universality and the AI's performance.\n   d) Discuss potential challenges in experimental design and how you would address them.\n\n5. Ethical and Societal Implications (200-250 words):\n   a) Discuss potential ethical concerns related to developing and implementing a universal language.\n   b) Analyze possible societal impacts of widespread adoption of your language system.\n   c) Propose guidelines for responsible development and use of neural-based universal languages.\n\n6. Future Directions (150-200 words):\n   a) Suggest two potential improvements or extensions to your universal language system.\n   b) Discuss how this technology might evolve and its potential impact on global communication.\n   c) Propose a related research direction that combines insights from your system with another scientific discipline.\n\nEnsure your response demonstrates a deep understanding of neuroscience, linguistics, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.\n\nFormat your response with clear headings for each section, numbered as above. Your total response should be between 1450-1750 words. Include a word count at the end of your response."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately addresses the linguistic feature of {t['linguistic_feature']} and the neural region {t['neural_region']}.",
            "The proposed universal language design is innovative and scientifically plausible.",
            "The AI system architecture is well-designed and capable of implementing the proposed language.",
            "The experimental design is comprehensive and appropriate for testing the language and AI system.",
            "The response demonstrates a deep understanding of neuroscience, linguistics, and artificial intelligence.",
            "The ethical and societal implications are thoroughly considered.",
            "The future directions proposed are insightful and relevant."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
