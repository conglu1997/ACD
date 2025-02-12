import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "Superposition",
            "Entanglement",
            "Quantum tunneling",
            "Quantum coherence"
        ]
        consciousness_aspects = [
            "Self-awareness",
            "Integrated information",
            "Qualia",
            "Global workspace"
        ]
        return {
            "1": {
                "quantum_principle": random.choice(quantum_principles),
                "consciousness_aspect": random.choice(consciousness_aspects)
            },
            "2": {
                "quantum_principle": random.choice(quantum_principles),
                "consciousness_aspect": random.choice(consciousness_aspects)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired neural network architecture for modeling consciousness, focusing on the quantum principle of {t['quantum_principle']} and its application to the consciousness aspect of {t['consciousness_aspect']}. Your response should include:

1. Quantum-Inspired Neural Architecture (300-350 words):
   a) Describe the key components of your quantum-inspired neural network architecture.
   b) Explain how you incorporate the quantum principle of {t['quantum_principle']} into your architecture.
   c) Discuss how this architecture is specifically tailored to model the consciousness aspect of {t['consciousness_aspect']}.
   d) Include a simple diagram or schematic representation of your architecture (using ASCII art or a clear textual description).

2. Quantum Principle Application (250-300 words):
   a) Explain in detail how the quantum principle of {t['quantum_principle']} is used to enhance the modeling of consciousness.
   b) Describe the theoretical advantages this quantum-inspired approach might offer over classical neural networks for modeling {t['consciousness_aspect']}.
   c) Discuss any challenges in implementing this quantum principle in a neural network architecture.

3. Consciousness Modeling (200-250 words):
   a) Provide a step-by-step explanation of how your architecture would process and model the consciousness aspect of {t['consciousness_aspect']}.
   b) Describe the data inputs, processing steps, and expected outputs of your system.
   c) Explain how the quantum-inspired elements contribute to modeling this aspect of consciousness.

4. Comparative Analysis (200-250 words):
   a) Compare your quantum-inspired approach to a state-of-the-art classical method for modeling consciousness.
   b) Analyze potential performance improvements, efficiency gains, or novel capabilities of your approach.
   c) Discuss any limitations or drawbacks of your quantum-inspired architecture.

5. Neuroscientific Implications (150-200 words):
   a) Discuss how your quantum-inspired architecture might relate to or inform our understanding of brain function and consciousness.
   b) Propose a hypothesis about how quantum effects might play a role in biological neural systems.

6. Ethical and Philosophical Considerations (150-200 words):
   a) Identify potential ethical implications of using quantum-inspired neural networks to model consciousness.
   b) Discuss philosophical questions raised by your approach to modeling consciousness.
   c) Propose guidelines for responsible development and use of consciousness-modeling technologies.

7. Future Research Directions (100-150 words):
   a) Suggest two potential areas for further research based on your quantum-inspired consciousness model.
   b) Explain how these research directions could advance the fields of quantum computing, neuroscience, or artificial intelligence.

Ensure your response demonstrates a deep understanding of quantum physics principles, neuroscience, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1350-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of quantum physics, neuroscience, and artificial intelligence.",
            f"The quantum-inspired neural architecture effectively incorporates the principle of {t['quantum_principle']}.",
            f"The model convincingly addresses the consciousness aspect of {t['consciousness_aspect']}.",
            "The explanation of quantum principle application is thorough and scientifically sound.",
            "The comparative analysis shows insightful understanding of both quantum-inspired and classical approaches.",
            "Ethical and philosophical considerations are thoughtfully addressed.",
            "The response is well-structured, coherent, and demonstrates creative problem-solving within the constraints of scientific plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
