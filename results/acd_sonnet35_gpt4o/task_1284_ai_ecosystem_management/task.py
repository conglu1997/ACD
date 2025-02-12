import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biomes = [
            "tropical rainforest",
            "coral reef",
            "arctic tundra",
            "temperate grassland"
        ]
        challenges = [
            "climate change adaptation",
            "invasive species management",
            "pollution mitigation",
            "resource conservation"
        ]
        return {
            "1": {
                "biome": random.choice(biomes),
                "challenge": random.choice(challenges)
            },
            "2": {
                "biome": random.choice(biomes),
                "challenge": random.choice(challenges)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI-driven ecosystem management system for a {t['biome']}, focusing on the challenge of {t['challenge']}. Your system should incorporate principles of complex systems theory and machine learning to optimize biodiversity and ecosystem resilience. Your response should include the following sections:

1. Ecosystem Analysis (200-250 words):
   a) Describe the key characteristics and components of the {t['biome']} ecosystem.
   b) Explain the specific challenges posed by {t['challenge']} in this biome.
   c) Identify the critical variables and interactions that your AI system needs to monitor and manage.

2. AI System Architecture (250-300 words):
   a) Design the overall architecture of your AI ecosystem management system.
   b) Explain how your system incorporates principles of complex systems theory.
   c) Describe the machine learning algorithms or approaches you would use and why.
   d) Discuss how your system would handle uncertainty and adapt to changing conditions.

3. Data Collection and Processing (200-250 words):
   a) Outline the types of data your system would collect and how.
   b) Describe how you would ensure data quality and handle missing or noisy data.
   c) Explain how your system would integrate and analyze data from multiple sources.

4. Intervention Strategies (200-250 words):
   a) Describe how your AI system would determine when and how to intervene in the ecosystem.
   b) Provide examples of specific interventions your system might recommend for {t['challenge']}.
   c) Explain how your system would evaluate the effectiveness of its interventions and adjust its strategies.

5. Ethical Considerations and Safeguards (150-200 words):
   a) Discuss the potential ethical implications of using AI to manage natural ecosystems.
   b) Propose safeguards to prevent unintended consequences or misuse of the system.
   c) Explain how you would ensure transparency and accountability in the system's decision-making process.

6. Long-term Impact Assessment (150-200 words):
   a) Describe how you would measure the long-term success of your AI ecosystem management system.
   b) Discuss potential challenges or limitations in predicting long-term ecological outcomes.
   c) Propose a method for continuous improvement and adaptation of the system over time.

Ensure your response demonstrates a deep understanding of ecology, complex systems theory, and artificial intelligence. Use appropriate technical terminology and provide clear explanations where necessary. Be innovative in your approach while maintaining scientific plausibility and ethical responsibility.

Format your response with clear headings for each section. Your total response should be between 1150-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of the {t['biome']} ecosystem and the challenges posed by {t['challenge']}",
            "The AI system architecture incorporates principles of complex systems theory and appropriate machine learning approaches",
            "The data collection and processing strategy is comprehensive and addresses potential issues",
            "The intervention strategies are specific, relevant, and adaptable",
            "Ethical considerations are thoughtfully addressed with proposed safeguards",
            "The long-term impact assessment plan is well-reasoned and includes a method for system improvement",
            "The response shows interdisciplinary knowledge integration and innovative thinking",
            "The proposed system is scientifically plausible and ethically responsible"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
