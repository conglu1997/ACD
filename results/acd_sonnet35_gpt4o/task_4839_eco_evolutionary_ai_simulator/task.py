import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ecosystems = [
            {
                "type": "coral reef",
                "climate_threat": "ocean acidification",
                "key_species": "coral polyps",
                "evolutionary_mechanism": "symbiotic adaptation"
            },
            {
                "type": "boreal forest",
                "climate_threat": "increasing wildfires",
                "key_species": "coniferous trees",
                "evolutionary_mechanism": "phenotypic plasticity"
            },
            {
                "type": "arctic tundra",
                "climate_threat": "permafrost thaw",
                "key_species": "caribou",
                "evolutionary_mechanism": "genetic drift"
            }
        ]
        return {
            "1": random.choice(ecosystems),
            "2": random.choice(ecosystems)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates and optimizes ecosystem adaptation to climate change for a {t['type']} ecosystem facing the threat of {t['climate_threat']}. Your system should focus on the key species {t['key_species']} and incorporate the evolutionary mechanism of {t['evolutionary_mechanism']}. Your response should include the following sections:

1. AI System Architecture (300-350 words):
   a) Describe the key components of your AI system for ecosystem simulation and optimization.
   b) Explain how your system integrates principles from evolutionary biology, artificial intelligence, and environmental science.
   c) Detail how your system models the {t['type']} ecosystem and the impact of {t['climate_threat']}.
   d) Discuss how your system incorporates {t['evolutionary_mechanism']} in its simulations.
   e) Include a brief diagram or flowchart description of your AI system architecture.

2. Ecosystem Modeling Approach (250-300 words):
   a) Explain your approach to modeling the {t['type']} ecosystem, including key environmental variables and species interactions.
   b) Describe how your model simulates the effects of {t['climate_threat']} on the ecosystem.
   c) Detail how you incorporate {t['evolutionary_mechanism']} into your model, particularly for {t['key_species']}.
   d) Discuss any novel algorithms or techniques used in your ecosystem modeling approach.

3. Adaptation Optimization Strategy (250-300 words):
   a) Describe your AI system's strategy for optimizing ecosystem adaptation to {t['climate_threat']}.
   b) Explain how your system evaluates and selects potential adaptation strategies.
   c) Discuss how you balance short-term survival with long-term evolutionary potential in your optimization approach.
   d) Provide an example scenario of how your system might optimize adaptation for {t['key_species']}.

4. Data Integration and Analysis (200-250 words):
   a) Explain how your system integrates and analyzes data from various sources (e.g., climate models, species databases, genetic information).
   b) Describe any machine learning techniques used for pattern recognition or prediction in your system.
   c) Discuss how your system handles uncertainty and variability in ecological and climate data.

5. Validation and Testing (200-250 words):
   a) Propose methods to validate your AI system's predictions and optimization strategies.
   b) Describe how you would test your system against real-world data or alternative models.
   c) Discuss the limitations of your approach and potential sources of error or bias.

6. Ethical Considerations and Implications (150-200 words):
   a) Discuss the ethical implications of using AI to simulate and optimize ecosystem adaptation.
   b) Address concerns about potential misuse or unintended consequences of your system.
   c) Propose guidelines for the responsible development and use of such AI systems in ecological management.

7. Future Directions and Applications (100-150 words):
   a) Suggest potential expansions or modifications to your system for future research.
   b) Discuss how your approach could be applied to other ecosystems or climate change scenarios.
   c) Propose a novel research question that could be explored using your AI system.

Ensure your response demonstrates a deep understanding of evolutionary biology, artificial intelligence, and environmental science. Use appropriate terminology and provide clear explanations for complex concepts. Be creative and innovative while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1450-1800 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a comprehensive AI system architecture that integrates evolutionary biology, artificial intelligence, and environmental science for simulating and optimizing adaptation in a {t['type']} ecosystem facing {t['climate_threat']}.",
            f"The ecosystem modeling approach effectively incorporates {t['evolutionary_mechanism']} and focuses on {t['key_species']}.",
            "The adaptation optimization strategy is well-explained and demonstrates a balance between short-term survival and long-term evolutionary potential.",
            "The data integration and analysis section describes appropriate machine learning techniques and addresses uncertainty in ecological and climate data.",
            "The validation and testing methods are clearly described and address potential limitations and biases.",
            "Ethical considerations are thoroughly discussed, and guidelines for responsible use are proposed.",
            "Future directions and applications are suggested creatively and relevantly.",
            "The overall response demonstrates interdisciplinary knowledge synthesis, complex systems modeling, and analytical reasoning about the interplay between ecology, evolution, and artificial intelligence."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
