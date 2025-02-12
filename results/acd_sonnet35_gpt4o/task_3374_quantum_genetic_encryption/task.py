import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        genetic_elements = [
            {"element": "DNA sequence", "quantum_concept": "superposition"},
            {"element": "Gene expression", "quantum_concept": "entanglement"},
            {"element": "Epigenetic markers", "quantum_concept": "quantum tunneling"},
            {"element": "Protein folding", "quantum_concept": "quantum annealing"}
        ]
        applications = [
            "Personalized medicine",
            "Genetic disease prevention",
            "Synthetic biology",
            "Bioweapon defense"
        ]
        return {
            "1": {
                "genetic_element": random.choice(genetic_elements),
                "application": random.choice(applications)
            },
            "2": {
                "genetic_element": random.choice(genetic_elements),
                "application": random.choice(applications)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical quantum-based genetic encryption system for protecting and transmitting genetic information, focusing on the genetic element of {t['genetic_element']['element']} using the quantum concept of {t['genetic_element']['quantum_concept']}. Then, analyze its potential applications and ethical implications in {t['application']}. Your response should include:

1. Quantum Genetic Encryption System Design (300-350 words):
   a) Describe the key components and mechanisms of your encryption system.
   b) Explain how it incorporates the specified quantum concept in genetic information processing.
   c) Detail how the system protects and transmits the given genetic element.
   d) Include an innovative feature that distinguishes your system from classical encryption methods.

2. Quantum-Genetic Integration (250-300 words):
   a) Explain the theoretical basis for applying the given quantum concept to the specified genetic element.
   b) Describe how your system represents and processes genetic data using quantum principles.
   c) Discuss potential advantages and challenges of this quantum-genetic approach.

3. Cryptographic Analysis (200-250 words):
   a) Analyze the security of your encryption system against both classical and quantum attacks.
   b) Discuss the system's key generation, distribution, and management processes.
   c) Explain how your system ensures data integrity and authenticity.

4. Application in {t['application']} (200-250 words):
   a) Describe how your quantum genetic encryption system could be applied in this field.
   b) Discuss potential benefits and risks of using this technology in this context.
   c) Propose a specific use case and explain its implementation.

5. Ethical Implications and Guidelines (200-250 words):
   a) Analyze ethical considerations related to quantum encryption of genetic information.
   b) Discuss potential societal impacts, both positive and negative.
   c) Propose guidelines for responsible development and use of this technology.

6. Future Directions and Limitations (150-200 words):
   a) Suggest potential improvements or extensions to your quantum genetic encryption system.
   b) Discuss current technological limitations and how they might be overcome.
   c) Propose a related research question that could further advance this field.

Ensure your response demonstrates a deep understanding of quantum physics, genetics, cryptography, and bioethics. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response effectively integrates the quantum concept of {t['genetic_element']['quantum_concept']} with the genetic element of {t['genetic_element']['element']}.",
            f"The proposed system and its application in {t['application']} are innovative yet scientifically plausible.",
            "The response demonstrates a deep understanding of quantum physics, genetics, cryptography, and bioethics.",
            "The ethical analysis is thorough and considers multiple perspectives."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
