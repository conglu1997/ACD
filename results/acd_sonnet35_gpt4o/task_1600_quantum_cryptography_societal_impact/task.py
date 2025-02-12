import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "city_name": "QuantumPolis",
                "population": "10 million",
                "key_infrastructure": "Quantum Internet",
                "main_concern": "Data Privacy"
            },
            {
                "city_name": "NeoQuantica",
                "population": "5 million",
                "key_infrastructure": "Quantum Energy Grid",
                "main_concern": "Infrastructure Security"
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel quantum cryptographic system for the futuristic smart city of {t['city_name']} (population: {t['population']}) and analyze its societal implications. The city's key infrastructure is its {t['key_infrastructure']}, and the main concern is {t['main_concern']}. Your response should include:

1. Quantum Cryptographic System Design (300-350 words):
   a) Describe the key components and mechanisms of your quantum cryptographic system.
   b) Explain how it leverages quantum principles to enhance security.
   c) Detail how the system integrates with the city's {t['key_infrastructure']}.
   d) Address how your system specifically tackles the main concern of {t['main_concern']}.
   e) Include at least one equation or mathematical representation related to your quantum cryptographic system.
   f) Provide a textual description of a diagram or schematic representation of your quantum cryptographic system.
   g) Discuss specific quantum cryptographic protocols or algorithms used in your system.

2. Implementation and Scalability (200-250 words):
   a) Outline the steps required to implement your system city-wide.
   b) Discuss potential challenges in scaling the system for a population of {t['population']}.
   c) Propose solutions to overcome these challenges.

3. Security Analysis (200-250 words):
   a) Analyze potential vulnerabilities in your quantum cryptographic system.
   b) Compare its security level to current classical cryptographic systems.
   c) Discuss how it might fare against future quantum computing attacks.
   d) Explore potential quantum-resistant classical algorithms and their role in your system.

4. Societal Impact Assessment (250-300 words):
   a) Evaluate the potential positive and negative societal impacts of implementing your system.
   b) Discuss how it might affect citizens' daily lives, privacy, and civil liberties.
   c) Analyze potential economic impacts on the city and its businesses.
   d) Consider any unintended consequences or ethical dilemmas that might arise.

5. Regulatory Framework (150-200 words):
   a) Propose a regulatory framework for the ethical use and governance of your quantum cryptographic system.
   b) Discuss how to balance security needs with individual privacy rights.
   c) Suggest mechanisms for public oversight and accountability.

6. Future Prospects (150-200 words):
   a) Speculate on how your system might evolve over the next 50 years.
   b) Discuss potential applications beyond cryptography.
   c) Consider how it might impact global geopolitics and digital sovereignty.

Ensure your response demonstrates a deep understanding of quantum computing, cryptography, urban planning, and ethics. Use appropriate technical terminology and provide clear explanations where necessary. Be innovative in your approach while maintaining scientific plausibility and considering real-world implications.

Format your response with clear headings for each section and number your paragraphs within each section. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The quantum cryptographic system design must be tailored to the city of {t['city_name']} and its {t['key_infrastructure']}",
            f"The response should specifically address the main concern of {t['main_concern']}",
            "The system design should be scientifically plausible and demonstrate understanding of quantum principles",
            "The response should include at least one relevant equation or mathematical representation",
            "The response should include a textual description of a diagram or schematic representation of the quantum cryptographic system",
            "The response should discuss specific quantum cryptographic protocols or algorithms used in the system",
            "The implementation plan should consider the challenges of scaling for a population of {t['population']}",
            "The security analysis should compare the system to classical cryptography, consider future quantum attacks, and explore quantum-resistant classical algorithms",
            "The societal impact assessment should consider both positive and negative effects, including ethical implications",
            "The proposed regulatory framework should balance security needs with individual privacy rights",
            "The response should demonstrate interdisciplinary knowledge integration across quantum computing, cryptography, urban planning, and ethics",
            "The response should be formatted with clear headings for each section, numbered as instructed",
            "The total response should be between 1250-1550 words",
            "The response should include substantive content for all required sections (1-6)"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
