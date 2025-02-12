import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'infrastructure': 'Power grid',
                'quantum_resource': 'Entanglement-based quantum key distribution',
                'classical_attack': 'Distributed Denial of Service (DDoS)',
                'quantum_attack': 'Shor\'s algorithm'
            },
            {
                'infrastructure': 'Financial system',
                'quantum_resource': 'Quantum random number generator',
                'classical_attack': 'Man-in-the-middle',
                'quantum_attack': 'Grover\'s algorithm'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""As an expert in quantum computing and cybersecurity, you are tasked with designing a cutting-edge quantum-based cryptographic defense system for a critical infrastructure network. Your goal is to create a robust system that can withstand both classical and quantum attacks, ensuring the highest level of security for essential services.

Design a quantum-based cryptographic defense system for a {t['infrastructure']} network, utilizing {t['quantum_resource']} as a key quantum resource. Then, analyze its resilience against both classical and quantum attacks, specifically addressing {t['classical_attack']} and {t['quantum_attack']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your quantum cryptographic defense system.
   b) Explain how {t['quantum_resource']} is integrated into your system.
   c) Detail how your system interacts with the existing {t['infrastructure']} network.
   d) Include a high-level diagram or flowchart of your system architecture (describe this textually, using ASCII characters if necessary).

2. Quantum Cryptographic Protocol (250-300 words):
   a) Describe the quantum cryptographic protocol used in your system.
   b) Explain how this protocol leverages {t['quantum_resource']}.
   c) Discuss any novel features or improvements you've introduced to enhance security.

3. Classical Attack Resilience (200-250 words):
   a) Analyze how your system defends against {t['classical_attack']}.
   b) Describe any potential vulnerabilities and how you address them.
   c) Compare the effectiveness of your quantum-based defense to traditional methods.

4. Quantum Attack Resilience (200-250 words):
   a) Evaluate your system's resilience against {t['quantum_attack']}.
   b) Explain any quantum-resistant features you've incorporated.
   c) Discuss the long-term implications of quantum attacks on your system.

5. Implementation and Scalability (200-250 words):
   a) Describe the practical challenges in implementing your system in a real-world {t['infrastructure']}.
   b) Discuss how your system scales to protect large, complex networks.
   c) Propose a phased approach for transitioning from classical to quantum-based security.

6. Ethical and Policy Implications (150-200 words):
   a) Discuss the ethical considerations of implementing such advanced cryptographic systems.
   b) Analyze potential societal impacts of widespread quantum-based cybersecurity.
   c) Propose policy guidelines for the responsible development and use of quantum cryptographic defenses.

Ensure your response demonstrates a deep understanding of quantum mechanics, cryptography, network security, and ethics. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific and practical plausibility.

Format your response with clear headings for each section. Your total response should be between 1300-1600 words. Include relevant citations to scientific literature throughout your response to support your arguments and demonstrate depth of knowledge."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of quantum cryptography and {t['quantum_resource']}.",
            f"The system architecture effectively integrates quantum resources with the {t['infrastructure']} network.",
            f"The analysis of resilience against {t['classical_attack']} and {t['quantum_attack']} is thorough and well-reasoned.",
            "The proposed implementation and scalability plans are practical and well-considered.",
            "The discussion of ethical and policy implications is insightful and comprehensive.",
            "The overall response shows strong integration of knowledge from quantum physics, cryptography, and cybersecurity.",
            "The response includes relevant citations to scientific literature.",
            "The response adheres to the specified word count limits for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
