import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ecosystems = [
            {
                'name': 'Coral Reef',
                'key_species': ['coral polyps', 'zooxanthellae algae', 'parrotfish'],
                'environmental_factor': 'ocean acidification'
            },
            {
                'name': 'Boreal Forest',
                'key_species': ['spruce trees', 'bark beetles', 'woodpeckers'],
                'environmental_factor': 'increasing temperatures'
            }
        ]
        
        return {str(i+1): {'ecosystem': ecosystem} for i, ecosystem in enumerate(random.sample(ecosystems, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that models symbiotic relationships in the {t['ecosystem']['name']} ecosystem, focusing on the interactions between {', '.join(t['ecosystem']['key_species'])}. Your system should use principles from complex systems theory to predict ecological outcomes under the influence of {t['ecosystem']['environmental_factor']} and propose sustainable interventions. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the overall structure of your AI system, including its main components and their interactions.
   b) Explain how your system incorporates principles from complex systems theory.
   c) Detail how your system models symbiotic relationships and environmental factors.
   d) Include a high-level diagram or pseudocode of your system's architecture (described textually).

2. Symbiotic Relationship Modeling (200-250 words):
   a) Explain how your system models the symbiotic relationships between the key species.
   b) Describe the data inputs and parameters your model uses.
   c) Discuss how your model accounts for different types of symbiosis (e.g., mutualism, commensalism, parasitism).

3. Environmental Impact Simulation (200-250 words):
   a) Detail how your system simulates the impact of {t['ecosystem']['environmental_factor']} on the ecosystem.
   b) Explain any feedback loops or emergent behaviors your model might reveal.
   c) Describe how your system handles uncertainty and variability in environmental factors.

4. Predictive Capabilities (150-200 words):
   a) Explain how your system generates predictions about ecological outcomes.
   b) Discuss the time scales over which your model can make reliable predictions.
   c) Describe how your system validates its predictions against real-world data.

5. Sustainable Intervention Proposals (200-250 words):
   a) Explain how your system generates and evaluates potential interventions.
   b) Describe the criteria your system uses to assess the sustainability of interventions.
   c) Provide an example of a specific intervention your system might propose for the {t['ecosystem']['name']} ecosystem.

6. Ethical Considerations (100-150 words):
   a) Discuss potential ethical issues in using AI to guide ecological interventions.
   b) Propose guidelines for responsible development and use of such AI systems in ecology.

7. Limitations and Future Work (100-150 words):
   a) Identify potential limitations of your proposed system.
   b) Suggest areas for future research or improvements to your model.

Ensure your response demonstrates a deep understanding of ecology, complex systems theory, and artificial intelligence. Use technical terminology appropriately and provide explanations where necessary. Be creative and innovative in your approach while maintaining scientific plausibility.

Format your response using clear headings for each section. Your total response should be between 1200-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a thorough understanding of the specified ecosystem and its symbiotic relationships.",
            "The AI system design incorporates principles from complex systems theory in a meaningful way.",
            "The modeling of environmental impacts and predictive capabilities is scientifically sound and innovative.",
            "The proposed interventions are creative, sustainable, and well-reasoned.",
            "Ethical considerations and limitations are thoughtfully addressed.",
            "The overall response is well-structured, clear, and adheres to the specified word count and section guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
