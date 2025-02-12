class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "quantum_threat": "Shor's algorithm",
                "additional_constraint": "Low computational resources"
            },
            "2": {
                "quantum_threat": "Grover's algorithm",
                "additional_constraint": "High-speed performance"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel post-quantum cryptographic system that is resistant to {t['quantum_threat']} and optimized for {t['additional_constraint']}. Your task has five parts:

        1. Cryptosystem Design (250-300 words):
           a) Describe the key components and mechanisms of your cryptosystem.
           b) Explain how it achieves resistance against {t['quantum_threat']}.
           c) Discuss how your design addresses the {t['additional_constraint']} requirement.

        2. Mathematical Foundation (200-250 words):
           a) Explain the mathematical problem or principle underlying your cryptosystem.
           b) Provide a brief proof or justification for why this problem is believed to be hard for quantum computers.

        3. Implementation and Performance (200-250 words):
           a) Describe how your cryptosystem would be implemented in practice.
           b) Analyze its performance characteristics (e.g., key size, encryption/decryption speed, ciphertext expansion).
           c) Compare its performance to existing post-quantum candidates.

        4. Security Analysis (200-250 words):
           a) Analyze potential vulnerabilities or attack vectors for your cryptosystem.
           b) Discuss its security level in terms of quantum and classical computing power.
           c) Propose a hybrid approach combining your system with a classical algorithm for added security.

        5. Future-proofing and Adaptability (150-200 words):
           a) Discuss how your cryptosystem could be adapted to resist potential future quantum algorithms.
           b) Propose a method for transitioning existing systems to your post-quantum cryptosystem.

        Ensure your response demonstrates a deep understanding of both quantum computing principles and cryptography. Be creative in your design while maintaining scientific and mathematical rigor. Use appropriate technical terminology and provide clear explanations for a knowledgeable audience in the field of cryptography and quantum computing.

        Format your response with clear headings for each section.
        """

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all five required sections with appropriate content and word counts.",
            "The cryptosystem design is novel, well-explained, and addresses both the quantum threat and additional constraint.",
            "The mathematical foundation is sound and includes a reasonable justification for quantum resistance.",
            "The implementation and performance analysis is thorough and compares the system to existing candidates.",
            "The security analysis identifies potential vulnerabilities and proposes a hybrid approach.",
            "The future-proofing section discusses adaptability and proposes a transition method.",
            "The overall response demonstrates deep understanding of quantum computing and cryptography principles.",
            "The proposed cryptosystem is creative while maintaining scientific and mathematical rigor."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
