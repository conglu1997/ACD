import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environments = [
            "Tidally locked planet with extreme temperature differences",
            "Low-gravity world with dense atmosphere and floating organisms",
            "Subterranean planet with bioluminescent ecosystem",
            "Water world with occasional bursts of solar radiation"
        ]
        species_traits = [
            "Hive mind collective consciousness",
            "Rapid evolutionary adaptation",
            "Silicon-based lifeforms with crystalline structures",
            "Temporal perception across multiple dimensions"
        ]
        challenges = [
            "Resource scarcity and distribution",
            "Interspecies communication and cooperation",
            "Ethical treatment of non-sentient life",
            "Balancing technological progress with environmental preservation"
        ]
        return {
            "1": {
                "environment": random.choice(environments),
                "species_trait": random.choice(species_traits),
                "challenge": random.choice(challenges)
            },
            "2": {
                "environment": random.choice(environments),
                "species_trait": random.choice(species_traits),
                "challenge": random.choice(challenges)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a governance system for an exoplanet with the following characteristics:\n\nEnvironment: {t['environment']}\nDominant Species Trait: {t['species_trait']}\nKey Challenge: {t['challenge']}\n\nYour task is to create a comprehensive governance proposal that addresses the unique aspects of this exoplanet and its inhabitants. Follow these steps:\n\n1. Environmental Analysis (150-200 words):\n   a) Describe how the planet's environment influences societal structures and governance needs.\n   b) Identify potential environmental challenges and opportunities for the governance system.\n\n2. Species Trait Integration (150-200 words):\n   a) Explain how the dominant species trait shapes social dynamics and decision-making processes.\n   b) Propose governance mechanisms that leverage or accommodate this trait.\n\n3. Governance Structure (200-250 words):\n   a) Outline the key components of your proposed governance system.\n   b) Describe how power is distributed and decisions are made.\n   c) Explain how this structure addresses the planet's unique characteristics.\n\n4. Ethical Framework (150-200 words):\n   a) Develop an ethical framework suitable for this exoplanet's context.\n   b) Discuss how this framework guides governance decisions and policies.\n\n5. Challenge Resolution (150-200 words):\n   a) Propose specific policies or mechanisms to address the key challenge.\n   b) Explain how these solutions fit within the broader governance structure.\n\n6. Adaptive Mechanisms (100-150 words):\n   a) Describe how your governance system can adapt to unforeseen changes or crises.\n   b) Propose a method for evaluating and improving the system over time.\n\n7. Earth Comparison (100-150 words):\n   a) Compare your proposed system to existing Earth governance models.\n   b) Discuss what insights from your exoplanet governance could be valuable for Earth.\n\nEnsure your response demonstrates a deep understanding of political science, environmental science, and ethics. Use appropriate terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining logical consistency and plausibility given the exoplanet's characteristics.\n\nFormat your response using clear headings for each section. Your total response should be between 1000-1350 words.\n"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of how {t['environment']} influences governance needs.",
            f"The governance system effectively integrates and addresses the implications of {t['species_trait']}.",
            f"The proposed solution for {t['challenge']} is creative, well-reasoned, and fits the exoplanet's context.",
            "The governance structure is comprehensive, logically consistent, and plausible given the exoplanet's characteristics.",
            "The response shows interdisciplinary knowledge application, combining concepts from political science, environmental science, and ethics.",
            "The ethical framework and adaptive mechanisms are well-developed and appropriate for the given scenario.",
            "The Earth comparison provides meaningful insights and demonstrates the ability to draw relevant parallels and contrasts."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
