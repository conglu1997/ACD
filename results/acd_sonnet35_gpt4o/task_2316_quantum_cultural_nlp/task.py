import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultural_contexts = [
            {
                'culture': 'Polynesian',
                'linguistic_feature': 'honorifics',
                'quantum_aspect': 'superposition'
            },
            {
                'culture': 'Inuit',
                'linguistic_feature': 'evidentiality',
                'quantum_aspect': 'entanglement'
            }
        ]
        return {str(i+1): context for i, context in enumerate(cultural_contexts)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing algorithm for natural language processing that incorporates cultural context, focusing on the following parameters:

Culture: {t['culture']}
Linguistic Feature: {t['linguistic_feature']}
Quantum Aspect: {t['quantum_aspect']}

Your task is to:

1. Quantum NLP Algorithm Design (300-350 words):
   a) Describe the overall structure and key components of your quantum NLP algorithm.
   b) Explain how you incorporate the specified quantum aspect into the algorithm.
   c) Detail how your algorithm handles the given linguistic feature.
   d) Discuss how cultural context is integrated into the quantum NLP process.

2. Quantum-Linguistic-Cultural Integration (250-300 words):
   a) Analyze how the quantum aspect enhances the processing of the specified linguistic feature.
   b) Explain how your algorithm accounts for cultural nuances in language processing.
   c) Provide a specific example of how your algorithm would process a culturally-specific phrase or concept.

3. Mathematical Formulation (200-250 words):
   a) Present a high-level mathematical representation of your quantum NLP algorithm.
   b) Explain the key quantum operations or transformations used.
   c) Discuss how classical NLP techniques are adapted to the quantum realm in your algorithm.

4. Potential Applications (200-250 words):
   a) Propose two potential applications of your quantum cultural NLP algorithm in cross-cultural communication.
   b) Discuss how your algorithm could be used in anthropological research.
   c) Analyze the potential advantages of your approach over classical NLP methods in these applications.

5. Ethical Considerations (150-200 words):
   a) Identify potential ethical concerns related to using quantum computing for cultural and linguistic analysis.
   b) Discuss the implications for privacy, cultural preservation, and potential biases.
   c) Propose guidelines for the responsible development and use of quantum cultural NLP technologies.

6. Future Research Directions (150-200 words):
   a) Suggest two potential research projects that could further develop or validate your quantum cultural NLP approach.
   b) Discuss how these projects could contribute to our understanding of the intersection between quantum computing, linguistics, and cultural anthropology.

Ensure your response demonstrates a deep understanding of quantum computing principles, linguistic theory, and cultural anthropology. Use appropriate technical terminology and provide clear explanations where necessary. Be innovative in your approach while maintaining scientific and theoretical plausibility.

Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum computing, linguistics, and cultural anthropology",
            "The quantum NLP algorithm effectively incorporates the specified quantum aspect and linguistic feature",
            "The algorithm design shows innovative integration of cultural context in quantum NLP",
            "The mathematical formulation is coherent and plausible within the constraints of quantum computing",
            "Proposed applications and future research directions are insightful and well-reasoned",
            "Ethical considerations are thoroughly addressed",
            "The response adheres to the specified word limit (1250-1550 words)"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
