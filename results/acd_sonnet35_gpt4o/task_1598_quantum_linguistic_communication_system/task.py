import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'quantum_principle': 'Entanglement',
                'linguistic_feature': 'Semantic fields',
                'information_theory_concept': 'Channel capacity'
            },
            {
                'quantum_principle': 'Superposition',
                'linguistic_feature': 'Phonological rules',
                'information_theory_concept': 'Data compression'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical quantum-based communication system that incorporates principles from linguistics and information theory to enable instant, secure, and context-aware communication across vast distances. Your system should focus on the quantum principle of {t['quantum_principle']}, the linguistic feature of {t['linguistic_feature']}, and the information theory concept of {t['information_theory_concept']}.

Provide your response in the following format:

1. System Overview (250-300 words):
   a) Describe the key components and architecture of your quantum linguistic communication system.
   b) Explain how {t['quantum_principle']} is utilized in your system's design.
   c) Discuss how {t['linguistic_feature']} is integrated into the communication process.
   d) Elaborate on how {t['information_theory_concept']} is applied to optimize communication.

2. Quantum-Linguistic Interface (200-250 words):
   a) Explain how your system translates linguistic information into quantum states.
   b) Describe the process of encoding semantic and contextual information using quantum properties.
   c) Discuss how {t['linguistic_feature']} influences the quantum encoding process.

3. Information Processing and Transmission (200-250 words):
   a) Detail the quantum mechanisms used for information processing and transmission.
   b) Explain how your system achieves instant communication across vast distances.
   c) Describe how {t['information_theory_concept']} is implemented to enhance efficiency and security.

4. Context-Awareness and Adaptive Communication (150-200 words):
   a) Explain how your system adapts to different communication contexts.
   b) Describe any learning or adaptive mechanisms incorporated into the system.
   c) Discuss how context-awareness impacts the application of {t['quantum_principle']} and {t['linguistic_feature']}.

5. Theoretical Challenges and Solutions (150-200 words):
   a) Identify at least two major theoretical challenges in implementing your system.
   b) Propose potential solutions or research directions to address these challenges.
   c) Discuss any trade-offs or limitations of your proposed solutions.

6. Potential Applications and Implications (150-200 words):
   a) Propose three potential applications of your quantum linguistic communication system.
   b) Discuss the ethical implications and potential societal impacts of your system.
   c) Speculate on how this technology might influence the future of communication and language use.

Ensure your response demonstrates a deep understanding of quantum mechanics, linguistics, and information theory. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Your total response should be between 1100-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['quantum_principle']} and its application in communication systems.",
            f"The integration of {t['linguistic_feature']} into the quantum communication process is innovative and well-explained.",
            f"The application of {t['information_theory_concept']} in the system design is clear and justified.",
            "The quantum-linguistic interface is described in a scientifically plausible manner.",
            "The system's approach to instant, secure, and context-aware communication is creative and well-reasoned.",
            "The response addresses theoretical challenges and proposes thoughtful solutions.",
            "The potential applications and implications of the system are insightful and demonstrate foresight.",
            "The overall response shows strong integration of knowledge from quantum mechanics, linguistics, and information theory.",
            "The response adheres to the specified word limits for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
