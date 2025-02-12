import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ecosystems = [
            {
                "ecosystem": "Coral reef",
                "key_species": "Coral polyps",
                "environmental_factor": "Ocean acidification",
                "time_scale": "50 years"
            },
            {
                "ecosystem": "Boreal forest",
                "key_species": "Spruce trees",
                "environmental_factor": "Increasing wildfires",
                "time_scale": "100 years"
            }
        ]
        return {
            "1": ecosystems[0],
            "2": ecosystems[1]
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system to model and predict complex ecosystem dynamics for a {t['ecosystem']} ecosystem, focusing on {t['key_species']} as a key species and considering the impact of {t['environmental_factor']} over a {t['time_scale']} time scale. Your response should address the following points:

1. AI System Architecture (300-350 words):
   a) Describe the overall structure of your AI system for ecosystem modeling.
   b) Explain how it incorporates principles from environmental science and complex systems theory.
   c) Detail the key components, including data inputs, processing modules, and output formats.
   d) Discuss any novel machine learning techniques or algorithms used in your design.

2. Data Integration and Processing (250-300 words):
   a) Identify the types of data your system would use (e.g., species population data, climate data, etc.).
   b) Explain how your system would preprocess and integrate diverse data sources.
   c) Describe how you would handle missing or uncertain data in your model.
   d) Discuss any challenges in data representation specific to {t['ecosystem']} ecosystems and how your architecture addresses them.

3. Ecosystem Modeling Approach (250-300 words):
   a) Explain how your AI system models the complex interactions within the {t['ecosystem']} ecosystem.
   b) Describe how it accounts for the role of {t['key_species']} and their interactions with other species.
   c) Detail how your model incorporates the impact of {t['environmental_factor']} on the ecosystem.
   d) Discuss how your system handles non-linear dynamics and feedback loops common in ecosystems.

4. Predictive Capabilities (250-300 words):
   a) Describe how your system generates predictions over the {t['time_scale']} time scale.
   b) Explain how it accounts for uncertainty and variability in long-term predictions.
   c) Discuss how your model balances short-term fluctuations with long-term trends.
   d) Provide an example of a specific prediction your system might make about the {t['ecosystem']} ecosystem.

5. Validation and Improvement (200-250 words):
   a) Propose a method for validating the accuracy of your AI system's predictions.
   b) Describe how you would use real-world data to refine and improve your model over time.
   c) Discuss the challenges of validating long-term ecological predictions and how you would address them.

6. Ethical Considerations and Applications (200-250 words):
   a) Discuss the potential applications of your AI system in conservation and environmental management.
   b) Address any ethical concerns related to using AI for ecosystem modeling and decision-making.
   c) Explore how your system could be used to inform policy decisions related to {t['environmental_factor']}.
   d) Discuss the potential risks of over-reliance on AI models in ecological decision-making.

Ensure your response demonstrates a deep understanding of environmental science, complex systems theory, and artificial intelligence. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary.

Your total response should be between 1450-1750 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The AI system architecture is well-described and incorporates principles from environmental science and complex systems theory.",
            "The approach to data integration and processing is comprehensive and addresses challenges specific to the given ecosystem.",
            f"The ecosystem modeling approach effectively addresses the role of {t['key_species']} and the impact of {t['environmental_factor']}.",
            f"The predictive capabilities are well-explained and account for the {t['time_scale']} time scale.",
            "The validation and improvement methods are sound and address the challenges of long-term ecological predictions.",
            "Ethical considerations and potential applications are thoroughly discussed.",
            "The response demonstrates a deep understanding of environmental science, complex systems theory, and artificial intelligence.",
            "The proposed solutions are innovative while maintaining scientific plausibility.",
            "The response follows the specified format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
