import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "scenario": "secure communication between two space stations",
                "constraint": "limited by the effects of relativistic time dilation"
            },
            {
                "scenario": "quantum money for a post-quantum economy",
                "constraint": "must be immune to double-spending attacks"
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(scenarios)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel quantum cryptographic protocol for {t['scenario']}. Your protocol should be {t['constraint']}. Provide your response in the following format:

1. Protocol Design (250-300 words):
   a) Describe the key components of your quantum cryptographic protocol.
   b) Explain how it leverages quantum mechanical principles to achieve security.
   c) Detail the step-by-step process of how the protocol would work.
   d) Discuss how your protocol addresses the given constraint.

2. Security Analysis (200-250 words):
   a) Analyze the security of your protocol against known quantum and classical attacks.
   b) Identify potential vulnerabilities and propose mitigations.
   c) Compare the security of your protocol to existing quantum cryptographic methods.

3. Implementation Challenges (200-250 words):
   a) Discuss the main technical challenges in implementing your protocol.
   b) Propose solutions or approaches to overcome these challenges.
   c) Analyze the feasibility of your protocol with current or near-future quantum technologies.

4. Information-Theoretic Analysis (150-200 words):
   a) Provide a brief information-theoretic analysis of your protocol.
   b) Calculate or estimate the protocol's key rate and/or channel capacity.
   c) Explain how quantum effects contribute to the information-theoretic security.

5. Societal Implications (150-200 words):
   a) Discuss potential applications and impacts of your protocol beyond the given scenario.
   b) Analyze ethical considerations or potential misuse of the technology.
   c) Propose guidelines or policies for responsible development and use of your protocol.

Ensure your response demonstrates a deep understanding of quantum mechanics, cryptography, and information theory. Be creative in your design while maintaining scientific plausibility and addressing the specific challenges of the given scenario.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum mechanics and its application to cryptography",
            "The proposed protocol is novel and creative, while remaining scientifically plausible",
            f"The protocol effectively addresses the given scenario: {t['scenario']}",
            f"The design considers and accounts for the specified constraint: {t['constraint']}",
            "The security analysis is thorough and considers both quantum and classical attack vectors",
            "The implementation challenges and proposed solutions are realistic and well-reasoned",
            "The information-theoretic analysis is accurate and demonstrates understanding of quantum information theory",
            "The discussion of societal implications shows critical thinking about the broader impacts of the technology"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
