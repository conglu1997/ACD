import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "regions": ["Arctic", "Coastal Megacities"],
                "timescale": "100 years",
                "focus": "Sea ice dynamics and sea level rise",
                "data": {
                    "Arctic": {
                        "current_sea_ice_extent": "4.5 million km²",
                        "average_temperature": "-18°C",
                        "CO2_levels": "420 ppm"
                    },
                    "Coastal Megacities": {
                        "current_sea_level": "0 cm (baseline)",
                        "average_temperature": "22°C",
                        "population_density": "5,000 people/km²"
                    },
                    "conflicting_data": "Recent 5-year data shows a 2% increase in Arctic sea ice extent, contradicting the long-term decline trend."
                }
            },
            {
                "regions": ["Amazon Rainforest", "Sahel"],
                "timescale": "75 years",
                "focus": "Deforestation impact and desertification",
                "data": {
                    "Amazon Rainforest": {
                        "current_forest_cover": "5.5 million km²",
                        "average_temperature": "25°C",
                        "annual_deforestation_rate": "10,000 km²/year"
                    },
                    "Sahel": {
                        "current_arable_land": "100,000 km²",
                        "average_temperature": "28°C",
                        "annual_rainfall": "600 mm"
                    },
                    "conflicting_data": "Satellite imagery shows a 5% increase in vegetation cover in the Sahel over the last decade, despite climate models predicting desertification."
                }
            }
        ]
        return {
            "1": scenarios[0],
            "2": scenarios[1]
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a complex adaptive system model using AI techniques to predict climate change patterns and propose adaptive mitigation strategies for the regions of {', '.join(t['regions'])} over a {t['timescale']} timescale, focusing on {t['focus']}. Use the following initial data in your model: {t['data']}.

Your task also includes critiquing and improving upon an existing climate model with the following flaw: it assumes linear relationships between all variables and does not account for tipping points or feedback loops.

Your response should include the following sections:

1. Model Architecture (300-350 words):
   a) Describe the overall structure of your complex adaptive system model.
   b) Explain how you integrate climate science principles, complex systems theory, and AI techniques in your model.
   c) Detail the key components and their interactions within the system, including how you model the interaction between the given regions.
   d) Discuss how your model handles uncertainty, non-linear dynamics, and conflicting data.

2. Data Integration and Processing (250-300 words):
   a) Identify additional types of data your model would require and potential sources.
   b) Explain how your model processes and integrates diverse data types, including the conflicting data provided.
   c) Describe any novel data processing techniques you employ to handle the complexity and scale of multi-regional climate data.

3. AI and Machine Learning Implementation (250-300 words):
   a) Detail the specific AI and machine learning techniques used in your model.
   b) Explain how these techniques enhance the model's predictive capabilities and adaptive features.
   c) Discuss any innovations in your AI approach that address challenges specific to modeling multiple interacting regions.

4. Climate Change Prediction (250-300 words):
   a) Describe how your model predicts climate change patterns for the given regions and timescale.
   b) Explain how the model accounts for feedback loops and tipping points in the climate system.
   c) Provide a quantitative prediction for a key variable in each region at the end of the given timescale. For example, predict the sea ice extent for the Arctic and sea level rise for Coastal Megacities, showing your reasoning and calculations.
   d) Address how your model resolves the conflicting data provided.

5. Adaptive Mitigation Strategies (250-300 words):
   a) Explain how your model generates adaptive mitigation strategies based on its predictions.
   b) Describe at least two specific mitigation strategies your model might propose for each region.
   c) Discuss how these strategies adapt to changing conditions over time and interact across regions.
   d) Include a basic cost-benefit analysis for one of your proposed strategies, considering a limited budget scenario. For example, estimate the cost of implementing a strategy and its potential benefits in terms of damage prevented or resources saved.

6. Model Validation and Uncertainty Quantification (200-250 words):
   a) Propose methods to validate your model's predictions and assess its reliability.
   b) Describe how your model quantifies and communicates uncertainty in its predictions and recommendations.
   c) Discuss the limitations of your approach and potential areas for improvement.
   d) Explain how your model improves upon the flawed climate model mentioned in the task description, specifically addressing its handling of non-linear relationships, tipping points, and feedback loops.

7. Ethical Considerations and Societal Impact (200-250 words):
   a) Identify potential ethical issues related to the use of AI in climate change prediction and mitigation, particularly in the context of multiple regions with potentially competing interests.
   b) Discuss the societal implications of implementing AI-driven climate strategies across different regions.
   c) Propose guidelines for the responsible development and use of AI in multi-regional climate science.

Ensure your response demonstrates a deep understanding of climate science, complex systems theory, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Use subheadings a), b), c), d) for each point within the sections. Your total response should be between 1700-2100 words. Include a word count at the end of your response.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response addresses all seven sections as specified in the instructions.",
            "The model design demonstrates integration of climate science principles, complex systems theory, and AI techniques across multiple interacting regions.",
            "The response includes specific examples and quantitative predictions relevant to the given regions, timescale, and focus.",
            "The proposed adaptive mitigation strategies are logical, relevant to the scenarios, and consider interactions between regions.",
            "The response demonstrates a deep understanding of climate science, complex systems theory, and artificial intelligence.",
            "The response is innovative while maintaining scientific plausibility.",
            "The response uses appropriate technical terminology and provides clear explanations for complex concepts.",
            "The response includes at least one feedback loop and one tipping point relevant to the given scenarios.",
            "The response proposes at least two specific, feasible mitigation strategies for each region.",
            "The response discusses ethical considerations and societal impacts specific to the given scenarios and multiple regions.",
            "The response includes a basic cost-benefit analysis for one proposed strategy, with numerical estimates.",
            "The response addresses and resolves the conflicting data provided in the scenario.",
            "The response critiques and improves upon the flawed climate model as specified in the instructions, addressing non-linear relationships, tipping points, and feedback loops.",
            "The total response is between 1700-2100 words and includes a word count."
        ]
        score = sum(eval_with_llm_judge(instructions, submission, [criterion]) for criterion in criteria) / len(criteria)
        return score
