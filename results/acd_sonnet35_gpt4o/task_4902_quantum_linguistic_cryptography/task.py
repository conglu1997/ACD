import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        endangered_languages = [
            "Ayapaneco",
            "Njerep",
            "Kaixana",
            "Liki",
            "Sarcee"
        ]
        quantum_properties = [
            "Superposition",
            "Entanglement",
            "Quantum tunneling",
            "Quantum interference",
            "Quantum teleportation"
        ]
        return {
            "1": {"language": random.choice(endangered_languages), "quantum_property": random.choice(quantum_properties)},
            "2": {"language": random.choice(endangered_languages), "quantum_property": random.choice(quantum_properties)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-based cryptographic system that uses linguistic features from the endangered language {t['language']} to enhance security, focusing on the quantum property of {t['quantum_property']}. Then, analyze its potential impact on language preservation and quantum computing advancement. Your response should include the following sections:

1. Linguistic Analysis (250-300 words):
   a) Describe the key features of {t['language']} that make it suitable for cryptographic purposes.
   b) Explain how these features can be mapped to quantum states or operations.
   c) Discuss any challenges in using an endangered language for this purpose and how you would address them.

2. Quantum Cryptographic System Design (300-350 words):
   a) Describe the overall architecture of your quantum cryptographic system.
   b) Explain how you incorporate {t['quantum_property']} into your system design.
   c) Detail how linguistic features from {t['language']} are integrated into the quantum cryptographic process.
   d) Provide a step-by-step explanation of how encryption and decryption would work in your system.

3. Security Analysis (200-250 words):
   a) Analyze the security strengths of your proposed system.
   b) Discuss potential vulnerabilities and how they might be addressed.
   c) Compare your system's theoretical security to current classical and quantum cryptographic methods.

4. Implementation Challenges (200-250 words):
   a) Identify the main technical challenges in implementing your system.
   b) Discuss any linguistic or cultural challenges in using an endangered language for cryptography.
   c) Propose solutions or research directions to address these challenges.

5. Impact Analysis (250-300 words):
   a) Discuss how your system could contribute to the preservation of {t['language']}.
   b) Analyze potential advancements in quantum computing that might result from your approach.
   c) Consider ethical implications of using endangered languages in cryptographic systems.
   d) Explore potential applications of your system beyond cryptography.

6. Future Directions (150-200 words):
   a) Propose two potential extensions or improvements to your system.
   b) Discuss how your approach could be adapted to other endangered languages or quantum properties.
   c) Speculate on the long-term implications of quantum-linguistic cryptography for both fields.

Ensure your response demonstrates a deep understanding of quantum computing, linguistics, and cryptography. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of the endangered language {t['language']} and its potential for cryptographic use.",
            f"The quantum cryptographic system design effectively incorporates the quantum property of {t['quantum_property']}.",
            "The security analysis is thorough and compares the proposed system to existing methods.",
            "Implementation challenges are realistically identified and addressed.",
            "The impact analysis considers both language preservation and quantum computing advancements.",
            "The proposed future directions are innovative and build upon the presented system.",
            "The response shows creativity and interdisciplinary knowledge integration throughout."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
