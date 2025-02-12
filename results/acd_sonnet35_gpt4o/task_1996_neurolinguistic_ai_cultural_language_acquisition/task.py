import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultures = [
            {
                "culture": "Amazonian Pirahã",
                "linguistic_feature": "absence of number words and counting",
                "cultural_context": "hunter-gatherer society with strong emphasis on immediate experience"
            },
            {
                "culture": "Inuit",
                "linguistic_feature": "polysynthetic language structure",
                "cultural_context": "Arctic environment with complex kinship systems"
            }
        ]
        return {
            "1": random.choice(cultures),
            "2": random.choice(cultures)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can analyze and reproduce the neural patterns associated with language acquisition in the {t['culture']} culture, focusing on their {t['linguistic_feature']}. Then, use this system to create a novel method for rapid language learning. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system, including neural network architecture and data processing modules.
   b) Explain how your system integrates neuroscientific principles of language acquisition.
   c) Detail how the system accounts for the specific {t['linguistic_feature']} of the {t['culture']} language.
   d) Discuss how the system incorporates the {t['cultural_context']} in its language learning process.

2. Neural Pattern Analysis (250-300 words):
   a) Explain your approach to analyzing neural patterns associated with language acquisition.
   b) Describe how your system differentiates between general language acquisition patterns and culture-specific patterns.
   c) Propose a method for validating the accuracy of the AI's neural pattern analysis.

3. Rapid Language Learning Method (250-300 words):
   a) Based on your AI system's analysis, propose a novel method for rapid language learning.
   b) Explain how this method leverages the neural patterns identified by your system.
   c) Describe how this method could be adapted for learners from different cultural backgrounds.
   d) Provide a specific example of how this method would teach a complex aspect of the {t['culture']} language.

4. Ethical Considerations and Limitations (200-250 words):
   a) Discuss potential ethical implications of using AI to analyze and reproduce cultural language acquisition patterns.
   b) Address concerns about cultural appropriation or misrepresentation in your system.
   c) Identify limitations of your approach and propose ways to address them.

5. Cross-Cultural Applications (200-250 words):
   a) Explain how your system and rapid learning method could be applied to other cultures and languages.
   b) Discuss potential benefits and challenges of using this technology for cross-cultural communication and understanding.
   c) Propose an experiment to test the effectiveness of your system across multiple cultures.

Ensure your response demonstrates a deep understanding of neurolinguistics, artificial intelligence, and cultural anthropology. Be creative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Your total response should be between 1200-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The AI system design effectively incorporates the {t['linguistic_feature']} of the {t['culture']} language.",
            f"The proposal demonstrates a deep understanding of neurolinguistics, AI, and the cultural context of {t['culture']}.",
            "The rapid language learning method is innovative and well-justified based on the AI system's analysis.",
            "Ethical considerations and limitations are thoroughly addressed.",
            "The cross-cultural applications are thoughtfully explored and demonstrate the system's potential broader impact.",
            "The response is well-structured, comprehensive, and within the specified word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
