import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environmental_factors = [
            "carbon emissions",
            "biodiversity",
            "ocean acidification",
            "deforestation"
        ]
        economic_factors = [
            "GDP growth",
            "employment rates",
            "income inequality",
            "energy prices"
        ]
        policy_types = [
            "carbon pricing",
            "renewable energy subsidies",
            "reforestation initiatives",
            "circular economy regulations"
        ]
        regions = [
            "North America",
            "European Union",
            "East Asia",
            "Sub-Saharan Africa"
        ]
        return {
            "1": {
                "environmental_factor": random.choice(environmental_factors),
                "economic_factor": random.choice(economic_factors),
                "policy_type": random.choice(policy_types),
                "region": random.choice(regions)
            },
            "2": {
                "environmental_factor": random.choice(environmental_factors),
                "economic_factor": random.choice(economic_factors),
                "policy_type": random.choice(policy_types),
                "region": random.choice(regions)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a climate policy simulation system and use it to analyze the impact of a novel policy intervention. Your task has the following components:

1. Simulation System Design (300-350 words):
   a) Describe the key components of your climate policy simulation system.
   b) Explain how your system models the interactions between environmental factors, economic indicators, and policy interventions.
   c) Detail how you incorporate uncertainty and feedback loops in your model.
   d) Discuss any machine learning or AI techniques used in your simulation.

2. Data Integration and Analysis (250-300 words):
   a) Explain how your system integrates and analyzes data from diverse sources.
   b) Describe your approach to handling data gaps and inconsistencies across different regions and time scales.
   c) Discuss how your system validates its predictions against historical data.
   d) Include a hypothetical dataset structure for {t['environmental_factor']} and {t['economic_factor']} in {t['region']}.

3. Policy Design and Analysis (300-350 words):
   a) Propose a novel policy intervention related to {t['policy_type']} that aims to improve {t['environmental_factor']} while minimizing negative impacts on {t['economic_factor']} in {t['region']}.
   b) Use your simulation system to analyze the potential impacts of this policy over a 30-year timeframe.
   c) Provide quantitative predictions for key environmental and economic indicators.
   d) Discuss any unexpected outcomes or secondary effects revealed by your simulation.

4. Sensitivity Analysis (200-250 words):
   a) Perform a sensitivity analysis to identify the most critical variables in your model.
   b) Explain how changes in these variables affect the outcomes of your proposed policy.
   c) Discuss the implications of this analysis for real-world policy implementation.
   d) Include a table or graph illustrating the sensitivity analysis results.

5. Cross-disciplinary Implications (200-250 words):
   a) Analyze how insights from your simulation could inform research in environmental science, economics, and public policy.
   b) Discuss potential applications of your system in other domains (e.g., urban planning, public health).
   c) Propose a research agenda that builds on the capabilities of your simulation system.

6. Ethical Considerations and Limitations (200-250 words):
   a) Discuss ethical considerations in using simulations to inform real-world policy decisions.
   b) Address potential biases in your model and how they might affect policy recommendations.
   c) Explain limitations of your approach and areas for future improvement.

Ensure your response demonstrates a deep understanding of climate science, economics, data analysis, and policy-making. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Include at least one table or graph in your response. Your total response should be between 1450-1750 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a comprehensive understanding of climate science, economics, and policy-making, particularly in relation to {t['environmental_factor']}, {t['economic_factor']}, and {t['policy_type']} in {t['region']}.",
            "The proposed simulation system is innovative, scientifically plausible, and incorporates appropriate machine learning or AI techniques.",
            f"The policy analysis is thorough, considering multiple factors and potential outcomes specific to {t['region']}.",
            "The sensitivity analysis is well-executed, with a clear table or graph illustrating the results.",
            "The cross-disciplinary implications are thoughtfully explored, with a concrete research agenda proposed.",
            "Ethical considerations and limitations are adequately addressed, including potential biases in the model.",
            "The response includes the required table or graph and falls within the specified word count range."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
