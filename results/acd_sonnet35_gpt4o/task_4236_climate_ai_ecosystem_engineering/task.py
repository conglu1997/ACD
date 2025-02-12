import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biomes = [
            "Tropical Rainforest",
            "Coral Reef",
            "Arctic Tundra",
            "Temperate Grassland",
            "Mangrove Swamp"
        ]
        climate_effects = [
            "Rising temperatures",
            "Ocean acidification",
            "Extreme weather events",
            "Sea level rise",
            "Desertification"
        ]
        ai_approaches = [
            "Reinforcement learning",
            "Evolutionary algorithms",
            "Multi-agent systems",
            "Neural-symbolic AI",
            "Quantum-inspired algorithms"
        ]
        
        tasks = [
            {
                "biome": random.choice(biomes),
                "climate_effect": random.choice(climate_effects),
                "ai_approach": random.choice(ai_approaches)
            } for _ in range(2)
        ]
        
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI-driven ecosystem engineering system to mitigate the effects of {t['climate_effect']} on the {t['biome']} biome, using {t['ai_approach']} as your primary AI approach. Your response should include the following sections:

1. Ecosystem Analysis (250-300 words):
   a) Describe the key characteristics and vulnerabilities of the {t['biome']} biome.
   b) Explain how {t['climate_effect']} impacts this specific ecosystem.
   c) Identify the critical ecological processes and species interactions that need to be maintained or restored.

2. AI System Architecture (300-350 words):
   a) Outline the key components of your AI-driven ecosystem engineering system.
   b) Explain how you integrate {t['ai_approach']} into your system design.
   c) Describe how your system models and predicts ecosystem dynamics.
   d) Discuss how your AI system interfaces with the physical environment (e.g., through sensors, robotic interventions, etc.).

3. Mitigation Strategies (250-300 words):
   a) Propose at least three specific strategies your system would implement to mitigate {t['climate_effect']} in the {t['biome']}.
   b) Explain the ecological reasoning behind each strategy.
   c) Describe how your AI system would adapt these strategies over time based on ecosystem responses.

4. Complex Systems Integration (200-250 words):
   a) Discuss how your system accounts for the complex, non-linear interactions within the ecosystem.
   b) Explain how you handle uncertainty and incomplete information in your model.
   c) Describe how your system balances short-term interventions with long-term ecosystem stability.

5. Ethical and Ecological Considerations (200-250 words):
   a) Identify potential unintended consequences of your ecosystem engineering approach.
   b) Discuss the ethical implications of using AI to manage natural ecosystems.
   c) Propose guidelines for responsible development and deployment of AI in ecological contexts.

6. Evaluation and Monitoring (150-200 words):
   a) Describe how you would measure the success of your system in mitigating {t['climate_effect']}.
   b) Propose a method for long-term monitoring of ecosystem health and biodiversity.
   c) Discuss how you would validate your AI model's predictions against real-world outcomes.

7. Scalability and Global Impact (150-200 words):
   a) Explain how your approach could be scaled or adapted to other biomes facing similar climate challenges.
   b) Discuss the potential global impact of your system if widely implemented.
   c) Identify key barriers to large-scale deployment and propose solutions.

Ensure your response demonstrates a deep understanding of ecology, climate science, complex systems theory, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and ecological sensitivity.

Format your response with clear headings for each section. Your total response should be between 1500-1850 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should address the specific biome of {t['biome']}, climate effect of {t['climate_effect']}, and AI approach of {t['ai_approach']}",
            "The design should clearly integrate principles from ecology, climate science, complex systems theory, and artificial intelligence",
            "The response should include all required sections: Ecosystem Analysis, AI System Architecture, Mitigation Strategies, Complex Systems Integration, Ethical and Ecological Considerations, Evaluation and Monitoring, and Scalability and Global Impact",
            "The proposed system should be innovative while maintaining scientific plausibility and ecological sensitivity",
            "The response should demonstrate a deep understanding of the chosen biome's ecology and the impacts of the specified climate effect",
            "The discussion should address potential unintended consequences and ethical implications of AI-driven ecosystem engineering"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
