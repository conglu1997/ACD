import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                'scenario': 'Arctic sea ice melt',
                'economic_sector': 'Global shipping',
                'time_horizon': '50 years'
            },
            {
                'scenario': 'Amazon rainforest dieback',
                'economic_sector': 'Agriculture',
                'time_horizon': '30 years'
            },
            {
                'scenario': 'Coral reef collapse',
                'economic_sector': 'Tourism',
                'time_horizon': '25 years'
            },
            {
                'scenario': 'Permafrost thaw',
                'economic_sector': 'Energy production',
                'time_horizon': '40 years'
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a predictive model that simulates the complex interactions between climate change and global economic systems, focusing on the scenario of {t['scenario']} and its impact on the {t['economic_sector']} sector over a {t['time_horizon']} time horizon. Your model should incorporate feedback loops and potential tipping points. Your response should include:

1. Model Architecture (300-350 words):
   a) Describe the key components of your climate-economic model and how they interact.
   b) Explain how your model incorporates feedback loops between climate and economic systems.
   c) Detail the data inputs required for your model and how they would be obtained or estimated.
   d) Discuss how your model accounts for uncertainty and variability in both climate and economic projections.
   e) Provide a diagram or flowchart representing your model's architecture.

2. Climate-Economic Interactions (250-300 words):
   a) Identify and explain at least three key feedback loops between {t['scenario']} and the {t['economic_sector']} sector.
   b) Describe how your model simulates these interactions over the {t['time_horizon']} period.
   c) Discuss any potential tipping points or non-linear effects in your model.

3. Predictive Capabilities (200-250 words):
   a) Explain the specific outputs or predictions your model can generate.
   b) Describe how your model handles different timescales (short-term, medium-term, long-term) in its predictions.
   c) Discuss the reliability and limitations of your model's predictions.
   d) Provide at least one quantitative estimate or prediction from your model, with justification.

4. Scenario Analysis (250-300 words):
   a) Present a baseline scenario for the {t['scenario']} and its impact on the {t['economic_sector']} sector over {t['time_horizon']}.
   b) Describe two alternative scenarios with different assumptions or interventions.
   c) Compare and contrast the outcomes of these scenarios, highlighting key differences and potential policy implications.
   d) Include quantitative estimates for key variables in each scenario.

5. Novel Climate-Economic Metric (150-200 words):
   a) Propose a new metric or index that combines climate and economic factors relevant to your model.
   b) Explain the components of this metric and how it is calculated.
   c) Discuss how this metric provides unique insights into the climate-economic interactions in your model.

6. Model Validation and Calibration (200-250 words):
   a) Propose a method for validating your model using historical data or other models.
   b) Describe how you would calibrate your model to improve its accuracy over time.
   c) Discuss any challenges in validating complex climate-economic models and how you would address them.

7. Ethical Considerations and Limitations (150-200 words):
   a) Discuss potential ethical implications of using your model for policy decisions.
   b) Address any limitations or potential biases in your model.
   c) Suggest ways to ensure responsible use of your model's predictions.

8. Interdisciplinary Insights and Contrasting Viewpoints (200-250 words):
   a) Explain how your model integrates insights from climate science, economics, and other relevant disciplines.
   b) Discuss any novel interdisciplinary insights that emerge from your modeling approach.
   c) Present and address at least one contrasting viewpoint or alternative interpretation of the data related to your model's predictions.
   d) Suggest areas where further interdisciplinary research could enhance the model's capabilities.

Ensure your response demonstrates a deep understanding of climate science, economics, and complex systems modeling. Use appropriate technical terminology and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility and real-world applicability.

Cite relevant literature or data sources to support your model design and predictions. Use in-text citations in the format (Author, Year) and provide a brief bibliography at the end of your response.

Format your response with clear headings for each section. Your total response should be between 1700-2100 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The model effectively integrates climate science and economics, focusing on {t['scenario']} and its impact on the {t['economic_sector']} sector.",
            "The response demonstrates a deep understanding of complex systems modeling, feedback loops, and tipping points.",
            "The model's predictive capabilities and scenario analyses are well-explained and include plausible quantitative estimates.",
            "The proposed novel climate-economic metric is innovative and well-justified.",
            "The response addresses ethical considerations and limitations of the model appropriately.",
            "The submission shows creativity and interdisciplinary thinking while maintaining scientific plausibility.",
            "The response includes relevant citations and addresses contrasting viewpoints or alternative data interpretations."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
