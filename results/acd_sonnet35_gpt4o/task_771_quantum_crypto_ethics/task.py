import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                'quantum_protocol': 'BB84',
                'application': 'financial transactions',
                'ethical_concern': 'privacy preservation'
            },
            {
                'quantum_protocol': 'E91',
                'application': 'voting systems',
                'ethical_concern': 'fairness and equality'
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum cryptography system based on the {t['quantum_protocol']} protocol for use in {t['application']}, and analyze its ethical implications in a post-quantum world, with a focus on {t['ethical_concern']}. Your response should include:

1. Quantum Cryptography System Design (300-350 words):
   a) Explain the basic principles of the {t['quantum_protocol']} protocol.
   b) Describe how you would implement this protocol for {t['application']}.
   c) Discuss any modifications or enhancements you would make to the protocol for this specific application.
   d) Address potential vulnerabilities and how you would mitigate them.
   e) Provide a concrete example of how your system would work in a specific scenario related to {t['application']}.

2. Post-Quantum World Scenario (200-250 words):
   a) Describe a plausible scenario where quantum computers have become widespread.
   b) Discuss how this scenario would impact traditional cryptography.
   c) Explain why quantum cryptography remains secure in this scenario.
   d) Illustrate with a specific example of how a quantum attack might work on a traditional system vs. your quantum system.

3. Ethical Analysis (250-300 words):
   a) Identify at least three ethical implications of implementing your quantum cryptography system for {t['application']}.
   b) Analyze these implications in depth, with a particular focus on {t['ethical_concern']}.
   c) Discuss any potential misuse scenarios and their consequences.
   d) Provide a real-world analogy to help explain one of the ethical implications to a non-expert audience.

4. Mitigation Strategies (200-250 words):
   a) Propose strategies to address the ethical concerns you've identified.
   b) Explain how these strategies could be implemented in practice.
   c) Discuss any trade-offs between security, usability, and ethical considerations.
   d) Suggest a specific policy or regulation that could help enforce ethical use of your system.

5. Future Implications (150-200 words):
   a) Speculate on how widespread adoption of quantum cryptography might change society.
   b) Discuss potential long-term consequences for privacy, security, and trust in digital systems.
   c) Propose a framework for ongoing ethical evaluation of quantum cryptography systems.
   d) Describe a potential future scenario that illustrates both the benefits and risks of ubiquitous quantum cryptography.

Ensure your response demonstrates a deep understanding of quantum mechanics, cryptography, and ethical reasoning. Use technical terminology appropriately, but also provide clear explanations that a non-expert could understand. Be creative in your approach while maintaining scientific and technological plausibility.

Format your response using clear headings for each section. Your total response should be between 1100-1350 words. Begin each section with the heading (e.g., '1. Quantum Cryptography System Design:') followed by your response for that section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of the {t['quantum_protocol']} protocol and its application to {t['application']}, including a concrete example.",
            "The post-quantum world scenario is plausible, well-reasoned, and includes a specific example of a quantum attack.",
            f"The ethical analysis thoroughly addresses {t['ethical_concern']} and other relevant ethical implications, with a clear real-world analogy.",
            "The proposed mitigation strategies are practical, address the identified ethical concerns, and include a specific policy suggestion.",
            "The discussion of future implications shows deep thought about the long-term consequences of quantum cryptography, including a detailed future scenario.",
            "The response balances technical accuracy with clear explanations accessible to a non-expert audience.",
            "The response follows the specified format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
