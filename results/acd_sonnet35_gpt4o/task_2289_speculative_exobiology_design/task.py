import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        exoplanets = [
            {
                "name": "Proxima Centauri b",
                "conditions": {
                    "gravity": "1.27 Earth's gravity",
                    "atmosphere": "Thin, mostly hydrogen and helium",
                    "temperature": "Average -40°C to 30°C",
                    "radiation": "High levels of X-ray and ultraviolet radiation"
                }
            },
            {
                "name": "TRAPPIST-1e",
                "conditions": {
                    "gravity": "0.92 Earth's gravity",
                    "atmosphere": "Dense, possibly water-rich",
                    "temperature": "Average 0°C to 100°C",
                    "radiation": "Moderate stellar radiation"
                }
            },
            {
                "name": "K2-18b",
                "conditions": {
                    "gravity": "2.6 Earth's gravity",
                    "atmosphere": "Hydrogen-rich, potential water clouds",
                    "temperature": "Average -73°C to 47°C",
                    "radiation": "Low stellar radiation"
                }
            }
        ]
        return {str(i+1): exoplanet for i, exoplanet in enumerate(random.sample(exoplanets, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical alien life form that could evolve on the exoplanet {t['name']}, given the following planetary conditions:

{', '.join(f'{key}: {value}' for key, value in t['conditions'].items())}

Your response should include the following sections:

1. Organism Description (250-300 words):
   a) Provide a detailed description of the alien life form's physical characteristics.
   b) Explain how its features are adapted to the planet's conditions.
   c) Describe its sensory organs and how they function in the given environment.

2. Biochemistry and Metabolism (200-250 words):
   a) Propose a plausible biochemical basis for this life form.
   b) Explain its metabolic processes and energy sources.
   c) Discuss how it deals with the planet's atmospheric composition and temperature range.

3. Reproduction and Life Cycle (200-250 words):
   a) Describe the organism's reproductive strategy.
   b) Outline its life cycle, including any distinct phases or metamorphoses.
   c) Explain how its reproduction is adapted to the planetary conditions.

4. Ecological Role and Interactions (200-250 words):
   a) Describe the organism's role in its hypothetical ecosystem.
   b) Propose other life forms it might interact with and how.
   c) Explain how it copes with the planet's gravity and radiation levels.

5. Evolutionary History (150-200 words):
   a) Propose a plausible evolutionary path for this organism.
   b) Explain how key planetary factors might have driven its evolution.

6. Scientific Implications (150-200 words):
   a) Discuss what the existence of such a life form would imply about the nature of life in the universe.
   b) Propose an experiment to detect this type of life on the exoplanet.

7. Visual Representation:
   Provide a detailed textual description of what this alien life form would look like, as if you were describing a drawing or image. Include specifics about its shape, size, color, and any unique features.

Ensure your response demonstrates a deep understanding of biology, chemistry, and physics. Use appropriate scientific terminology and provide clear explanations for your design choices. Be creative in your approach while maintaining scientific plausibility given the planetary conditions.

Your total response should be between 1150-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response must demonstrate a clear understanding of how the given planetary conditions would affect the evolution and characteristics of life.",
            "The proposed alien life form should be creative yet scientifically plausible, with features and adaptations that logically correspond to the exoplanet's conditions.",
            "The response should include detailed explanations of the organism's biochemistry, metabolism, reproduction, and ecological role, all consistent with the planetary environment.",
            "The evolutionary history and scientific implications should be thoughtfully considered and logically presented.",
            "The visual representation description should provide a clear and vivid mental image of the alien life form."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
