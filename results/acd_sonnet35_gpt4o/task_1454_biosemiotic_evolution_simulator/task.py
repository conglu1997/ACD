import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "ecosystem": "Coral Reef",
                "communication_type": "Chemical signaling",
                "evolutionary_pressure": "Increasing ocean acidification"
            },
            {
                "ecosystem": "Temperate Forest",
                "communication_type": "Acoustic signaling",
                "evolutionary_pressure": "Noise pollution from human activities"
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(scenarios)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical framework and simulation model for analyzing the evolution of biological communication systems in a {t['ecosystem']} ecosystem, focusing on {t['communication_type']} under the evolutionary pressure of {t['evolutionary_pressure']}. Your response should include:

1. Theoretical Framework (300-350 words):
   a) Describe the key components of your biosemiotic framework for analyzing biological communication systems.
   b) Explain how you integrate principles from information theory and evolutionary biology into your framework.
   c) Discuss how your framework accounts for the specific characteristics of {t['communication_type']} in a {t['ecosystem']} ecosystem.
   d) Explain how your framework incorporates the evolutionary pressure of {t['evolutionary_pressure']}.

2. Simulation Model Design (250-300 words):
   a) Outline the structure of your simulation model, including key variables and parameters.
   b) Explain how your model simulates the evolution of communication systems over time.
   c) Describe how you incorporate stochastic processes and feedback loops in your model.
   d) Discuss how your model handles the interaction between multiple species or populations.

3. Mathematical Formulation (200-250 words):
   a) Provide the key equations or algorithms that form the core of your simulation model.
   b) Explain the biological and information-theoretical significance of each component in your equations.
   c) Describe how your mathematical formulation captures the evolutionary dynamics of the communication system.

4. Data Requirements and Analysis (150-200 words):
   a) Specify the types of data your model would require for initialization and validation.
   b) Describe the key metrics you would use to analyze the simulation results.
   c) Explain how you would validate your model against real-world observations.

5. Predicted Outcomes and Hypotheses (200-250 words):
   a) Based on your framework and model, propose at least three hypotheses about how {t['communication_type']} might evolve under the pressure of {t['evolutionary_pressure']}.
   b) Describe potential emergent properties or unexpected outcomes that your simulation might reveal.
   c) Discuss how your predictions align with or challenge current understanding in biosemiotics and evolutionary biology.

6. Limitations and Future Directions (150-200 words):
   a) Discuss the limitations of your theoretical framework and simulation model.
   b) Propose at least two ways to extend or refine your approach in future research.
   c) Suggest how your framework could be applied to other types of biological communication systems or evolutionary pressures.

Ensure your response demonstrates a deep understanding of biosemiotics, information theory, and evolutionary biology. Be creative in your approach while maintaining scientific rigor and plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of biosemiotics, information theory, and evolutionary biology",
            "The theoretical framework effectively integrates principles from multiple disciplines",
            "The simulation model is well-designed and incorporates key biological and information-theoretical concepts",
            "The mathematical formulation is sound and accurately represents the evolutionary dynamics",
            "The predicted outcomes and hypotheses are logical and well-reasoned",
            f"The framework and model adequately address the specific scenario of {t['communication_type']} in a {t['ecosystem']} ecosystem under the pressure of {t['evolutionary_pressure']}"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
