import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        crypto_purposes = [
            {
                "purpose": "key distribution",
                "classical_algorithm": "Diffie-Hellman key exchange",
                "quantum_threat": "Shor's algorithm"
            },
            {
                "purpose": "digital signatures",
                "classical_algorithm": "RSA",
                "quantum_threat": "Shor's algorithm"
            },
            {
                "purpose": "hash function",
                "classical_algorithm": "SHA-3",
                "quantum_threat": "Grover's algorithm"
            },
            {
                "purpose": "symmetric encryption",
                "classical_algorithm": "AES",
                "quantum_threat": "Grover's algorithm"
            }
        ]
        return {
            "1": random.choice(crypto_purposes),
            "2": random.choice(crypto_purposes)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Quantum computing leverages quantum mechanical phenomena like superposition and entanglement to perform certain computations faster than classical computers. Post-quantum cryptography aims to develop cryptographic systems that are secure against both quantum and classical computers.\n\nDesign a novel quantum algorithm for {t['purpose']} that is resistant to quantum attacks. Your task has four parts:\n\n1. Algorithm Design (300-350 words):\nCreate a quantum algorithm that addresses the vulnerabilities of {t['classical_algorithm']} to {t['quantum_threat']}. Your algorithm should:\na) Explain the core principle of your quantum approach.\nb) Describe how it leverages quantum mechanical properties (e.g., superposition, entanglement).\nc) Outline the steps of the algorithm using quantum circuit notation or high-level pseudocode.\nd) Explain how your algorithm achieves post-quantum security.\n\n2. Theoretical Analysis (200-250 words):\nAnalyze the theoretical performance of your algorithm, addressing:\na) Time and space complexity in terms of quantum operations and qubits.\nb) How it compares to classical alternatives in terms of efficiency and security.\nc) Any trade-offs made in the design and their justification.\n\n3. Practical Considerations (200-250 words):\nDiscuss the practical aspects of implementing and using your algorithm:\na) Required quantum hardware capabilities and current technological limitations.\nb) Potential challenges in scaling the algorithm for real-world use.\nc) Integration with existing cryptographic infrastructures.\n\n4. Implications and Future Directions (250-300 words):\nExplore the broader implications of your quantum cryptographic algorithm:\na) Potential impact on current cryptographic standards and protocols.\nb) Ethical considerations, including privacy and security implications.\nc) Suggest areas for future research to enhance or extend your algorithm.\nd) Discuss how your algorithm might evolve with advancements in quantum computing technology.\n\nEnsure your response demonstrates a deep understanding of quantum computing principles, cryptography, and their intersection. Be innovative in your approach while maintaining scientific plausibility. Format your response using clear headings for each section. Your total response should be between 950-1150 words, adhering to the specified word counts for each section."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should propose a novel quantum algorithm for {t['purpose']}.",
            "The algorithm design should be clearly explained and leverage quantum mechanical properties.",
            "The theoretical analysis should address time and space complexity, and compare to classical alternatives.",
            "Practical considerations should discuss hardware requirements and implementation challenges.",
            "The implications and future directions should be thoughtfully explored.",
            "The response should demonstrate a deep understanding of both quantum computing and cryptography.",
            "The response should adhere to the specified word count for each section and the overall total."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
