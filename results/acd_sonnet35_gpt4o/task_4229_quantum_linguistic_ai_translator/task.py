import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "name": "Quantum Entanglement Translation",
                "description": "Develop a method to encode linguistic information in entangled quantum states and use it for translation.",
                "quantum_concept": "Quantum Entanglement",
                "linguistic_feature": "Semantic Relationships",
                "human_language": "Mandarin Chinese"
            },
            {
                "name": "Superposition Language Processing",
                "description": "Create an algorithm that uses quantum superposition to simultaneously process multiple linguistic interpretations.",
                "quantum_concept": "Quantum Superposition",
                "linguistic_feature": "Ambiguity Resolution",
                "human_language": "Arabic"
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that uses quantum computing principles to translate between {t['human_language']} and a hypothetical alien language based on quantum states. Focus on the task of {t['name']}: {t['description']}

Your response should include the following sections:

1. Quantum-Linguistic AI System Design (300-400 words):
   a) Describe the key components and architecture of your AI system.
   b) Explain how your system incorporates the quantum concept of {t['quantum_concept']}.
   c) Detail how your system handles the linguistic feature of {t['linguistic_feature']}.
   d) Discuss any novel quantum algorithms or neural network approaches used in your system.
   e) Provide a detailed description of your system's architecture.

2. Quantum-Linguistic Integration (250-350 words):
   a) Explain how your system maps quantum states to linguistic elements in {t['human_language']}.
   b) Describe how it handles the differences between classical and quantum information processing in the context of language.
   c) Discuss how your approach might reveal new insights about the nature of language or quantum information.

3. Alien Language Model (200-300 words):
   a) Describe the key features of your hypothetical alien language based on quantum states.
   b) Explain how this language differs from {t['human_language']} and how it leverages quantum properties.
   c) Provide an example of a simple 'sentence' or 'expression' in this alien language, showing its quantum state representation.

4. Translation Process (250-350 words):
   a) Detail the step-by-step process your AI system uses to translate between {t['human_language']} and the alien language.
   b) Explain how it handles ambiguities, contextual information, and cultural nuances specific to {t['human_language']}.
   c) Provide a concrete example of translating a sentence from {t['human_language']} to the alien language and vice versa, explaining each step.

5. Potential Applications and Implications (200-300 words):
   a) Discuss potential applications of your quantum-linguistic AI system beyond alien communication.
   b) Explore the implications of this technology for our understanding of language, cognition, and quantum physics.
   c) Consider any ethical considerations or potential risks associated with this technology.

6. Challenges and Future Directions (150-250 words):
   a) Identify the main technical and theoretical challenges in implementing your system.
   b) Propose approaches to address these challenges.
   c) Suggest two directions for future research that could extend or improve your system.

Ensure your response demonstrates a deep understanding of quantum physics, linguistics (especially related to {t['human_language']}), and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section and number your paragraphs within each section. Your total response should be between 1350-1950 words.

NOTE: Your response will be evaluated based on the accuracy and innovation of your quantum-linguistic AI system design, the plausibility and creativity of your alien language model, the clarity and completeness of your translation process explanation, the depth of your analysis of potential applications and implications, and your ability to identify and address challenges in this interdisciplinary field. Strive for a balance between creativity and scientific plausibility in your approach."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must design an AI system that accurately incorporates {t['quantum_concept']} for translating between {t['human_language']} and a hypothetical alien language",
            f"The system must effectively handle the linguistic feature of {t['linguistic_feature']} in the context of {t['human_language']}",
            "The response should include a detailed description of the alien language model based on quantum states",
            f"A concrete example of translating a sentence from {t['human_language']} to the alien language and vice versa must be provided",
            "The response should demonstrate a deep understanding of quantum physics, linguistics, and artificial intelligence",
            "The proposed system should be innovative while maintaining scientific plausibility",
            "The response must address potential applications, implications, challenges, and future directions of the technology",
            "The response should be well-structured, following the outlined sections and word count guidelines"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
