import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environments = [
            {
                "name": "Methane Ocean World",
                "description": "A cold planet with oceans of liquid methane and ethane, similar to Saturn's moon Titan.",
                "dominant_elements": ["Carbon", "Hydrogen", "Nitrogen"],
                "temperature_range": "90 to 180 Kelvin",
                "pressure": "1.5 Earth atmospheres",
                "gravity": "0.14 g (similar to Titan)"
            },
            {
                "name": "Super-Earth Iron Core",
                "description": "A massive rocky planet with a strong magnetic field and dense metallic atmosphere.",
                "dominant_elements": ["Iron", "Nickel", "Silicon"],
                "temperature_range": "600 to 1200 Kelvin",
                "pressure": "90 Earth atmospheres",
                "gravity": "3 g"
            },
            {
                "name": "Binary Star Habitable Zone",
                "description": "A planet orbiting in the habitable zone of a binary star system, with extreme day-night cycles.",
                "dominant_elements": ["Oxygen", "Carbon", "Nitrogen"],
                "temperature_range": "250 to 350 Kelvin",
                "pressure": "0.8 Earth atmospheres",
                "gravity": "1.2 g"
            },
            {
                "name": "Subsurface Ocean World",
                "description": "An icy world with a global subsurface ocean, similar to Jupiter's moon Europa.",
                "dominant_elements": ["Oxygen", "Hydrogen", "Sulfur"],
                "temperature_range": "50 to 280 Kelvin",
                "pressure": "Varies from near vacuum on surface to 300 Earth atmospheres in ocean depths",
                "gravity": "0.134 g (similar to Europa)"
            }
        ]
        return {
            "1": random.choice(environments),
            "2": random.choice(environments)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical communication system for extraterrestrial life forms inhabiting the following environment: {t['name']} - {t['description']}. Your task has the following parts:

1. Environmental Analysis (200-250 words):
   a) Based on the given environmental parameters, discuss potential adaptations of life forms in this environment.
   b) Analyze how the physical conditions might influence the evolution of sensory and communication systems.
   c) Propose at least two unique challenges for communication in this environment.

2. Communication System Design (300-350 words):
   a) Describe your proposed communication system, including the physical medium or channel used.
   b) Explain how your system leverages or overcomes the environmental constraints.
   c) Detail the encoding method for information transmission, considering the dominant elements available.
   d) Discuss any novel quantum or relativistic effects your system might utilize.

3. Information Theory Analysis (200-250 words):
   a) Estimate the channel capacity of your communication system using Shannon's information theory.
   b) Discuss potential sources of noise or interference and propose methods to mitigate them.
   c) Compare the efficiency of your system to known terrestrial communication methods.

4. Biological Interface (200-250 words):
   a) Propose how the extraterrestrial life forms might biologically interface with your communication system.
   b) Describe any specialized organs or cellular structures that might evolve to utilize this system.
   c) Discuss potential cognitive implications of using this communication method.

5. Interspecies Communication (150-200 words):
   a) Explain how your system could be adapted for communication between the extraterrestrial life forms and human explorers.
   b) Discuss challenges in establishing a common language or understanding.
   c) Propose a method for initial contact and basic information exchange.

Ensure your response demonstrates a deep understanding of physics, biology, and information theory. Use appropriate scientific terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility. Your total response should be between 1050-1300 words.

Environmental Parameters:
- Dominant Elements: {', '.join(t['dominant_elements'])}
- Temperature Range: {t['temperature_range']}
- Pressure: {t['pressure']}
- Gravity: {t['gravity']}
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of physics, biology, and information theory.",
            "The proposed communication system is creative and innovative while remaining scientifically plausible.",
            "The design effectively addresses the unique challenges posed by the given environmental parameters.",
            "The information theory analysis is sound and properly applies concepts like channel capacity and noise mitigation.",
            "The biological interface proposal is well-reasoned and consistent with the environmental constraints.",
            "The interspecies communication section offers plausible solutions for human-alien interaction.",
            "The response effectively synthesizes knowledge from multiple scientific disciplines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
