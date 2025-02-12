import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                'quantum_property': 'superposition',
                'cryptographic_goal': 'key distribution',
                'application_domain': 'financial transactions'
            },
            {
                'quantum_property': 'entanglement',
                'cryptographic_goal': 'secure communication',
                'application_domain': 'military operations'
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel quantum cryptography protocol that utilizes the quantum property of {t['quantum_property']} to achieve the cryptographic goal of {t['cryptographic_goal']}. Your protocol should be applicable in the domain of {t['application_domain']}. Provide your response in the following format:

1. Protocol Design (250-300 words):
   a) Describe the key components and steps of your quantum cryptography protocol.
   b) Explain how your protocol leverages {t['quantum_property']} to achieve {t['cryptographic_goal']}.
   c) Include a diagram or step-by-step representation of your protocol (describe it textually).
   d) Provide at least one mathematical formula or equation that is central to your protocol's functioning.

2. Security Analysis (200-250 words):
   a) Analyze the security strengths of your protocol.
   b) Identify potential vulnerabilities or attack vectors.
   c) Compare the security of your protocol to existing classical and quantum cryptography methods.

3. Efficiency and Scalability (150-200 words):
   a) Discuss the computational complexity and resource requirements of your protocol.
   b) Analyze its scalability for practical implementation in {t['application_domain']}.
   c) Propose optimizations or trade-offs to enhance efficiency.

4. Real-world Application (200-250 words):
   a) Describe how your protocol could be implemented in {t['application_domain']}.
   b) Discuss potential challenges and solutions for real-world deployment.
   c) Analyze the advantages your protocol offers over existing solutions in this domain.

5. Ethical and Societal Implications (150-200 words):
   a) Discuss the ethical considerations of implementing your quantum cryptography protocol.
   b) Analyze potential societal impacts, both positive and negative.
   c) Propose guidelines or policies for responsible use of your protocol.

6. Future Research Directions (100-150 words):
   a) Suggest two potential research projects to further develop or improve your protocol.
   b) Briefly describe the methodology and expected outcomes of these projects.

Ensure your response demonstrates a deep understanding of both quantum mechanics and cryptography principles. Use technical terminology appropriately and provide explanations where necessary. Your response should be technically sound and comprehensive, with a high level of detail and accuracy. Be creative in your design while maintaining scientific plausibility. Your total response should be between 1050-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The protocol design clearly incorporates the quantum property of {t['quantum_property']} to achieve {t['cryptographic_goal']}.",
            "The security analysis demonstrates a thorough understanding of both quantum and classical cryptography principles.",
            "The efficiency and scalability discussion shows consideration of practical implementation challenges.",
            f"The real-world application section provides a plausible implementation in {t['application_domain']}.",
            "The ethical and societal implications are thoughtfully considered.",
            "The response demonstrates creativity and innovation while maintaining scientific accuracy.",
            "At least one relevant mathematical formula or equation is included and correctly explained.",
            "The response shows a high level of technical depth and comprehensive understanding of the subject matter."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
