import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environments = [
            {
                "name": "High-gravity rocky planet",
                "gravity": "3x Earth's gravity",
                "atmosphere": "Dense, high-pressure atmosphere rich in chlorine",
                "temperature": "Average surface temperature of 50°C"
            },
            {
                "name": "Subsurface ocean of an icy moon",
                "gravity": "0.1x Earth's gravity",
                "atmosphere": "None (subsurface ocean)",
                "temperature": "Water temperature near freezing point"
            },
            {
                "name": "Gas giant upper atmosphere",
                "gravity": "1.5x Earth's gravity",
                "atmosphere": "Primarily hydrogen and helium, with layers of ammonia clouds",
                "temperature": "Extreme temperature variations from -150°C to 100°C"
            },
            {
                "name": "Tidally-locked planet, twilight zone",
                "gravity": "0.8x Earth's gravity",
                "atmosphere": "Thin atmosphere with high carbon dioxide content",
                "temperature": "Constant temperature around 10°C, with extreme wind patterns"
            }
        ]
        return {str(i+1): env for i, env in enumerate(random.sample(environments, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a fictional alien organism adapted to survive in the following environment: {t['name']}

Environmental conditions:
- Gravity: {t['gravity']}
- Atmosphere: {t['atmosphere']}
- Temperature: {t['temperature']}

Your task is to:

1. Organism Design (100-150 words):
   Describe your alien organism, including its physical characteristics, sensory organs, locomotion method, and any unique adaptations. Ensure these features are logically consistent with the given environment.

2. Scientific Explanation (100-150 words):
   Explain how your organism's adaptations allow it to survive in this environment. Reference real biological, physical, and chemical principles to support your design choices.

3. Ecological Role (50-75 words):
   Briefly describe the organism's ecological niche and its interactions with its environment or potential other lifeforms.

4. Potential Evolutionary Pathway (50-75 words):
   Speculate on a possible evolutionary history that could have led to this organism, considering the environmental pressures.

5. Earth Analogue (2-3 sentences):
   Identify an Earth organism with similar adaptations or survival strategies, explaining the parallels.

Ensure your response is creative yet grounded in scientific principles. Demonstrate a clear understanding of how environmental factors influence biological adaptations."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a detailed description of an alien organism with adaptations consistent with the given environment",
            "The scientific explanation uses real biological, physical, and chemical principles to justify the organism's adaptations",
            "The ecological role and evolutionary pathway are logically consistent with the organism's design and environment",
            "An appropriate Earth analogue is identified with clear parallels explained",
            "The overall response demonstrates creativity while maintaining scientific plausibility"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
