import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "superposition",
            "entanglement",
            "tunneling",
            "coherence"
        ]
        biological_structures = [
            "DNA",
            "proteins",
            "cell membranes",
            "synapses"
        ]
        organism_types = [
            "bacteria",
            "plants",
            "insects",
            "mammals"
        ]
        return {
            "1": {
                "quantum_principle": random.choice(quantum_principles),
                "biological_structure": random.choice(biological_structures),
                "organism_type": random.choice(organism_types)
            },
            "2": {
                "quantum_principle": random.choice(quantum_principles),
                "biological_structure": random.choice(biological_structures),
                "organism_type": random.choice(organism_types)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical quantum-biological communication system for information exchange between {t['organism_type']}, integrating principles from quantum mechanics, molecular biology, and information theory. Your system should focus on the quantum principle of {t['quantum_principle']} and utilize the biological structure {t['biological_structure']}.

Provide your response in the following format:

1. System Overview (250-300 words):
   a) Describe the key components and mechanisms of your quantum-biological communication system.
   b) Explain how {t['quantum_principle']} is utilized in your system's design.
   c) Discuss how {t['biological_structure']} is integrated into the communication mechanism.
   d) Outline the basic process of information exchange between organisms using your system.

2. Quantum-Biological Interface (200-250 words):
   a) Explain how your system interfaces quantum phenomena with biological structures.
   b) Describe the process of encoding and decoding information using quantum states in biological systems.
   c) Discuss any novel mechanisms or principles employed in this interface.

3. Information Processing and Transmission (200-250 words):
   a) Detail the step-by-step process of how information is processed and transmitted in your system.
   b) Explain how the quantum and biological components work together to achieve efficient communication.
   c) Describe any error correction or noise reduction mechanisms in your system.

4. Evolutionary and Ecological Implications (150-200 words):
   a) Discuss how this communication system might have evolved or could evolve in {t['organism_type']}.
   b) Explain potential ecological advantages or disadvantages of this system.
   c) Speculate on how this communication method might influence the behavior and interactions of {t['organism_type']}.

5. Theoretical Performance Analysis (150-200 words):
   a) Analyze the theoretical performance of your system compared to classical biological communication systems.
   b) Discuss any potential advantages or limitations of your quantum-biological approach.
   c) Propose metrics for evaluating the efficiency and effectiveness of your system in real-world scenarios.

6. Challenges and Future Directions (150-200 words):
   a) Identify at least three major challenges in implementing or detecting this communication system in nature.
   b) Propose potential solutions or research directions to address these challenges.
   c) Discuss the potential impact of this system on our understanding of quantum biology and inter-organism communication.

Ensure your response demonstrates a deep understanding of quantum mechanics, molecular biology, and information theory. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility. Note that while the system is hypothetical, it should be grounded in current scientific understanding and physical laws.

Your total response should be between 1100-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must include a well-structured design for a quantum-biological communication system for {t['organism_type']}, focusing on {t['quantum_principle']} and {t['biological_structure']}.",
            "The system overview should provide a clear and coherent explanation of how quantum principles are integrated with biological structures for communication.",
            "The quantum-biological interface section should demonstrate a deep understanding of both quantum mechanics and molecular biology.",
            "The information processing and transmission section should present a logical and scientifically plausible process.",
            "The response should address all six required sections with appropriate content and adherence to word limits.",
            "The proposed system should be creative yet grounded in current scientific understanding of quantum mechanics, biology, and information theory.",
            "The discussion of challenges and future directions should be thoughtful and demonstrate an understanding of the complexities involved in quantum biology and inter-organism communication."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
