import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ecosystems = [
            {
                "type": "Coral Reef",
                "stressor": "Ocean Acidification",
                "key_species": "Acropora palmata (Elkhorn Coral)"
            },
            {
                "type": "Boreal Forest",
                "stressor": "Increasing Wildfires",
                "key_species": "Picea mariana (Black Spruce)"
            },
            {
                "type": "Arctic Tundra",
                "stressor": "Permafrost Thaw",
                "key_species": "Eriophorum vaginatum (Tussock Cottongrass)"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(ecosystems, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a predictive model for ecosystem resilience in the face of climate change, focusing on a {t['type']} ecosystem affected by {t['stressor']}. Your model should incorporate complex systems theory and environmental science principles, with particular attention to the role of {t['key_species']}. Provide your response in the following format:

1. Model Framework (300-350 words):
   a) Describe the key components and interactions in your ecosystem resilience model.
   b) Explain how your model incorporates complex systems theory principles.
   c) Detail how your model accounts for the specific climate change stressor and its effects on the ecosystem.
   d) Discuss how the key species is integrated into your model and its significance for ecosystem resilience.

2. Data Requirements and Parameters (200-250 words):
   a) Specify the types of data your model would require for accurate predictions.
   b) List and explain the key parameters in your model, including both biotic and abiotic factors.
   c) Describe how you would obtain or estimate these parameters, addressing any challenges in data collection.

3. Resilience Metrics and Thresholds (200-250 words):
   a) Define specific metrics for measuring ecosystem resilience in your model.
   b) Explain how these metrics relate to the ecosystem's structure and function.
   c) Propose thresholds or tipping points that would indicate a significant loss of resilience.

4. Predictive Capabilities (250-300 words):
   a) Describe the temporal and spatial scales over which your model can make predictions.
   b) Explain how your model accounts for feedback loops and non-linear dynamics in the ecosystem.
   c) Discuss how your model handles uncertainty and variability in climate change projections.
   d) Provide an example scenario of how your model might predict ecosystem changes over time.

5. Model Validation and Refinement (200-250 words):
   a) Propose a method for validating your model's predictions against real-world data.
   b) Describe how you would refine and update your model based on new data or observed ecosystem changes.
   c) Discuss the limitations of your model and potential areas for improvement.

6. Applications and Implications (150-200 words):
   a) Suggest practical applications of your model for ecosystem management and conservation.
   b) Discuss the potential implications of your model's predictions for policy-making and climate change adaptation strategies.
   c) Explore how your modeling approach could be extended to other ecosystems or global-scale predictions.

Ensure your response demonstrates a deep understanding of complex systems theory, environmental science, and climate change impacts. Use appropriate scientific terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and ecological realism.

Format your response with clear headings for each section. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must demonstrate a clear understanding of {t['type']} ecosystems and the effects of {t['stressor']}.",
            "The model framework should be innovative, logically consistent, and well-explained, incorporating complex systems theory principles.",
            f"The role of {t['key_species']} should be effectively integrated into the model and its significance for ecosystem resilience clearly explained.",
            "The data requirements, parameters, and resilience metrics should be appropriate and well-justified for the specific ecosystem and stressor.",
            "The model's predictive capabilities, including handling of feedback loops and non-linear dynamics, should be clearly described and ecologically plausible.",
            "The proposed validation method and model refinement process should be scientifically sound and practical.",
            "The response must thoughtfully address the applications and implications of the model for ecosystem management and policy-making."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
