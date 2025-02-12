import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        climate_phenomena = [
            "Arctic sea ice decline",
            "Coral reef bleaching",
            "Extreme weather events",
            "Ocean acidification"
        ]
        ai_techniques = [
            "Deep learning",
            "Reinforcement learning",
            "Federated learning",
            "Explainable AI"
        ]
        return {
            "1": {
                "climate_phenomenon": random.choice(climate_phenomena),
                "ai_technique": random.choice(ai_techniques)
            },
            "2": {
                "climate_phenomenon": random.choice(climate_phenomena),
                "ai_technique": random.choice(ai_techniques)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an advanced AI system for climate modeling that integrates machine learning, big data analysis, and predictive modeling to improve our understanding of climate change and its impacts. Focus on the climate phenomenon of {t['climate_phenomenon']} and incorporate the AI technique of {t['ai_technique']}. Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the overall structure of your AI climate modeling system.
   b) Explain how your system incorporates machine learning, big data analysis, and predictive modeling.
   c) Detail how you integrate {t['ai_technique']} into your system architecture.
   d) Provide a high-level diagram of your architecture using ASCII art or a detailed textual description.

2. Data Integration and Preprocessing (250-300 words):
   a) Discuss the types of data your system would use for modeling {t['climate_phenomenon']}.
   b) Explain your approach to data integration from various sources (e.g., satellite data, ground-based sensors, historical records).
   c) Describe any novel data preprocessing techniques your system employs.
   d) Provide an example of how you would preprocess a specific data point related to {t['climate_phenomenon']}.

3. Model Development and Training (250-300 words):
   a) Explain your approach to developing and training climate models within your AI system.
   b) Discuss how you handle challenges such as model uncertainty and bias.
   c) Describe how {t['ai_technique']} is specifically used in model development or training.
   d) Provide a pseudocode snippet (5-10 lines) illustrating a key aspect of your model training process.

4. Predictive Capabilities (200-250 words):
   a) Outline the specific predictions your system can make regarding {t['climate_phenomenon']}.
   b) Explain how your system quantifies and communicates uncertainty in its predictions.
   c) Discuss any novel predictive capabilities enabled by your AI approach.
   d) Provide an example prediction format, including uncertainty quantification.

5. Validation and Evaluation (200-250 words):
   a) Propose methods for validating your AI climate models against observed data.
   b) Describe how you would evaluate the performance of your system compared to traditional climate models.
   c) Discuss any ethical considerations in the validation and use of your AI climate modeling system.
   d) Suggest a specific metric for evaluating your system's performance on {t['climate_phenomenon']} prediction.

6. Potential Applications and Impacts (150-200 words):
   a) Suggest two potential real-world applications of your AI climate modeling system.
   b) Discuss how these applications could contribute to climate change mitigation or adaptation strategies.
   c) Analyze potential societal impacts of using AI for climate modeling and prediction.

7. Future Directions (150-200 words):
   a) Propose two areas for future research or improvement in AI-driven climate modeling.
   b) Discuss how advancements in AI hardware or algorithms might impact climate modeling capabilities.
   c) Suggest an experiment to further validate or extend your system's capabilities.

Ensure your response demonstrates a deep understanding of climate science, artificial intelligence, and data analysis. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section and subsections labeled a, b, c, d as appropriate. Your total response should be between 1500-1850 words. Include a word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response addresses all seven required sections comprehensively, including all subsections.",
            f"The system architecture effectively incorporates {t['ai_technique']} and is well-explained, with a clear diagram or description provided.",
            f"The approach to modeling {t['climate_phenomenon']} is scientifically sound, innovative, and includes specific examples of data preprocessing and model training.",
            "The response demonstrates a deep understanding of both climate science and artificial intelligence, using appropriate technical terminology.",
            "The proposed system offers novel capabilities or insights beyond traditional climate modeling approaches, with clear examples of predictive capabilities.",
            "The discussion of validation, evaluation, and ethical considerations is thorough and includes specific metrics for performance evaluation.",
            "The potential applications and future directions are well-reasoned, impactful, and directly related to the proposed system.",
            "The writing is clear, well-structured, and adheres to the specified format and word count requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
