import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "planet_name": "Zeta Proxima b",
                "gravity": "1.3 times Earth's gravity",
                "atmosphere": "Nitrogen-rich, with trace amounts of oxygen and methane",
                "temperature_range": "-20°C to 40°C",
                "day_length": "36 Earth hours",
                "water_availability": "Scarce, mainly in the form of underground reservoirs"
            },
            {
                "planet_name": "Epsilon Eridani c",
                "gravity": "0.8 times Earth's gravity",
                "atmosphere": "Dense carbon dioxide atmosphere with sulfuric acid clouds",
                "temperature_range": "60°C to 150°C",
                "day_length": "120 Earth hours",
                "water_availability": "Abundant, with global oceans and frequent acid rain"
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical ecosystem for the exoplanet {t['planet_name']} with the following environmental parameters:

- Gravity: {t['gravity']}
- Atmosphere: {t['atmosphere']}
- Temperature range: {t['temperature_range']}
- Day length: {t['day_length']}
- Water availability: {t['water_availability']}

Your task is to create a scientifically plausible and ecologically balanced ecosystem for this exoplanet. Your response should include:

1. Dominant Life Forms (200-250 words):
   Describe 3-5 main species that have evolved to thrive in this environment. For each species, explain:
   a) Its physical adaptations to the planet's conditions
   b) Its role in the ecosystem (e.g., primary producer, predator, decomposer)
   c) How it interacts with other species in the ecosystem

2. Energy Flow and Nutrient Cycling (150-200 words):
   Explain how energy flows through your ecosystem and how essential nutrients are cycled. Include:
   a) The primary energy source for the ecosystem
   b) At least one unique biochemical process adapted to the planet's conditions
   c) A brief description of a food web involving at least three trophic levels

3. Environmental Challenges and Adaptations (150-200 words):
   Discuss how the life forms in your ecosystem have adapted to overcome at least two major environmental challenges posed by the planet's conditions.

4. Ecosystem Stability and Resilience (100-150 words):
   Explain how your ecosystem maintains balance and resilience in the face of potential disturbances or extreme events.

5. Potential for Complex Life (100-150 words):
   Assess the potential for the evolution of complex, possibly intelligent life in this ecosystem. Provide reasoning for your assessment based on the planet's conditions and the ecosystem you've designed.

Ensure your response is creative yet grounded in scientific principles. Use appropriate scientific terminology and provide explanations where necessary. Your total response should be between 700-950 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The ecosystem design is scientifically plausible and ecologically balanced",
            "The response addresses all required sections (Dominant Life Forms, Energy Flow and Nutrient Cycling, Environmental Challenges and Adaptations, Ecosystem Stability and Resilience, Potential for Complex Life)",
            "The described life forms and processes are well-adapted to the given planetary conditions",
            "The explanation demonstrates a strong understanding of ecological principles and creative problem-solving",
            "The response uses appropriate scientific terminology and provides clear explanations",
            "The ecosystem design is original and demonstrates creative thinking"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
