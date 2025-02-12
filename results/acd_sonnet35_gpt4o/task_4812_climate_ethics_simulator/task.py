import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "policy_area": "energy transition",
                "region": "Southeast Asia",
                "time_frame": "50 years",
                "key_challenge": "balancing economic growth with emissions reduction",
                "current_data": {
                    "renewable_energy_share": "23%",
                    "annual_GDP_growth": "4.5%",
                    "carbon_emissions": "1.5 billion tonnes"
                }
            },
            {
                "policy_area": "urban planning",
                "region": "Sub-Saharan Africa",
                "time_frame": "30 years",
                "key_challenge": "managing rapid urbanization while adapting to climate change",
                "current_data": {
                    "urban_population_share": "40%",
                    "informal_settlement_rate": "62%",
                    "flood_risk_exposure": "18% of urban areas"
                }
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(scenarios)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a climate ethics simulation system that models the long-term effects of climate policies on environmental and social factors, then use it to make ethical decisions about resource allocation and policy implementation. Focus on {t['policy_area']} in {t['region']} over a {t['time_frame']} period, with the key challenge of {t['key_challenge']}. Current data for the region: {t['current_data']}.

Your response should include the following sections, clearly labeled:

1. Simulation System Design (250-300 words):
   a) Describe the key components and structure of your climate ethics simulation system.
   b) Explain how your system models the interactions between climate policies, environmental factors, and social outcomes.
   c) Detail the data sources and variables your system would use to generate predictions.
   d) Include a high-level diagram of your system architecture (described textually).

2. Predictive Modeling Approach (200-250 words):
   a) Explain the methodologies your system uses to generate long-term predictions.
   b) Discuss how your system accounts for uncertainty and complex system dynamics.
   c) Provide an example of how your system would predict the outcome of a specific policy intervention related to the given scenario.

3. Ethical Framework and Decision-Making (200-250 words):
   a) Describe the ethical framework your system uses to evaluate policy outcomes.
   b) Explain how your system weighs different ethical considerations (e.g., utilitarianism, environmental ethics, social justice).
   c) Provide an example of how your system would make an ethical judgment about a policy decision in the given scenario.

4. Policy Recommendations (150-200 words):
   a) Based on your simulation system, propose three specific policy recommendations for the given scenario.
   b) Explain the rationale behind each recommendation, considering both environmental and social impacts.
   c) Discuss potential trade-offs or ethical dilemmas associated with these recommendations.

5. Limitations and Future Improvements (100-150 words):
   a) Identify potential limitations or biases in your simulation system.
   b) Propose methods for validating and improving the accuracy of your system over time.

Ensure your response demonstrates a deep understanding of climate science, environmental policy, ethics, and complex systems modeling. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and addressing real-world constraints.

Your total response should be between 900-1150 words, with each section adhering to the specified word count ranges."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must focus on {t['policy_area']} in {t['region']} over a {t['time_frame']} period, addressing the key challenge of {t['key_challenge']}.",
            "The simulation system design should include all required components and demonstrate scientific plausibility.",
            "The predictive modeling approach should account for complex systems and uncertainty, with a relevant example provided.",
            "The ethical framework should consider multiple perspectives and include a scenario-specific example.",
            "Three specific, well-justified policy recommendations should be provided, with consideration of trade-offs.",
            "Limitations and future improvements should be thoughtfully addressed.",
            "The response should adhere to the specified word count ranges for each section.",
            "The overall response should demonstrate interdisciplinary knowledge integration and creative problem-solving."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
