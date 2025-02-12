import random
from typing import List, Optional

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        climate_systems = [
            "Arctic sea ice",
            "Amazon rainforest",
            "West Antarctic Ice Sheet",
            "Atlantic Meridional Overturning Circulation",
            "Permafrost thawing"
        ]
        return {
            "1": {"climate_system": random.choice(climate_systems)},
            "2": {"climate_system": random.choice(climate_systems)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system to analyze multi-dimensional climate data and predict potential tipping points for the {t['climate_system']}, then propose adaptive strategies. Your response should include:\n\n1. System Architecture (300-350 words):\n   a) Describe the key components of your AI system for climate tipping point prediction.\n   b) Explain how your system integrates various types of climate data.\n   c) Detail the machine learning algorithms or models used in your system.\n   d) Discuss any novel approaches in your design for handling complex, non-linear climate systems.\n   e) Include a high-level diagram or pseudocode illustrating your system's architecture.\n\n2. Data Analysis and Integration (250-300 words):\n   a) Identify the types of data your system would use for the {t['climate_system']}.\n   b) Explain how you would preprocess and integrate data from different sources and scales.\n   c) Discuss how your system handles uncertainties and gaps in climate data.\n   d) Describe any data visualization techniques your system employs.\n   e) Include at least one example of a hypothetical data point or statistical measure relevant to the {t['climate_system']}.\n\n3. Tipping Point Prediction Methodology (250-300 words):\n   a) Explain your system's approach to identifying potential tipping points.\n   b) Describe how your AI accounts for feedback loops and non-linear dynamics in the {t['climate_system']}.\n   c) Discuss how your system quantifies and communicates the uncertainty in its predictions.\n   d) Provide an example of how your system might predict a specific tipping point scenario, including at least one quantitative threshold or probability estimate.\n\n4. Adaptive Strategies Generation (200-250 words):\n   a) Describe how your AI system generates adaptive strategies based on its predictions.\n   b) Explain how these strategies account for socio-economic factors and feasibility.\n   c) Provide two example adaptive strategies your system might propose for the {t['climate_system']}, including quantitative goals or targets.\n   d) Discuss how your system evaluates and ranks different adaptive strategies.\n\n5. Ethical Considerations and Policy Implications (200-250 words):\n   a) Discuss the ethical implications of using AI for climate prediction and policy recommendations.\n   b) Address potential biases in your system and how they might be mitigated.\n   c) Explain how your system could interface with policymakers and the public.\n   d) Propose guidelines for the responsible use of AI in climate science and policy.\n\n6. System Evaluation and Limitations (150-200 words):\n   a) Propose methods to evaluate the accuracy and reliability of your system's predictions, including specific performance metrics.\n   b) Discuss the limitations of your approach and potential areas for improvement.\n   c) Suggest future research directions to enhance the capabilities of your system.\n\nEnsure your response demonstrates a deep understanding of climate science, data analysis, machine learning, and environmental policy. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility. Include quantitative elements throughout your response where relevant.\n\nFormat your response with clear headings for each section. Your total response should be between 1350-1650 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of climate science and the specific climate system mentioned.",
            "The AI system design is innovative, well-structured, and appropriate for the complex task of climate tipping point prediction.",
            "The data analysis and integration approach is thorough and accounts for the challenges of climate data, including specific examples of data points or statistical measures.",
            "The tipping point prediction methodology is scientifically sound and accounts for the complexities of non-linear climate systems, with quantitative thresholds or probability estimates.",
            "The adaptive strategies generated are practical, consider socio-economic factors, and are relevant to the specific climate system, including quantitative goals or targets.",
            "Ethical considerations and policy implications are thoughtfully addressed.",
            "The system evaluation is critical, identifies genuine limitations, and includes specific performance metrics.",
            "The response incorporates quantitative elements throughout, demonstrating the ability to integrate numerical reasoning with qualitative analysis."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
