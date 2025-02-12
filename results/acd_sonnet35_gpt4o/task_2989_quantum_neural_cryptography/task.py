import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        encryption_types = [
            "Quantum Key Distribution",
            "Post-Quantum Cryptography",
            "Homomorphic Encryption"
        ]
        quantum_concepts = [
            "Superposition",
            "Entanglement",
            "Quantum Tunneling"
        ]
        neural_architectures = [
            "Quantum Convolutional Neural Networks",
            "Quantum Recurrent Neural Networks",
            "Quantum Generative Adversarial Networks"
        ]
        
        tasks = [
            {
                "encryption_type": enc,
                "quantum_concept": qc,
                "neural_architecture": na
            }
            for enc in encryption_types
            for qc in quantum_concepts
            for na in neural_architectures
        ]
        
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that uses quantum-inspired neural networks to create and break advanced encryption protocols, then analyze its potential applications and ethical implications in cybersecurity. Your system should focus on {t['encryption_type']} and incorporate the quantum concept of {t['quantum_concept']} using a {t['neural_architecture']} architecture.

Brief explanations of encryption types:
- Quantum Key Distribution: A method for securely exchanging cryptographic keys using quantum mechanical principles.
- Post-Quantum Cryptography: Cryptographic algorithms designed to be secure against quantum computer attacks.
- Homomorphic Encryption: A form of encryption allowing computation on ciphertexts, generating an encrypted result that matches the result of operations performed on the plaintext.

Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your quantum-inspired neural cryptography system.
   b) Explain how your system integrates the specified quantum concept into the neural network architecture.
   c) Detail how the system approaches the creation and breaking of the specified encryption type.
   d) Include a high-level diagram or pseudocode to illustrate your architecture (describe it textually).

2. Quantum-Neural Integration (250-300 words):
   a) Explain how the specified quantum concept enhances the neural network's capabilities.
   b) Describe any novel quantum-inspired algorithms or techniques used in your system.
   c) Discuss the theoretical advantages of your approach over classical cryptography methods.

3. Encryption and Decryption Process (250-300 words):
   a) Provide a step-by-step explanation of how your system creates an encryption protocol.
   b) Describe the process your system uses to attempt breaking an encryption.
   c) Analyze the strengths and potential vulnerabilities of your approach.

4. Performance Analysis (200-250 words):
   a) Propose metrics to evaluate the effectiveness of your system in creating and breaking encryptions.
   b) Discuss how you would benchmark your system against current state-of-the-art cryptography methods.
   c) Address any potential limitations or challenges in implementing your system.

5. Cybersecurity Applications (200-250 words):
   a) Suggest two potential real-world applications of your quantum-neural cryptography system.
   b) Analyze how these applications could impact current cybersecurity practices.
   c) Discuss any technical or practical challenges in deploying such a system.

6. Ethical Implications (200-250 words):
   a) Identify potential ethical issues arising from the development and use of quantum-neural cryptography.
   b) Discuss the dual-use nature of this technology (for both defensive and offensive purposes).
   c) Propose guidelines for responsible development and use of advanced AI-driven cryptography systems.

7. Future Research Directions (150-200 words):
   a) Suggest areas for future research to enhance or extend your quantum-neural cryptography system.
   b) Discuss how advancements in quantum computing might impact the field of AI-driven cryptography.
   c) Propose a potential experiment to validate the effectiveness of your system.

Ensure your response demonstrates a deep understanding of quantum computing principles, neural network architectures, and cryptography. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1550-1900 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum computing principles, neural network architectures, and cryptography.",
            "The system architecture effectively integrates the specified quantum concept, neural architecture, and encryption type.",
            "The quantum-neural integration is well-explained and theoretically sound.",
            "The encryption and decryption processes are clearly described and analyzed.",
            "The performance analysis includes relevant metrics and benchmarking considerations.",
            "The proposed cybersecurity applications are innovative and well-reasoned.",
            "Ethical implications are thoroughly discussed, including dual-use concerns.",
            "Future research directions are insightful and relevant.",
            "The response is creative and innovative while maintaining scientific plausibility.",
            "The writing is clear, well-structured, and uses appropriate technical terminology.",
            "The total word count is between 1550-1900 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0