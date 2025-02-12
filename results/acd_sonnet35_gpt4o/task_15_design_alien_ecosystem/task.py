import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environments = [
            {"gravity": "low", "atmosphere": "thin", "temperature": "extreme fluctuations", "water": "scarce"},
            {"gravity": "high", "atmosphere": "dense", "temperature": "consistently hot", "water": "abundant"}
        ]
        return {
            "1": {"environment": environments[0]},
            "2": {"environment": environments[1]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a plausible ecosystem for an alien planet with the following environmental conditions:

- Gravity: {t['environment']['gravity']}
- Atmosphere: {t['environment']['atmosphere']}
- Temperature: {t['environment']['temperature']}
- Water availability: {t['environment']['water']}

Your task is to create a coherent ecosystem that could potentially evolve and thrive in these conditions. Provide your response in the following format:

1. Overview: Briefly describe the general characteristics of your ecosystem (2-3 sentences).

2. Key Species: Describe three key species in your ecosystem (one producer, one consumer, and one decomposer). For each species, include:
   a) Name: A creative name for the species
   b) Description: Physical characteristics and adaptations (2-3 sentences)
   c) Role: Its role in the ecosystem and interactions with other species (1-2 sentences)

3. Ecosystem Dynamics: Explain how energy flows through your ecosystem and how the species interact to form a stable system (3-4 sentences).

4. Environmental Adaptation: Describe how the ecosystem and its species are specifically adapted to the given environmental conditions (2-3 sentences).

Ensure that your ecosystem is scientifically plausible given the environmental conditions, while also being creative and unique. Consider how the specific environmental factors would shape the evolution and interactions of species in your ecosystem."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The ecosystem design is scientifically plausible given the environmental conditions.",
            "The response includes all required components: overview, key species (producer, consumer, decomposer), ecosystem dynamics, and environmental adaptation.",
            "The ecosystem demonstrates internal consistency and logical interactions between species.",
            "The design shows creativity and uniqueness while maintaining scientific plausibility.",
            "The response adequately explains how the ecosystem is adapted to the specific environmental conditions provided."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
