import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'ecosystem': 'Coral Reefs',
                'climate_factor': 'Ocean Acidification',
                'biodiversity_metric': 'Species Richness',
                'human_activity': 'Overfishing'
            },
            {
                'ecosystem': 'Amazon Rainforest',
                'climate_factor': 'Increasing Temperature',
                'biodiversity_metric': 'Functional Diversity',
                'human_activity': 'Deforestation'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a predictive model for global ecosystem dynamics, focusing on the {t['ecosystem']} ecosystem. Your model should incorporate the climate change factor of {t['climate_factor']}, the biodiversity metric of {t['biodiversity_metric']}, and the human activity of {t['human_activity']}. Provide your response in the following format:

1. Model Architecture (300-350 words):
   a) Describe the overall structure of your predictive model.
   b) Explain how it integrates the given climate factor, biodiversity metric, and human activity.
   c) Detail the key components and their roles in the prediction process.
   d) Include at least one equation or formal representation of a critical component in your model.

2. Data Integration (250-300 words):
   a) Identify the types of data your model would require.
   b) Explain how you would collect, process, and integrate these diverse data sources.
   c) Discuss any challenges in data acquisition or integration and propose solutions.

3. Predictive Capabilities (250-300 words):
   a) Describe the specific predictions your model can make about the {t['ecosystem']} ecosystem.
   b) Explain how your model accounts for feedback loops and non-linear interactions.
   c) Discuss the time scales over which your model can make reliable predictions.

4. Uncertainty and Sensitivity Analysis (200-250 words):
   a) Explain how your model quantifies and communicates uncertainty in its predictions.
   b) Describe methods for sensitivity analysis to identify key factors influencing ecosystem dynamics.
   c) Discuss how your model handles scenarios with limited or unreliable data.

5. Model Validation and Improvement (200-250 words):
   a) Propose methods to validate your model's predictions against real-world data.
   b) Describe how you would iteratively improve your model based on new data or scientific discoveries.
   c) Discuss the ethical considerations in using and communicating results from your model.

6. Implications and Applications (200-250 words):
   a) Discuss the potential implications of your model for environmental policy and conservation efforts.
   b) Explore possible applications in climate change mitigation strategies and biodiversity preservation.
   c) Describe how your model could be adapted to study other ecosystems or global environmental challenges.

7. Limitations and Future Directions (150-200 words):
   a) Identify potential limitations of your proposed model.
   b) Suggest improvements or extensions to address these limitations.
   c) Propose two novel research questions that could be explored using your model.

Ensure your response demonstrates a deep understanding of environmental science, complex systems theory, and predictive modeling. Use technical terminology appropriately and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility. Your total response should be between 1550-1900 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of environmental science, complex systems theory, and predictive modeling.",
            "The proposed model effectively integrates the given climate factor, biodiversity metric, and human activity.",
            "The response includes detailed explanations of data integration, predictive capabilities, and uncertainty analysis.",
            "The model validation, improvement strategies, and ethical considerations are thoroughly discussed.",
            "The response explores the implications and applications of the model in a thoughtful and scientifically plausible manner.",
            "The limitations and future directions are clearly identified and addressed.",
            "The overall response is well-structured, coherent, and demonstrates creative problem-solving within the constraints of scientific plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
