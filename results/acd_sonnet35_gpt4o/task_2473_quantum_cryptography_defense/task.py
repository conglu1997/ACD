import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        infrastructure_types = [
            "Power grid",
            "Financial system",
            "Healthcare network",
            "Transportation system",
            "Government communication network"
        ]
        quantum_attack_vectors = [
            "Shor's algorithm for factoring large numbers",
            "Grover's algorithm for database searching",
            "Quantum simulation of complex systems",
            "Quantum-enhanced machine learning attacks"
        ]
        tasks = {
            "1": {
                "infrastructure": random.choice(infrastructure_types),
                "attack_vector": random.choice(quantum_attack_vectors)
            },
            "2": {
                "infrastructure": random.choice(infrastructure_types),
                "attack_vector": random.choice(quantum_attack_vectors)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-resistant cybersecurity system for a {t['infrastructure']} network, focusing on defending against {t['attack_vector']}. Then, analyze potential vulnerabilities in your system and propose countermeasures. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your quantum-resistant cybersecurity system.
   b) Explain how your system specifically addresses the given quantum attack vector.
   c) Discuss any novel cryptographic algorithms or protocols you've incorporated.
   d) Include a high-level diagram or flowchart of your system architecture.

2. Quantum Resistance Mechanisms (250-300 words):
   a) Detail the specific quantum-resistant mechanisms employed in your system.
   b) Explain how these mechanisms provide security against the specified quantum attack.
   c) Compare the effectiveness of your approach to traditional (non-quantum-resistant) methods.

3. Implementation and Integration (200-250 words):
   a) Describe how your system would be implemented in the given infrastructure network.
   b) Discuss any challenges in integrating quantum-resistant security with existing systems.
   c) Propose a phased approach for transitioning from current security measures to your quantum-resistant system.

4. Vulnerability Analysis (250-300 words):
   a) Identify potential vulnerabilities or weak points in your quantum-resistant system.
   b) Analyze how these vulnerabilities might be exploited by advanced quantum or classical attacks.
   c) Assess the potential impact of these vulnerabilities on the overall security of the infrastructure.

5. Countermeasures and Future-Proofing (200-250 words):
   a) Propose specific countermeasures to address the identified vulnerabilities.
   b) Explain how your system could adapt to future advancements in quantum computing.
   c) Discuss any trade-offs between security, performance, and scalability in your proposed countermeasures.

6. Ethical and Policy Implications (150-200 words):
   a) Analyze the ethical implications of implementing your quantum-resistant system.
   b) Discuss potential policy or regulatory challenges related to quantum-resistant cybersecurity.
   c) Propose guidelines for responsible development and deployment of quantum-resistant systems in critical infrastructure.

Ensure your response demonstrates a deep understanding of quantum computing principles, cryptography, and cybersecurity. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific and practical plausibility.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words. Adhere to the word count limits for each section as specified above. Include a high-level diagram or flowchart of your system architecture as mentioned in section 1.

Your response will be evaluated based on the depth of understanding, technical accuracy, creativity, and completeness of your quantum-resistant cybersecurity system design. A perfect score will be awarded for responses that fully address all aspects of the task with a high degree of expertise and innovation.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum computing, cryptography, and cybersecurity principles",
            "The proposed system architecture is comprehensive and specifically addresses the given quantum attack vector",
            "The quantum resistance mechanisms are well-explained and appropriate for the given infrastructure",
            "The vulnerability analysis is thorough and identifies realistic potential weaknesses",
            "The proposed countermeasures are innovative and address the identified vulnerabilities",
            "The response considers ethical and policy implications of implementing quantum-resistant cybersecurity",
            "The overall solution is creative, technically sound, and demonstrates strategic thinking",
            "The response includes a high-level diagram or flowchart of the system architecture",
            "The response adheres to the specified word count limits for each section"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
