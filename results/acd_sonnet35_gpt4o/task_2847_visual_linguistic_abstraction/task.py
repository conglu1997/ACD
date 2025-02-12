import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        concepts = [
            {
                "concept": "time",
                "languages": ["Mandarin Chinese", "Hopi"],
                "cultural_context": "Linear vs. cyclic time perception"
            },
            {
                "concept": "causality",
                "languages": ["English", "Japanese"],
                "cultural_context": "Direct vs. indirect expression of cause and effect"
            }
        ]
        return {str(i+1): concept for i, concept in enumerate(random.sample(concepts, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can generate and interpret abstract visual representations of the linguistic concept '{t['concept']}' across the following languages and cultural contexts:

Languages: {', '.join(t['languages'])}
Cultural Context: {t['cultural_context']}

Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for generating and interpreting visual abstractions of linguistic concepts.
   b) Explain how your system incorporates cultural and linguistic nuances specific to the given languages and context.
   c) Detail how the system integrates natural language processing, visual generation, and cross-cultural knowledge.

2. Visual Abstraction Generation (200-250 words):
   a) Explain the process your AI uses to create abstract visual representations of the given concept.
   b) Describe how your system accounts for cultural differences in conceptualization and expression.
   c) Provide a textual description of the abstract visual representations your system would generate for each language.

3. Interpretation Mechanism (200-250 words):
   a) Detail how your AI system interprets and extracts meaning from abstract visual representations.
   b) Explain how the system handles ambiguity and cultural variations in visual symbolism.
   c) Describe a method for evaluating the accuracy and cross-cultural validity of your system's interpretations.

4. Cognitive Science Integration (150-200 words):
   a) Discuss how your system incorporates principles from cognitive linguistics and visual cognition.
   b) Explain how your AI models the relationship between language, thought, and visual perception.

5. Cross-cultural Application (150-200 words):
   a) Propose a method to extend your system to other languages and cultural contexts.
   b) Discuss potential challenges in scaling your system globally and how they might be addressed.

6. Ethical Considerations (100-150 words):
   a) Identify potential biases or limitations in your AI system's approach to cross-cultural visual-linguistic mapping.
   b) Propose safeguards to ensure ethical and culturally sensitive use of your system.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, artificial intelligence, and cross-cultural communication. Use appropriate technical terminology and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a comprehensive system architecture that integrates NLP, visual generation, and cross-cultural knowledge",
            "The visual abstraction generation process is well-explained and accounts for cultural differences",
            "The interpretation mechanism is detailed and addresses ambiguity and cultural variations",
            "The system incorporates relevant principles from cognitive science and linguistics",
            "A viable method for cross-cultural application and scaling is proposed",
            "Ethical considerations and potential biases are adequately addressed",
            "The response demonstrates deep understanding of linguistics, cognitive science, AI, and cross-cultural communication",
            "The proposed system is creative and innovative while maintaining scientific plausibility"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
