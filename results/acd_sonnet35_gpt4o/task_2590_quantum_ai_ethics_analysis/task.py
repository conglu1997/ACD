import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_features = [
            "Superposition",
            "Entanglement",
            "Quantum tunneling",
            "Quantum annealing",
            "Quantum error correction"
        ]
        ai_applications = [
            "Network intrusion detection",
            "Encryption key generation",
            "Anomaly detection in data streams",
            "Quantum-resistant cryptography",
            "Secure multi-party computation"
        ]
        return {
            "1": {"quantum_feature": random.choice(quantum_features), "ai_application": random.choice(ai_applications)},
            "2": {"quantum_feature": random.choice(quantum_features), "ai_application": random.choice(ai_applications)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical quantum AI system for cybersecurity that utilizes the quantum feature of {t['quantum_feature']} for the AI application of {t['ai_application']}. Then, analyze its ethical implications for privacy and security. Your response should include:

1. Quantum AI System Design (300-350 words):
   a) Describe the key components of your quantum AI system.
   b) Explain how the specified quantum feature is integrated into the AI architecture.
   c) Detail how the system would function for the given cybersecurity application.
   d) Discuss any novel capabilities or advantages this system might have over classical AI systems.

2. Technical Challenges and Limitations (200-250 words):
   a) Identify potential technical challenges in implementing your proposed system.
   b) Discuss any limitations or trade-offs inherent in your design.
   c) Propose potential solutions or areas for future research to address these challenges.

3. Privacy Implications (250-300 words):
   a) Analyze how your quantum AI system might impact individual and collective privacy.
   b) Discuss any novel privacy concerns that arise from the quantum nature of the system.
   c) Propose safeguards or guidelines to protect privacy in the deployment of such systems.

4. Security Implications (250-300 words):
   a) Examine how your system could enhance cybersecurity measures.
   b) Discuss potential vulnerabilities or security risks introduced by the quantum AI system.
   c) Analyze the broader implications for national and international security.

5. Ethical Considerations (200-250 words):
   a) Identify key ethical issues raised by the development and deployment of your quantum AI system.
   b) Discuss potential societal impacts, both positive and negative.
   c) Propose an ethical framework for the responsible development of quantum AI in cybersecurity.

6. Future Scenarios (150-200 words):
   a) Describe a potential future scenario (5-10 years ahead) where your quantum AI system is widely deployed.
   b) Discuss how this scenario might change societal norms around privacy and security.
   c) Speculate on potential unintended consequences of this technology.

Ensure your response demonstrates a deep understanding of quantum computing, artificial intelligence, cybersecurity, and ethical reasoning. Be innovative in your design while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must include a detailed design of a quantum AI system that incorporates {t['quantum_feature']} for {t['ai_application']}.",
            "The analysis should cover both privacy and security implications of the proposed system.",
            "The response must demonstrate a clear understanding of quantum computing principles and AI technologies.",
            "The ethical considerations should be thoughtful and comprehensive.",
            "The response should include all six required sections with appropriate content for each.",
            "The speculative elements should be creative yet grounded in current scientific understanding.",
            "The response must adhere to the specified word limits for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
