import random
import string

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_concepts = [
            "superposition",
            "entanglement",
            "quantum tunneling",
            "quantum teleportation"
        ]
        linguistic_features = [
            "syntax",
            "semantics",
            "pragmatics",
            "phonology"
        ]
        tasks = {
            "1": {
                "quantum_concept": random.choice(quantum_concepts),
                "linguistic_feature": random.choice(linguistic_features),
                "message_type": "short sentence"
            },
            "2": {
                "quantum_concept": random.choice(quantum_concepts),
                "linguistic_feature": random.choice(linguistic_features),
                "message_type": "paragraph"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired linguistic encryption system based on the quantum concept of {t['quantum_concept']} and the linguistic feature of {t['linguistic_feature']}. Then, use your system to encrypt and decrypt a {t['message_type']}. Your response should include:

1. Encryption System Design (300-350 words):
   a) Explain how your encryption system incorporates the quantum concept of {t['quantum_concept']}.
   b) Describe how the linguistic feature of {t['linguistic_feature']} is used in the encryption process.
   c) Outline the step-by-step process of encrypting a message using your system.
   d) Discuss any novel elements or innovations in your design.
   e) Provide a simple example of how a single word might be encrypted using your system.

2. Encryption Demonstration (250-300 words):
   a) Provide a {t['message_type']} (in English) to be encrypted.
   b) Show the step-by-step encryption process for this message using your system.
   c) Present the final encrypted version of the message.

3. Decryption Process (250-300 words):
   a) Explain the decryption process for your system.
   b) Demonstrate the decryption of the message from step 2.
   c) Discuss any challenges in ensuring accurate decryption.

4. Security Analysis (200-250 words):
   a) Analyze the security strengths of your encryption system.
   b) Identify potential vulnerabilities or weaknesses.
   c) Propose improvements to enhance the system's security.

5. Linguistic and Quantum Implications (150-200 words):
   a) Discuss how your system might provide insights into the relationship between quantum phenomena and language processing.
   b) Explore potential applications of your system in linguistics or quantum computing research.

6. Ethical Considerations (100-150 words):
   a) Identify potential ethical implications of quantum-inspired linguistic encryption.
   b) Propose guidelines for responsible development and use of such systems.

Ensure your response demonstrates a deep understanding of both quantum computing principles and linguistics. Be creative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section, numbered as above. Use subheadings (a, b, c, etc.) within each section as indicated. Your total response should be between 1250-1550 words. Include a brief conclusion summarizing the key aspects of your quantum linguistic encryption system."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of the quantum concept of {t['quantum_concept']} and the linguistic feature of {t['linguistic_feature']}",
            "The encryption system design is creative, scientifically plausible, and effectively incorporates both quantum and linguistic elements",
            "A clear example of encrypting a single word is provided",
            f"The encryption and decryption processes are clearly explained and demonstrated for a {t['message_type']}",
            "The security analysis is thorough and identifies relevant strengths and weaknesses",
            "The discussion of linguistic and quantum implications shows thoughtful consideration of the system's potential impact and applications",
            "The response addresses ethical considerations and proposes relevant guidelines",
            "The writing is clear, well-structured, and uses appropriate technical terminology",
            "The response follows the required format, including section numbering and subheadings",
            "The response includes a brief conclusion summarizing the key aspects of the quantum linguistic encryption system",
            "The response stays within the specified word limit of 1250-1550 words"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
