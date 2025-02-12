import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cryptosystems = [
            {
                "name": "Post-Quantum Lattice-Based Cryptosystem",
                "constraint": "must be resilient against Shor's algorithm"
            },
            {
                "name": "Quantum Key Distribution Protocol",
                "constraint": "must address the vulnerability to man-in-the-middle attacks"
            }
        ]
        return {str(i+1): cryptosystem for i, cryptosystem in enumerate(cryptosystems)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-enhanced AI system for cryptanalysis targeting the {t['name']}. Your system {t['constraint']}. Provide your response in the following format:

1. System Architecture (250-300 words):
   a) Describe the key components of your quantum-enhanced AI cryptanalysis system.
   b) Explain how quantum computing principles are integrated with machine learning algorithms.
   c) Detail how your system addresses the specific challenges of the given cryptosystem.

2. Quantum Algorithms (200-250 words):
   a) Identify and explain the quantum algorithms your system employs for cryptanalysis.
   b) Discuss how these algorithms provide an advantage over classical approaches.
   c) Describe any novel quantum algorithmic techniques you've incorporated.

3. AI and Machine Learning Integration (200-250 words):
   a) Explain how AI and machine learning are utilized in your cryptanalysis system.
   b) Describe the training process for your AI components, including data requirements.
   c) Discuss how the AI enhances or complements the quantum computing elements.

4. Cryptanalysis Approach (200-250 words):
   a) Outline your system's step-by-step approach to analyzing and potentially breaking the given cryptosystem.
   b) Explain how your approach leverages both quantum and AI capabilities.
   c) Discuss potential weaknesses in the cryptosystem that your system exploits.

5. Performance Analysis (150-200 words):
   a) Estimate the theoretical performance of your system compared to classical cryptanalysis methods.
   b) Discuss any trade-offs or limitations in your approach.
   c) Propose metrics for evaluating the effectiveness of your quantum-enhanced AI cryptanalysis system.

6. Ethical and Security Implications (150-200 words):
   a) Discuss the ethical considerations of developing advanced cryptanalysis systems.
   b) Analyze potential security risks and propose safeguards against misuse.
   c) Suggest guidelines for responsible development and use of quantum-enhanced AI in cryptography.

Ensure your response demonstrates a deep understanding of quantum computing, artificial intelligence, and cryptography. Be creative in your approach while maintaining scientific and technological plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum computing principles and their application to cryptanalysis",
            "The proposed system effectively integrates AI and machine learning with quantum algorithms",
            f"The design addresses the specific challenges of the {t['name']}",
            f"The system adequately considers the constraint: {t['constraint']}",
            "The cryptanalysis approach is logically sound and leverages both quantum and AI capabilities",
            "The performance analysis and ethical considerations are thorough and well-reasoned"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
