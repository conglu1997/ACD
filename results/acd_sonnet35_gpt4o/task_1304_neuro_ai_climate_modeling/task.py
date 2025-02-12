import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        climate_scenarios = [
            {
                "scenario": "Rising sea levels",
                "time_frame": "100 years",
                "region": "Coastal cities",
                "constraint": "Limited resources for infrastructure changes"
            },
            {
                "scenario": "Increasing frequency of extreme weather events",
                "time_frame": "50 years",
                "region": "Agricultural areas",
                "constraint": "Technological limitations in weather prediction"
            }
        ]
        return {
            "1": climate_scenarios[0],
            "2": climate_scenarios[1]
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a neural network architecture inspired by the prefrontal cortex and hippocampus for long-term climate modeling and policy recommendation. Your task involves the following steps:

1. Neural Network Architecture (300-350 words):
   a) Describe the overall structure of your neural network, explaining how it mimics the functions of the prefrontal cortex and hippocampus.
   b) Detail the specific layers and connections in your network, including any novel elements.
   c) Explain how your architecture enables long-term prediction and decision-making in the context of climate modeling.
   d) Discuss how your network incorporates memory and learning mechanisms inspired by these brain regions.

2. Data Integration and Processing (250-300 words):
   a) Describe the types of climate and environmental data your network would use as input.
   b) Explain how your network would preprocess and integrate diverse data sources.
   c) Discuss any challenges in data representation and how your architecture addresses them.
   d) Propose a method for incorporating uncertainty and variability in climate data.

3. Climate Modeling Approach (250-300 words):
   a) Explain how your neural network would model long-term climate changes for the scenario: {t['scenario']}
   b) Describe how your network accounts for the specified time frame of {t['time_frame']}.
   c) Discuss how your model handles complex interactions between different climate factors.
   d) Explain how your network could adapt its predictions based on new data or changing conditions.

4. Policy Recommendation Generation (250-300 words):
   a) Describe how your network would generate policy recommendations for the given scenario and region ({t['region']}).
   b) Explain how the network balances short-term and long-term consequences in its recommendations.
   c) Discuss how your network addresses the constraint: {t['constraint']}
   d) Propose a method for evaluating the potential impact and feasibility of the generated recommendations.
   e) Provide a brief example of one specific policy recommendation your system might generate (50-75 words).

5. Ethical Considerations and Limitations (200-250 words):
   a) Discuss potential biases or limitations in your neural network architecture and how they might affect climate predictions or policy recommendations.
   b) Explain how your system could ensure transparency and interpretability in its decision-making process.
   c) Propose safeguards to prevent misuse or over-reliance on the system's recommendations.
   d) Discuss the ethical implications of using AI for climate policy decisions.

6. Comparative Analysis (200-250 words):
   a) Compare your neuro-inspired approach to traditional climate modeling techniques, highlighting potential advantages and disadvantages.
   b) Discuss how your architecture might perform differently from current AI systems used in climate science.
   c) Propose a method for empirically evaluating the performance of your system against existing approaches.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and climate science. Be creative in your approach while maintaining scientific plausibility. Use clear headings for each section of your response.

Your total response should be between 1500-1800 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The neural network architecture is well-described and clearly inspired by the prefrontal cortex and hippocampus.",
            "The approach to data integration and processing is comprehensive and addresses challenges in climate data representation.",
            f"The climate modeling approach effectively addresses the given scenario ({t['scenario']}) and time frame ({t['time_frame']}).",
            f"The policy recommendation generation process is well-explained and considers the given region ({t['region']}) and constraint ({t['constraint']}).",
            "A specific example of a policy recommendation is provided.",
            "Ethical considerations and limitations are thoroughly discussed with proposed safeguards.",
            "The comparative analysis provides insightful comparisons with traditional methods and proposes a valid evaluation approach.",
            "The response demonstrates a deep understanding of neuroscience, AI, and climate science concepts.",
            "The proposed solutions are creative while maintaining scientific plausibility.",
            "The response follows the specified format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
