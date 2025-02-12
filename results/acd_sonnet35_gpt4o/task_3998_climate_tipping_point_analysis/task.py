import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        climate_systems = ['Arctic sea ice', 'Amazon rainforest', 'Thermohaline circulation', 'Permafrost']
        socio_economic_scenarios = ['Rapid decarbonization', 'Business as usual', 'Technological breakthrough', 'Global economic crisis']
        time_horizons = [2050, 2075, 2100]
        
        return {
            "1": {
                "climate_system": random.choice(climate_systems),
                "scenario": random.choice(socio_economic_scenarios),
                "time_horizon": random.choice(time_horizons)
            },
            "2": {
                "climate_system": random.choice(climate_systems),
                "scenario": random.choice(socio_economic_scenarios),
                "time_horizon": random.choice(time_horizons)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a complex systems model to predict climate tipping points for the {t['climate_system']} system under the {t['scenario']} scenario, with a time horizon of {t['time_horizon']}. Then, develop adaptive strategies based on your analysis. Your response should include:

1. Model Design (300-350 words):
   a) Describe the key components and interactions of your complex systems model for the {t['climate_system']}.
   b) Explain how your model incorporates feedback loops and non-linear dynamics.
   c) Detail how you integrate socio-economic factors from the {t['scenario']} scenario into your climate model.
   d) Discuss any novel approaches or algorithms used in your model design.

2. Data Integration and Analysis (250-300 words):
   a) Specify the types of data your model requires and potential sources.
   b) Explain how you handle data uncertainty and variability in your model.
   c) Describe your approach to sensitivity analysis and model validation.
   d) Discuss how you identify and characterize potential tipping points in the {t['climate_system']}.

3. Tipping Point Predictions (250-300 words):
   a) Present your model's predictions for potential tipping points in the {t['climate_system']} up to {t['time_horizon']}.
   b) Analyze the key factors contributing to these tipping points.
   c) Discuss the level of confidence in your predictions and any critical uncertainties.
   d) Compare your results with existing research and explain any discrepancies.

4. Adaptive Strategies (300-350 words):
   a) Propose three adaptive strategies to mitigate or manage the predicted tipping points.
   b) Explain how each strategy addresses specific vulnerabilities identified in your analysis.
   c) Discuss the potential effectiveness and feasibility of each strategy within the {t['scenario']} scenario.
   d) Analyze potential unintended consequences or cascading effects of implementing these strategies.

5. Decision-Making Framework (200-250 words):
   a) Develop a framework for decision-making under the uncertainty revealed by your model.
   b) Explain how this framework balances short-term costs with long-term resilience.
   c) Discuss how your framework accounts for potential irreversibility of tipping points.
   d) Propose metrics for monitoring and evaluating the effectiveness of adaptive strategies over time.

6. Interdisciplinary Implications (200-250 words):
   a) Analyze how your model and findings might inform policy decisions in other sectors (e.g., energy, agriculture, urban planning).
   b) Discuss potential economic impacts of your predicted tipping points and proposed strategies.
   c) Consider the ethical implications of your analysis, particularly regarding intergenerational equity and global justice.
   d) Suggest areas for future research to improve understanding and management of climate tipping points.

Ensure your response demonstrates a deep understanding of climate science, complex systems modeling, and strategic decision-making under uncertainty. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and rigorous analysis.

Format your response with clear headings for each section. Your total response should be between 1500-1800 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of climate science, complex systems modeling, and decision-making under uncertainty.",
            f"The model design effectively incorporates the {t['climate_system']} and the {t['scenario']} scenario.",
            "The analysis provides plausible predictions for climate tipping points and thoughtful adaptive strategies.",
            "The proposed decision-making framework effectively addresses uncertainty and long-term consequences.",
            "The response shows innovative approaches while maintaining scientific rigor and plausibility.",
            "The interdisciplinary implications are well-considered and insightful.",
            "The answer covers all required sections with appropriate detail and word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
