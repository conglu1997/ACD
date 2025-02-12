import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environments = [
            {"type": "Neutron star surface", "temperature": "1 million K", "gravity": "2 x 10^11 g"},
            {"type": "Gas giant atmosphere", "temperature": "-150°C", "pressure": "1000 atm"},
            {"type": "Subterranean ocean", "temperature": "4°C", "pressure": "1000 atm"}
        ]
        quantum_properties = [
            "Superposition",
            "Entanglement",
            "Quantum tunneling"
        ]
        return {
            "1": {"environment": random.choice(environments), "quantum_property": random.choice(quantum_properties)},
            "2": {"environment": random.choice(environments), "quantum_property": random.choice(quantum_properties)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an innovative quantum-based biosemiotic communication system for a hypothetical silicon-based lifeform living in the following extreme environment: {t['environment']['type']} (Temperature: {t['environment']['temperature']}, {list(t['environment'].keys())[2]}: {t['environment'][list(t['environment'].keys())[2]]}). Your system should incorporate the quantum property of {t['quantum_property']}. Analyze the implications of this system for interspecies communication and information theory.

Structure your response using the following sections and adhere to the word count for each:

1. System Design (250-300 words):
   a) Describe the key components and mechanisms of your quantum-based biosemiotic communication system.
   b) Explain how your system is adapted to the given extreme environment.
   c) Detail how the specified quantum property is utilized in the communication process.
   d) Provide a diagram or detailed description of the system architecture.

2. Biosemiotic Principles (200-250 words):
   a) Explain how your system incorporates biosemiotic principles.
   b) Discuss how meaning is encoded and interpreted in your system.
   c) Analyze the relationship between the silicon-based life form's biology and the communication system.

3. Quantum Information Analysis (200-250 words):
   a) Describe how quantum information theory applies to your communication system.
   b) Discuss the advantages and limitations of using quantum properties in this context.
   c) Provide a simple mathematical formulation or pseudocode for a key quantum aspect of your system.

4. Interspecies Communication Implications (150-200 words):
   a) Analyze the potential for using this system to facilitate communication between different species.
   b) Discuss challenges and opportunities in translating between this system and human communication.

5. Ethical and Philosophical Considerations (150-200 words):
   a) Explore the ethical implications of interacting with silicon-based life forms using this communication system.
   b) Discuss how this system might challenge or expand our understanding of consciousness and intelligence.

6. Experimental Proposal (100-150 words):
   a) Propose an experiment or simulation to test the feasibility and effectiveness of your communication system.
   b) Describe the expected outcomes and how they would be measured.

7. Glossary (100-150 words):
   Provide a glossary of 5-7 key technical terms used in your response, demonstrating your understanding of concepts from quantum mechanics, biosemiotics, and information theory.

Ensure your response demonstrates a deep understanding of quantum mechanics, biosemiotics, and information theory. Be creative and innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations.

Your total response should be between 1150-1500 words. Include a word count at the end of each section and a total word count at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must include a detailed and innovative description of a quantum-based biosemiotic communication system adapted to the given extreme environment: {t['environment']['type']}.",
            f"The system design must creatively incorporate the quantum property of {t['quantum_property']} in a scientifically plausible manner.",
            "The response should demonstrate a clear and in-depth understanding of biosemiotic principles and their application to the communication system.",
            "The submission must include a comprehensive quantum information analysis with a well-explained mathematical formulation or pseudocode.",
            "The response should thoroughly address interspecies communication implications and ethical considerations, showing depth of thought.",
            "An experimental proposal to test the communication system must be included, with clear and measurable outcomes.",
            "The response must include a glossary of 5-7 key technical terms, demonstrating a deep understanding of the interdisciplinary concepts involved.",
            "The overall response should be highly creative, scientifically plausible, and demonstrate exceptional interdisciplinary knowledge integration.",
            "The response must adhere to the specified word counts for each section and the overall word limit."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
