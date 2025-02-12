import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biomes = [
            "Tropical Rainforest",
            "Coral Reef",
            "Arctic Tundra",
            "Temperate Grassland",
            "Mangrove Swamp",
            "Alpine Forest"
        ]
        quantum_concepts = [
            "Superposition",
            "Entanglement",
            "Quantum Tunneling",
            "Quantum Interference"
        ]
        climate_scenarios = [
            "Rapid warming (3°C increase over 50 years)",
            "Increased frequency of extreme weather events",
            "Sea level rise (1 meter over 50 years)",
            "Shifts in precipitation patterns"
        ]
        tasks = {}
        for i in range(2):
            biome = random.choice(biomes)
            quantum_concept = random.choice(quantum_concepts)
            climate_scenario = random.choice(climate_scenarios)
            tasks[str(i+1)] = {
                "biome": biome,
                "quantum_concept": quantum_concept,
                "climate_scenario": climate_scenario
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical quantum-inspired neural network model that simulates ecosystem dynamics and apply it to predict the impact of climate change on a {t['biome']}. Your model should incorporate the quantum concept of {t['quantum_concept']} and address the climate scenario: {t['climate_scenario']}. Provide your response in the following format:

1. Quantum-Neural-Ecological Model (300-350 words):
   a) Describe the key components of your quantum-inspired neural network model.
   b) Explain how you incorporate {t['quantum_concept']} into your model's architecture or functioning.
   c) Detail how your model simulates ecosystem dynamics, particularly for a {t['biome']}.
   d) Discuss how your model differs from classical ecological modeling approaches.
   e) Include a simple diagram or schematic representation of your model (describe it textually).

2. Climate Change Integration (200-250 words):
   a) Explain how your model incorporates the given climate change scenario: {t['climate_scenario']}.
   b) Describe the method for simulating various climate change impacts on the {t['biome']}.
   c) Discuss how your model accounts for complex ecological interactions under changing conditions.

3. Quantum Algorithm Application (200-250 words):
   a) Provide a high-level description of a quantum algorithm used in your model.
   b) Explain how this algorithm enhances the simulation or prediction process.
   c) Discuss any theoretical advantages this approach might have over classical methods.

4. Prediction and Analysis (250-300 words):
   a) Apply your model to predict the impact of the given climate scenario on the {t['biome']} over the next 50 years.
   b) Provide specific examples of predicted changes in species composition, biodiversity, or ecosystem services.
   c) Explain how the quantum aspects of your model contribute to these predictions.
   d) Compare your model's predictions to those of traditional ecological models.

5. Limitations and Future Improvements (150-200 words):
   a) Discuss the current limitations of your proposed model.
   b) Suggest potential future improvements or research directions.
   c) Speculate on how this technology might evolve and its potential long-term impact on ecological research and conservation.

6. Ethical and Practical Implications (150-200 words):
   a) Discuss potential ethical concerns of using quantum-inspired models for ecological predictions.
   b) Explore how this technology might impact conservation strategies and environmental policy-making.
   c) Address potential risks of over-relying on complex models for ecological decision-making.

Ensure your response demonstrates a deep understanding of quantum computing concepts, neural network principles, and ecological systems. Be creative in your approach while maintaining scientific plausibility. Your total response should be between 1250-1550 words.

Format your response with clear headings for each section and use subheadings where appropriate."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum computing, neural networks, and ecology",
            f"The model effectively incorporates the quantum concept of {t['quantum_concept']}",
            f"The ecological predictions for the {t['biome']} under the given climate scenario are plausible and well-reasoned",
            "The response shows creativity and innovation while maintaining scientific credibility",
            "The ethical and practical implications are thoughtfully considered",
            "The response includes a clear comparison to traditional ecological modeling techniques"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
