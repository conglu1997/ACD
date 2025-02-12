import random
import string

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "quantum_key_distribution", "attack_type": "man_in_the_middle"},
            "2": {"scenario": "post_quantum_cryptography", "attack_type": "shor_algorithm"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        base_instructions = """Design and analyze a quantum computing system for cybersecurity applications in the scenario of {scenario}, then simulate its performance against a {attack_type} attack. Your response should include the following sections:

1. Quantum System Design (300-350 words):
   a) Describe the key components and architecture of your quantum computing system for the given cybersecurity scenario.
   b) Explain the quantum principles and algorithms utilized in your system.
   c) Discuss any novel features or innovations in your design.
   d) Provide a high-level diagram of your system architecture (describe it textually).

2. Cybersecurity Application (250-300 words):
   a) Explain how your quantum system addresses the specific cybersecurity scenario.
   b) Discuss the advantages of your quantum approach over classical methods.
   c) Describe potential limitations or vulnerabilities of your system.

3. Attack Simulation (250-300 words):
   a) Design a simulation of the specified attack type against your quantum cybersecurity system.
   b) Describe the parameters and methodology of your simulation.
   c) Present the results of the simulation, including the system's performance and any vulnerabilities exposed.

4. Comparative Analysis (200-250 words):
   a) Compare your quantum system's performance to that of current classical cybersecurity systems.
   b) Analyze the trade-offs between security, efficiency, and practicality in your approach.
   c) Discuss the potential impact of your system on the cybersecurity landscape.

5. Ethical and Societal Implications (200-250 words):
   a) Discuss the ethical considerations of deploying advanced quantum cybersecurity systems.
   b) Analyze potential societal impacts, both positive and negative.
   c) Propose guidelines for responsible development and use of quantum cybersecurity technologies.

6. Future Developments (150-200 words):
   a) Suggest two potential improvements or expansions to your system.
   b) Discuss how emerging technologies could enhance your system's capabilities.
   c) Propose a related quantum computing challenge in cybersecurity that could be addressed using a similar approach.

Ensure your response demonstrates a deep understanding of quantum computing, cybersecurity, and ethical implications of advanced technologies. Use appropriate terminology and provide clear explanations where necessary. Be creative in your approach while maintaining scientific accuracy and plausibility.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

        return base_instructions.format(scenario=t["scenario"], attack_type=t["attack_type"])

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum computing principles and cybersecurity concepts.",
            "The quantum system design is innovative, well-explained, and appropriate for the given scenario.",
            "The attack simulation is well-designed and provides meaningful insights into the system's performance.",
            "The comparative analysis is thorough and highlights the advantages and limitations of the quantum approach.",
            "Ethical and societal implications are thoughtfully considered and discussed.",
            "The response is well-structured, within the specified word count, and uses appropriate terminology."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
