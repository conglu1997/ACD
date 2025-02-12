import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "quantum_principle": "Superposition",
                "cryptographic_element": "Key Distribution",
                "ai_technique": "Quantum Neural Networks"
            },
            {
                "quantum_principle": "Entanglement",
                "cryptographic_element": "Secure Communication",
                "ai_technique": "Quantum Reinforcement Learning"
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired AI system for creating and analyzing advanced cryptographic protocols, focusing on the quantum principle of {t['quantum_principle']}, the cryptographic element of {t['cryptographic_element']}, and utilizing {t['ai_technique']} as the primary AI component. Then, apply your system to a specific cryptographic challenge.

Your response should include the following sections:

1. Quantum-Inspired AI System Architecture (300-350 words):
   a) Describe the main components of your quantum-inspired AI system.
   b) Explain how you incorporate the specified quantum principle into your system design.
   c) Detail how your system integrates the given AI technique.
   d) Discuss any novel features that allow your system to handle cryptographic tasks effectively.

2. Cryptographic Protocol Design (250-300 words):
   a) Outline a new cryptographic protocol that your system could generate, focusing on the specified cryptographic element.
   b) Explain how this protocol leverages quantum-inspired concepts.
   c) Discuss the potential advantages of your protocol over classical cryptographic approaches.

3. AI-Driven Cryptanalysis (250-300 words):
   a) Describe how your system would approach the analysis of cryptographic protocols.
   b) Explain any quantum-inspired techniques used in the cryptanalysis process.
   c) Discuss how the AI component contributes to identifying potential vulnerabilities or strengths in cryptographic systems.

4. Specific Cryptographic Challenge (200-250 words):
   a) Present a specific cryptographic challenge related to the given cryptographic element.
   b) Explain how your quantum-inspired AI system would approach solving this challenge.
   c) Discuss any unique insights or solutions your system might provide.

5. Quantum-Classical Hybrid Approach (200-250 words):
   a) Explain how your system balances quantum-inspired methods with classical computing techniques.
   b) Discuss the potential advantages and limitations of this hybrid approach.
   c) Propose a method for optimizing the integration of quantum and classical components.

6. Ethical and Security Implications (150-200 words):
   a) Discuss potential ethical concerns related to the development and use of quantum-inspired AI cryptosystems.
   b) Analyze possible impacts on current cryptographic standards and practices.
   c) Propose guidelines for responsible development and deployment of such systems.

7. Future Directions and Applications (150-200 words):
   a) Suggest two potential extensions or improvements to your quantum-inspired AI cryptosystem.
   b) Discuss how your approach might be adapted to other areas of cryptography or computer security.
   c) Speculate on the long-term implications of this technology for the field of cryptography.

Ensure your response demonstrates a deep understanding of quantum computing principles, cryptography, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific and mathematical rigor.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1500-1850 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The system effectively integrates the quantum principle of {t['quantum_principle']}, the cryptographic element of {t['cryptographic_element']}, and {t['ai_technique']}.",
            "The response demonstrates a deep understanding of quantum computing concepts and their application to cryptography.",
            "The proposed cryptographic protocol is innovative and leverages quantum-inspired concepts effectively.",
            "The AI-driven cryptanalysis approach is well-explained and plausible.",
            "The specific cryptographic challenge and its proposed solution are relevant and well-reasoned.",
            "The quantum-classical hybrid approach is well-justified and its trade-offs are properly analyzed.",
            "Ethical and security implications are thoroughly discussed.",
            "Future directions and applications are insightful and demonstrate forward-thinking.",
            "The overall response is creative, scientifically plausible, and well-structured.",
            "All required sections and subpoints are addressed in the response."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
