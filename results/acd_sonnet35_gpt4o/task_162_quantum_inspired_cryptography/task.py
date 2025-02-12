import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            {
                "name": "Superposition",
                "description": "The ability of a quantum system to exist in multiple states simultaneously"
            },
            {
                "name": "Entanglement",
                "description": "A quantum phenomenon where particles become correlated in such a way that the quantum state of each particle cannot be described independently"
            }
        ]
        return {
            "1": random.choice(quantum_principles),
            "2": random.choice(quantum_principles)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired cryptographic system based on the principle of {t['name']}. Your task is to create an innovative and secure communication method that leverages this quantum principle in a classical computing environment. Your response should include:

1. System Overview (150-200 words):
   Provide a high-level description of your quantum-inspired cryptographic system, explaining how it incorporates the principle of {t['name']} ({t['description']}).

2. Encryption Process (200-250 words):
   Describe the step-by-step process of encrypting a message using your system. Include any necessary mathematical formulas or algorithms, and explain how the quantum principle is simulated or approximated in a classical setting.

3. Encryption Example:
   Provide a simple example of encrypting a short message (e.g., "QUANTUM") using your system. Show the intermediate steps and the final encrypted output.

4. Decryption Process (150-200 words):
   Explain how the intended recipient would decrypt the message, highlighting any unique features of your system that enhance security.

5. Security Analysis (200-250 words):
   Analyze the security strengths and potential vulnerabilities of your cryptographic system. Compare its security features to existing classical and quantum cryptographic methods.

6. Practical Implementation (150-200 words):
   Discuss the feasibility of implementing your system with current technology. Address any technical challenges and propose potential solutions.

7. Novel Application (100-150 words):
   Propose an innovative application of your quantum-inspired cryptographic system beyond secure communication (e.g., in finance, healthcare, or artificial intelligence).

8. Ethical Implications (100-150 words):
   Briefly discuss the potential ethical implications or societal impacts of your cryptographic system.

Ensure your response demonstrates a deep understanding of both quantum mechanics and cryptography principles. Be creative in your approach while maintaining scientific accuracy and plausibility. Your total response should not exceed 1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The cryptographic system clearly incorporates the given quantum principle in a novel way.",
            "The encryption and decryption processes are well-explained and scientifically plausible.",
            "A clear and correct example of the encryption process is provided for a short message.",
            "The security analysis demonstrates a thorough understanding of both classical and quantum cryptography.",
            "The practical implementation discussion addresses real-world challenges and potential solutions.",
            "The proposed novel application is creative and well-reasoned.",
            "The ethical implications are thoughtfully considered and relevant to the proposed system.",
            "The response adheres to the specified word limits for each section and the overall limit of 1500 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
