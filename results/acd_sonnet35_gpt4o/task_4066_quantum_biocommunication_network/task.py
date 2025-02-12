import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biological_systems = [
            {
                'system': 'Avian magnetoreception',
                'quantum_effect': 'Radical pair mechanism',
                'application': 'Long-distance secure communication'
            },
            {
                'system': 'Photosynthetic light-harvesting',
                'quantum_effect': 'Quantum coherence',
                'application': 'Energy-efficient data transmission'
            },
            {
                'system': 'Olfactory receptors',
                'quantum_effect': 'Quantum tunneling',
                'application': 'Chemical signal detection and analysis'
            },
            {
                'system': 'DNA mutation',
                'quantum_effect': 'Proton tunneling',
                'application': 'Quantum-based data storage and replication'
            }
        ]
        return {str(i+1): system for i, system in enumerate(random.sample(biological_systems, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired communication network based on the biological system of {t['system']}, which exhibits the quantum effect of {t['quantum_effect']}. Your design should aim to create a novel communication system with potential applications in {t['application']}. Your response should include:

1. Quantum-Bio-Inspired Network Architecture (300-350 words):
   a) Describe the key components of your communication network.
   b) Explain how the quantum effect from the biological system is incorporated into your design.
   c) Detail how your network processes and transmits information.
   d) Provide a high-level diagram or schematic of your network architecture (describe this textually).

2. Quantum-Classical Interface (200-250 words):
   a) Explain how your network interfaces between quantum and classical components.
   b) Discuss any novel approaches you've developed to handle this interface.
   c) Address potential challenges in implementing this interface and propose solutions.

3. Information Theory Analysis (200-250 words):
   a) Analyze the information capacity and efficiency of your network using relevant metrics.
   b) Compare your network's performance to classical communication systems.
   c) Discuss any unique properties of information flow in your quantum-bio-inspired network.

4. Application Scenario (250-300 words):
   a) Describe a specific scenario where your network could be applied to {t['application']}.
   b) Explain the advantages of your system over current technologies in this application.
   c) Discuss any limitations or potential drawbacks of your system in this context.
   d) Propose a method to experimentally validate your network's performance in this scenario.

5. Ethical Implications and Future Directions (200-250 words):
   a) Discuss potential ethical considerations in implementing your communication network.
   b) Analyze possible societal impacts of widespread adoption of your technology.
   c) Suggest two future research directions to enhance or expand your network design.
   d) Propose a potential integration of your system with another emerging technology.

6. References and Glossary (100-150 words):
   a) Cite at least three relevant scientific papers or theories that support your design.
   b) Provide a brief glossary of 5-7 key technical terms used in your response, ensuring correct usage and understanding.

Ensure your response demonstrates a deep understanding of quantum physics, biology, and information theory. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of the quantum effect {t['quantum_effect']} in the biological system {t['system']}.",
            "The proposed communication network design is innovative and scientifically plausible.",
            "The quantum-classical interface is well-explained and addresses potential challenges.",
            "The information theory analysis is thorough and compares the proposed system to classical alternatives.",
            f"The application scenario for {t['application']} is well-developed and includes a method for experimental validation.",
            "Ethical implications and future directions are thoughtfully considered.",
            "The response uses appropriate technical terminology from quantum physics, biology, and information theory.",
            "The analysis is well-structured, clear, and within the specified word count for each section.",
            "The response includes relevant scientific citations and a glossary of key terms."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
