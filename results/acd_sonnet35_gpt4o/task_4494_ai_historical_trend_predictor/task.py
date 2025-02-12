import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "historical_period": "Industrial Revolution",
                "societal_aspect": "Urbanization",
                "future_timeframe": "Next 50 years",
                "region": "Western Europe"
            },
            {
                "historical_period": "Information Age",
                "societal_aspect": "Work-life balance",
                "future_timeframe": "Next 30 years",
                "region": "East Asia"
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that analyzes historical data to predict future societal trends, then apply it to the following scenario:

Historical Period: {t['historical_period']}
Societal Aspect: {t['societal_aspect']}
Future Timeframe: {t['future_timeframe']}
Region: {t['region']}

Your response should include:

1. AI System Design (300-350 words):
   a) Describe the overall architecture of your AI system for historical trend analysis and prediction.
   b) Explain the key components, including data input, processing, and output mechanisms.
   c) Detail any novel algorithms or techniques your system employs for pattern recognition and prediction.
   d) Discuss how your system handles the complexity and nuances of historical data.

2. Data Sources and Preprocessing (200-250 words):
   a) Identify the types of historical data your system would use for analysis.
   b) Describe your approach to data collection, validation, and preprocessing.
   c) Explain how your system addresses potential biases or gaps in historical records.
   d) Discuss any ethical considerations in the use of historical data.

3. Historical Analysis (250-300 words):
   a) Explain how your AI system analyzes the historical period of {t['historical_period']}.
   b) Describe the key factors and variables your system considers for the societal aspect of {t['societal_aspect']}.
   c) Discuss how your system identifies and weighs the significance of historical events and trends.
   d) Explain how your system accounts for regional variations, focusing on {t['region']}.

4. Predictive Modeling (250-300 words):
   a) Detail the predictive modeling techniques your system uses to forecast trends for {t['future_timeframe']}.
   b) Explain how your system extrapolates from historical data to future scenarios.
   c) Describe how your system handles uncertainty and multiple possible futures.
   d) Discuss any limitations or potential biases in your predictive approach.

5. Scenario Application (300-350 words):
   a) Apply your AI system to predict how {t['societal_aspect']} might evolve in {t['region']} over {t['future_timeframe']}.
   b) Provide a detailed analysis of the predicted trends, including potential societal impacts.
   c) Identify key factors that could significantly alter these predictions.
   d) Discuss how policymakers or researchers might use these predictions.

6. Evaluation and Validation (200-250 words):
   a) Propose methods for evaluating the accuracy and reliability of your AI system's predictions.
   b) Describe how you would validate your system's performance against historical data.
   c) Discuss the challenges in assessing predictive accuracy for long-term societal trends.
   d) Suggest approaches for continually improving and updating your system.

Ensure your response demonstrates a deep understanding of AI, data analysis, historical trends, and societal dynamics. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1500-1800 words. Include a word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response adequately covers all six required sections, addressing the historical period of {t['historical_period']}, the societal aspect of {t['societal_aspect']}, the future timeframe of {t['future_timeframe']}, and the region of {t['region']}.",
            "The AI system design demonstrates a clear understanding of historical data analysis and predictive modeling techniques.",
            "The response shows creativity and innovation in the proposed AI system and its application to the given scenario.",
            "The submission includes a thoughtful analysis of data sources, preprocessing, and ethical considerations.",
            "The response provides a detailed and plausible prediction for the given scenario, including potential societal impacts.",
            "The submission discusses methods for evaluating and validating the AI system's predictions.",
            "The response maintains scientific plausibility while exploring novel ideas in AI-driven historical analysis and societal prediction.",
            "The submission includes a word count and falls within the specified range of 1500-1800 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
