import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_algorithms = [
            "Shor's algorithm",
            "Grover's algorithm",
            "Quantum Fourier Transform",
            "Quantum Phase Estimation"
        ]
        cryptographic_primitives = [
            "Lattice-based cryptography",
            "Hash-based cryptography",
            "Multivariate polynomial cryptography",
            "Code-based cryptography"
        ]
        ethical_concerns = [
            "Privacy in a post-quantum world",
            "Socioeconomic implications of quantum-resistant cryptography",
            "Dual-use potential of quantum cryptographic technologies",
            "Long-term effects on democratic institutions"
        ]
        tasks = [
            {
                "quantum_algorithm": qa,
                "cryptographic_primitive": cp,
                "ethical_concern": ec
            }
            for qa in quantum_algorithms
            for cp in cryptographic_primitives
            for ec in ethical_concerns
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-resistant cryptographic system that addresses the threat posed by {t['quantum_algorithm']}, utilizing {t['cryptographic_primitive']} as a core component. Then, analyze the ethical implications of your system, focusing on the concern of {t['ethical_concern']}. Your response should include the following sections:

1. Quantum Threat Analysis (200-250 words):
   a) Explain how {t['quantum_algorithm']} threatens current cryptographic systems.
   b) Discuss the timeline and potential impact of this threat becoming realized.
   c) Identify specific cryptographic primitives or protocols at risk.

2. Quantum-Resistant System Design (300-350 words):
   a) Describe your proposed quantum-resistant cryptographic system.
   b) Explain how {t['cryptographic_primitive']} is incorporated into your design.
   c) Discuss any novel approaches or optimizations in your system.
   d) Provide a high-level schematic or pseudocode of a key component in your system.

3. Security Analysis (200-250 words):
   a) Analyze the security of your system against quantum and classical attacks.
   b) Discuss any potential vulnerabilities or limitations.
   c) Compare the efficiency and practicality of your system to current cryptographic standards.

4. Implementation and Transition Strategy (200-250 words):
   a) Propose a strategy for implementing your system in real-world applications.
   b) Discuss challenges in transitioning from current cryptographic systems.
   c) Suggest methods for ensuring backward compatibility and interoperability.

5. Ethical Implications (250-300 words):
   a) Analyze the ethical concern of {t['ethical_concern']} in the context of your system.
   b) Discuss potential societal impacts, both positive and negative.
   c) Propose guidelines or policies to address the identified ethical issues.
   d) Consider long-term consequences and potential misuse scenarios.

6. Future Research Directions (150-200 words):
   a) Identify areas for further research in quantum-resistant cryptography.
   b) Suggest potential improvements or extensions to your system.
   c) Discuss how advancements in quantum computing might affect your design.

Ensure your response demonstrates a deep understanding of quantum computing, cryptography, and ethical reasoning. Use appropriate technical terminology and provide clear explanations where necessary. Be innovative in your approach while maintaining scientific and practical plausibility. Your total response should be between 1300-1600 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately explains the threat posed by {t['quantum_algorithm']} to current cryptographic systems",
            f"The proposed quantum-resistant system effectively incorporates {t['cryptographic_primitive']}",
            f"The security analysis is thorough and considers both quantum and classical attacks",
            f"The implementation and transition strategy is practical and addresses real-world challenges",
            f"The ethical implications of {t['ethical_concern']} are thoroughly analyzed in the context of the proposed system",
            "The response demonstrates a deep understanding of quantum computing, cryptography, and ethical reasoning",
            "The proposed system and analysis are innovative while maintaining scientific and practical plausibility",
            "The response addresses all required sections and is within the specified word count range"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
