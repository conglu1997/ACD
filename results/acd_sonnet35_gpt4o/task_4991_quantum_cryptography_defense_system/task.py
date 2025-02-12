import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                'infrastructure': 'power grid',
                'quantum_protocol': 'BB84',
                'threat_model': 'state-sponsored attacks',
                'ethical_concern': 'privacy vs. national security',
                'key_length': '256 bits',
                'network_nodes': '1000'
            },
            {
                'infrastructure': 'financial system',
                'quantum_protocol': 'E91',
                'threat_model': 'quantum computer-aided hacking',
                'ethical_concern': 'economic inequality',
                'key_length': '512 bits',
                'network_nodes': '10000'
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(scenarios)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum cryptography-based cybersecurity system for protecting the {t['infrastructure']} against {t['threat_model']}, using the {t['quantum_protocol']} protocol with a key length of {t['key_length']} and a network of {t['network_nodes']} nodes. Then, analyze its potential impact on the global cybersecurity landscape. Your response should include the following sections:

1. System Architecture (250-300 words):
   a) Describe the key components of your quantum cryptography-based cybersecurity system.
   b) Explain how you integrate the {t['quantum_protocol']} protocol into your system.
   c) Provide a high-level diagram or pseudocode illustrating the system's architecture (describe it textually).

2. Quantum Cryptography Implementation (200-250 words):
   a) Explain the principles of the {t['quantum_protocol']} protocol and how it enhances security.
   b) Describe how your system generates and distributes quantum keys of {t['key_length']} length.
   c) Include at least one relevant mathematical equation or formula related to the quantum key distribution process.

3. Threat Model and Defense Mechanisms (200-250 words):
   a) Analyze the {t['threat_model']} scenario and potential vulnerabilities in the {t['infrastructure']}.
   b) Explain how your quantum cryptography system mitigates these specific threats.

4. Performance and Scalability (150-200 words):
   a) Predict the performance of your system in terms of key generation rate and security level.
   b) Discuss how your system scales to protect {t['network_nodes']} nodes in the {t['infrastructure']}.

5. Global Cybersecurity Impact (200-250 words):
   a) Analyze how widespread adoption of your system could affect global cybersecurity dynamics.
   b) Discuss potential shifts in cyber warfare and espionage tactics.

6. Ethical and Societal Implications (150-200 words):
   a) Address the ethical concern of {t['ethical_concern']} in the context of your system.
   b) Propose guidelines for responsible development and use of quantum cybersecurity technologies.

Ensure your response demonstrates a deep understanding of quantum mechanics, cryptography, cybersecurity, and complex systems analysis. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific and practical plausibility.

Format your response with clear headings for each section, numbered as above. Use appropriate subheadings (a, b, c) within each section. Your total response should be between 1150-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates understanding of quantum cryptography, particularly the {t['quantum_protocol']} protocol with {t['key_length']} key length.",
            f"The system design addresses the protection of {t['infrastructure']} with {t['network_nodes']} nodes against {t['threat_model']}.",
            "The response includes a high-level diagram or pseudocode of the system architecture.",
            "The quantum cryptography implementation section includes at least one relevant mathematical equation or formula.",
            "The threat model and defense mechanisms are adequately explained.",
            "The performance and scalability section includes some quantitative predictions or comparisons.",
            "The global cybersecurity impact analysis considers multiple perspectives.",
            f"The ethical implications, particularly regarding {t['ethical_concern']}, are discussed.",
            "The response is well-structured, clear, and within the specified word count for each section and overall."
        ]
        scores = [float(eval_with_llm_judge(instructions, submission, [criterion])) for criterion in criteria]
        return sum(scores) / len(criteria)
