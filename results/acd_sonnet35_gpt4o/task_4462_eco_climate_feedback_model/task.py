import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'ecosystem': 'Tropical rainforest',
                'climate_factor': 'Precipitation patterns',
                'biodiversity_aspect': 'Plant species richness'
            },
            {
                'ecosystem': 'Arctic tundra',
                'climate_factor': 'Permafrost thawing',
                'biodiversity_aspect': 'Soil microbiome diversity'
            },
            {
                'ecosystem': 'Coral reef',
                'climate_factor': 'Ocean acidification',
                'biodiversity_aspect': 'Fish species abundance'
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a complex systems model to simulate and predict ecological-climatic feedback loops, focusing on the interactions between biodiversity, carbon cycles, and climate change. Your model should specifically address the {t['ecosystem']} ecosystem, with emphasis on {t['climate_factor']} as the primary climate factor and {t['biodiversity_aspect']} as the key biodiversity aspect.

Your response should include the following sections:

1. Conceptual Framework (300-350 words):
   a) Describe the key components and interactions in your eco-climate feedback model.
   b) Explain how you integrate biodiversity, carbon cycles, and climate change in your model.
   c) Discuss the specific roles of {t['climate_factor']} and {t['biodiversity_aspect']} in your model.
   d) Provide a diagram or flowchart illustrating the main feedback loops in your model (describe it textually).

2. Mathematical Formulation (250-300 words):
   a) Present the core equations of your model, explaining each variable and parameter.
   b) Describe how you quantify and relate {t['climate_factor']} and {t['biodiversity_aspect']}.
   c) Explain how your model accounts for non-linear interactions and potential tipping points.

3. Data Requirements and Analysis (200-250 words):
   a) Specify the types of data needed to parameterize and validate your model.
   b) Describe the statistical or machine learning techniques you would use to analyze the data.
   c) Discuss how you would handle uncertainties and variability in the data.

4. Simulation and Prediction (250-300 words):
   a) Outline the simulation process for your model, including time scales and spatial resolution.
   b) Describe how you would validate the model using historical data.
   c) Present a hypothetical scenario of how {t['climate_factor']} might change over the next 50 years and predict its impact on {t['biodiversity_aspect']}.
   d) Discuss the limitations and uncertainties in your predictions.

5. Model Applications and Implications (200-250 words):
   a) Propose two specific applications of your model in environmental management or policy-making.
   b) Discuss how your model could contribute to our understanding of ecosystem resilience and tipping points.
   c) Analyze the potential implications of your model's predictions for conservation strategies in the {t['ecosystem']}.

6. Interdisciplinary Integration and Future Directions (150-200 words):
   a) Explain how your model integrates concepts from ecology, climatology, and complex systems science.
   b) Discuss how your approach could be extended to include social or economic factors.
   c) Propose a future research direction that could enhance the predictive power of eco-climate feedback models.

Ensure your response demonstrates a deep understanding of ecological processes, climate science, and complex systems modeling. Use appropriate scientific terminology and provide clear explanations for technical concepts. Be innovative in your approach while maintaining scientific rigor and plausibility.

Format your response with clear headings for each section and subsections labeled a, b, c, d as appropriate. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of ecological processes, climate science, and complex systems modeling.",
            "The conceptual framework is well-developed and clearly integrates biodiversity, carbon cycles, and climate change.",
            "The mathematical formulation is sound and appropriately represents the key components and interactions of the model.",
            "The data requirements and analysis methods are well-specified and appropriate for the model.",
            "The simulation and prediction section provides a clear and plausible scenario based on the model.",
            "The model applications and implications are thoughtfully discussed and relevant to the given ecosystem.",
            "The response shows strong interdisciplinary integration and proposes innovative future directions.",
            "The writing is clear, well-organized, and uses appropriate scientific terminology.",
            "The response adheres to the specified format and word count requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
