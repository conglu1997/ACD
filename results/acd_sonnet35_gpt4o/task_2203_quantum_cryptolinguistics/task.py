import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ancient_systems = [
            {
                "writing_system": "Cuneiform",
                "quantum_concept": "Quantum superposition",
                "message_type": "Diplomatic treaty"
            },
            {
                "writing_system": "Egyptian hieroglyphs",
                "quantum_concept": "Quantum entanglement",
                "message_type": "Religious prophecy"
            },
            {
                "writing_system": "Linear B",
                "quantum_concept": "Quantum teleportation",
                "message_type": "Trade agreement"
            },
            {
                "writing_system": "Maya script",
                "quantum_concept": "Quantum error correction",
                "message_type": "Astronomical prediction"
            }
        ]
        return {
            "1": random.choice(ancient_systems),
            "2": random.choice(ancient_systems)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-based cryptographic system inspired by the ancient {t['writing_system']} writing system, incorporating the quantum concept of {t['quantum_concept']}. Then, use your system to encode and decode a complex message in the form of a {t['message_type']}. Your task has the following components:

1. Quantum Cryptosystem Design (300-350 words):
   a) Describe the key features of your quantum cryptographic system, explaining how it's inspired by {t['writing_system']}.
   b) Explain how your system incorporates {t['quantum_concept']} into its encryption and decryption processes.
   c) Discuss any novel elements in your design that differ from traditional quantum cryptography.
   d) Provide a high-level schematic or diagram of your system (describe it textually).

2. Ancient Language Integration (250-300 words):
   a) Explain how specific features of {t['writing_system']} are translated into quantum states or operations.
   b) Describe any challenges in adapting this ancient writing system to a quantum context and how you addressed them.
   c) Discuss how your system preserves or reinterprets the cultural and linguistic aspects of {t['writing_system']}.

3. Encoding Process (200-250 words):
   a) Detail the step-by-step process of encoding a {t['message_type']} using your quantum cryptosystem.
   b) Explain how the quantum states are prepared and manipulated during encoding.
   c) Describe any error mitigation techniques used in your encoding process.

4. Decoding Process (200-250 words):
   a) Explain the procedure for decoding a message encrypted with your system.
   b) Discuss how {t['quantum_concept']} is utilized in the decoding process.
   c) Address any potential vulnerabilities in your decoding method and how they might be mitigated.

5. Security Analysis (150-200 words):
   a) Analyze the security strengths of your quantum cryptosystem compared to classical systems.
   b) Discuss potential attack vectors and how your system resists them.
   c) Explain how the integration of {t['writing_system']} features enhances or challenges the security of your system.

6. Practical Application (150-200 words):
   a) Propose a realistic scenario where your quantum cryptolinguistic system could be applied.
   b) Discuss the potential impact of your system on fields such as archaeology, linguistics, or secure communication.
   c) Address any ethical considerations in using quantum technology inspired by ancient writing systems.

Ensure your response demonstrates a deep understanding of quantum computing, cryptography, and ancient writing systems. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific and technological plausibility.

Format your response using clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a comprehensive understanding of {t['writing_system']} and how it can be adapted to a quantum cryptographic system.",
            f"The quantum cryptosystem clearly incorporates {t['quantum_concept']} in a meaningful and technically sound way.",
            f"The encoding and decoding processes for a {t['message_type']} are well-explained and feasible within the proposed system.",
            "The security analysis is thorough and considers both quantum and classical attack vectors.",
            "The practical application scenario is realistic and thoughtfully considers ethical implications.",
            "The response maintains scientific rigor while showcasing creativity in system design and interdisciplinary knowledge integration.",
            "The response is well-structured with clear headings for each section as requested."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
