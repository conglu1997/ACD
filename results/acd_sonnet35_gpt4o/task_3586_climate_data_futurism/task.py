import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        climate_variables = [
            "temperature",
            "precipitation",
            "sea level",
            "atmospheric CO2",
            "ocean acidification"
        ]
        time_periods = [
            "2050-2100",
            "2100-2150",
            "2150-2200"
        ]
        regions = [
            "Arctic",
            "Amazon Rainforest",
            "Sahel",
            "Southeast Asian Archipelago",
            "Mediterranean Basin"
        ]
        climate_scenarios = [
            "RCP 2.6",
            "RCP 4.5",
            "RCP 6.0",
            "RCP 8.5"
        ]
        return {
            "1": {
                "climate_variable": random.choice(climate_variables),
                "time_period": random.choice(time_periods),
                "region": random.choice(regions),
                "climate_scenario": random.choice(climate_scenarios)
            },
            "2": {
                "climate_variable": random.choice(climate_variables),
                "time_period": random.choice(time_periods),
                "region": random.choice(regions),
                "climate_scenario": random.choice(climate_scenarios)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze historical climate data, create a predictive model, and design adaptive strategies for future scenarios while considering ethical implications. Focus on {t['climate_variable']} in the {t['region']} for the time period {t['time_period']}, considering the {t['climate_scenario']} scenario. Your response should include:

1. Historical Data Analysis (250-300 words):
   a) Describe the historical trends of {t['climate_variable']} in the {t['region']}.
   b) Identify key factors influencing these trends.
   c) Explain any significant patterns or anomalies in the data.

2. Predictive Model (300-350 words):
   a) Propose a method for creating a predictive model for {t['climate_variable']} in the {t['region']} for {t['time_period']} under the {t['climate_scenario']} scenario.
   b) Describe the key variables and data sources you would use in your model.
   c) Explain how your model accounts for potential tipping points or non-linear changes.
   d) Provide a hypothetical prediction with confidence intervals.

3. Adaptive Strategies (250-300 words):
   a) Based on your prediction, propose three adaptive strategies for the {t['region']}.
   b) Explain how each strategy addresses the projected changes in {t['climate_variable']}.
   c) Discuss the potential effectiveness and feasibility of each strategy.

4. Ethical Implications (200-250 words):
   a) Identify two potential ethical dilemmas arising from your adaptive strategies.
   b) Discuss how these dilemmas might affect different stakeholders in the {t['region']}.
   c) Propose guidelines for addressing these ethical concerns.

5. Interdisciplinary Integration (200-250 words):
   a) Explain how your analysis integrates knowledge from at least three different scientific disciplines.
   b) Discuss any challenges in synthesizing data or methods from these disciplines.
   c) Propose a novel research question that emerges from this interdisciplinary approach.

6. Uncertainty and Limitations (150-200 words):
   a) Discuss the main sources of uncertainty in your analysis and predictions.
   b) Explain how these uncertainties might affect decision-making based on your model.
   c) Propose methods for reducing or quantifying these uncertainties.

7. Global Context (150-200 words):
   a) Discuss how changes in {t['climate_variable']} in the {t['region']} might affect other regions or global systems.
   b) Propose a method for integrating your regional analysis into global climate models.

Ensure your response demonstrates a deep understanding of climate science, data analysis, and ethical reasoning. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section (numbered 1-7) and use lettered subheadings (a, b, c) within each section as outlined above. Your total response should be between 1500-1750 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must analyze historical trends of {t['climate_variable']} in the {t['region']}.",
            f"A predictive model for {t['climate_variable']} in the {t['region']} for {t['time_period']} under the {t['climate_scenario']} scenario must be proposed and explained.",
            "The predictive model must account for potential tipping points or non-linear changes.",
            f"Three adaptive strategies for the {t['region']} based on the prediction must be provided and discussed.",
            "Two potential ethical dilemmas arising from the adaptive strategies must be identified and discussed.",
            "The analysis must integrate knowledge from at least three different scientific disciplines, with specific examples provided.",
            "Main sources of uncertainty in the analysis and predictions must be discussed, along with their potential impact on decision-making.",
            f"The global impact of changes in {t['climate_variable']} in the {t['region']} must be addressed, including potential effects on other regions.",
            "The response must be formatted with clear numbered headings (1-7) and lettered subheadings (a, b, c) for each section as specified in the instructions.",
            "The response must be between 1500-1750 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
