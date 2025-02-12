import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "quantum_principle": "quantum superposition",
                "neural_feature": "neural oscillations",
                "consciousness_aspect": "subjective experience",
                "ethical_challenge": "free will and determinism"
            },
            {
                "quantum_principle": "quantum entanglement",
                "neural_feature": "neural integration",
                "consciousness_aspect": "unified perception",
                "ethical_challenge": "privacy of thoughts"
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a quantum computing system that simulates neural correlates of consciousness, incorporating principles from quantum mechanics, neuroscience, and artificial intelligence to explore the nature of conscious experience. Your system should focus on the quantum principle of {t['quantum_principle']}, the neural feature of {t['neural_feature']}, and address the consciousness aspect of {t['consciousness_aspect']}. Additionally, consider the ethical challenge of {t['ethical_challenge']} in your analysis.

Your response should include the following sections:

1. Quantum Neural Architecture (300-350 words):
   a) Describe the key components of your quantum neural simulation system.
   b) Explain how you integrate {t['quantum_principle']} with {t['neural_feature']} in your model.
   c) Detail any novel quantum algorithms or neural network structures used in your design.
   d) Include a brief description of a diagram representing your system's architecture.

2. Consciousness Simulation (250-300 words):
   a) Explain how your system models {t['consciousness_aspect']}.
   b) Describe the mechanisms by which quantum effects might contribute to conscious experience in your model.
   c) Discuss how your system distinguishes between conscious and unconscious processing.

3. Theoretical Implications (200-250 words):
   a) Analyze how your model relates to existing theories of consciousness (e.g., Integrated Information Theory, Global Workspace Theory).
   b) Propose a novel hypothesis about the nature of consciousness based on your quantum neural simulation.
   c) Discuss potential implications for our understanding of free will and determinism.

4. Experimental Design (200-250 words):
   a) Propose an experiment to test predictions made by your quantum neural consciousness model.
   b) Describe the methodology, including both quantum and neuroscientific measurements.
   c) Discuss potential challenges in empirically validating your model's predictions.

5. Ethical Considerations (200-250 words):
   a) Address the ethical challenge of {t['ethical_challenge']} in the context of your system.
   b) Discuss potential misuse of technology that can simulate or manipulate consciousness.
   c) Propose guidelines for responsible development and use of quantum neural consciousness models.

6. Future Directions and Limitations (150-200 words):
   a) Identify current limitations of your proposed system.
   b) Suggest areas for future research in quantum neural approaches to consciousness.
   c) Speculate on potential long-term implications for AI, neuroscience, and philosophy of mind.

Ensure your response demonstrates a deep understanding of quantum mechanics, neuroscience, artificial intelligence, and consciousness studies. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Adhere strictly to the word count ranges provided for each section. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum mechanics, neuroscience, artificial intelligence, and consciousness studies",
            "The proposed system effectively integrates the specified quantum principle with the neural feature",
            "The explanation of how the system models the given consciousness aspect is clear and scientifically grounded",
            "The response addresses all required sections comprehensively",
            "The proposed experimental design is well-thought-out and addresses potential challenges",
            "The ethical considerations, including the specified ethical challenge, are thoroughly discussed",
            "The response demonstrates innovative thinking while maintaining scientific plausibility",
            "The response adheres to the specified word count ranges for each section"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
