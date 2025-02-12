import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_properties = [
            {
                "name": "Superposition",
                "description": "The ability of a quantum system to exist in multiple states simultaneously until measured."
            },
            {
                "name": "Entanglement",
                "description": "A quantum phenomenon where particles become correlated in such a way that the quantum state of each particle cannot be described independently."
            },
            {
                "name": "No-cloning theorem",
                "description": "The impossibility of creating an identical copy of an arbitrary unknown quantum state."
            },
            {
                "name": "Quantum tunneling",
                "description": "The quantum mechanical phenomenon where a particle tunnels through a barrier that it classically could not surmount."
            }
        ]
        return {
            "1": random.choice(quantum_properties),
            "2": random.choice(quantum_properties)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum cryptography protocol for secure communication, leveraging the quantum property of {t['name']}. Then, evaluate its resilience against both classical and quantum attacks. Your protocol must use a minimum key length of 256 qubits and should be resistant to the side-channel attack known as 'photon number splitting attack'. Do not use or directly reference existing protocols such as BB84 or E91.

Your response should include the following sections:

1. Quantum Cryptography Protocol Design (300-350 words):
   a) Describe the key components and steps of your quantum cryptography protocol.
   b) Explain how your protocol incorporates {t['name']} to enhance security.
   c) Discuss any novel features that distinguish your approach from existing quantum key distribution methods.
   d) Provide a high-level schematic or pseudocode of your protocol.

2. Quantum-Classical Interface (200-250 words):
   a) Explain how your protocol bridges the quantum and classical domains for practical implementation.
   b) Discuss potential challenges in implementing this protocol in real-world communication systems.
   c) Propose solutions to overcome these challenges.

3. Security Analysis (250-300 words):
   a) Analyze the security of your protocol against classical cryptographic attacks.
   b) Evaluate its resilience against known quantum attacks, specifically addressing Shor's algorithm and the photon number splitting attack.
   c) Discuss any potential vulnerabilities or limitations of your approach.
   d) Compare the security level of your protocol to current classical encryption standards (e.g., AES-256).

4. Performance and Scalability (200-250 words):
   a) Estimate the key generation rate and maximum secure distance for your protocol.
   b) Discuss factors that might affect its performance in practical scenarios.
   c) Analyze the scalability of your protocol for large-scale, global secure communication networks.

5. Ethical and Societal Implications (150-200 words):
   a) Discuss the potential impact of quantum cryptography on privacy, national security, and global communication.
   b) Address ethical considerations related to the development and deployment of quantum cryptography systems.
   c) Propose guidelines for responsible development and use of this technology.

6. Future Developments (150-200 words):
   a) Suggest two potential improvements or extensions to your quantum cryptography protocol.
   b) Discuss how these developments could impact the field of cybersecurity.
   c) Propose a novel research question that arises from the intersection of quantum physics and cryptography.

Ensure your response demonstrates a deep understanding of quantum mechanics, cryptography, and cybersecurity principles. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific and technological plausibility.

Format your response with clear headings for each section and use subheadings where appropriate. Adhere strictly to the word count guidelines provided for each section. Your total response should be between 1250-1550 words.

Note: Do not use external resources or copy existing protocols. Your response should be based on your own understanding and creative problem-solving abilities."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a thorough understanding of quantum cryptography principles and correctly incorporates the quantum property of {t['name']}.",
            "The proposed protocol is innovative, detailed, and scientifically plausible, using a minimum key length of 256 qubits.",
            "The security analysis is comprehensive, considering both classical and quantum attacks, specifically addressing Shor's algorithm and the photon number splitting attack.",
            "The performance and scalability analysis provides realistic estimates for key generation rate and maximum secure distance.",
            "Ethical and societal implications are thoughtfully addressed, with specific guidelines for responsible development and use.",
            "The response shows strong interdisciplinary reasoning, combining insights from quantum physics, cryptography, and cybersecurity.",
            "The writing is clear, well-structured, and adheres to the specified word limits for each section.",
            "The response does not directly copy or reference existing protocols such as BB84 or E91."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
