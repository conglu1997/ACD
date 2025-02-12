import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "historical_period": "Industrial Revolution",
                "future_timeframe": "2050",
                "technological_focus": "Artificial Intelligence",
                "social_aspect": "Work and Employment"
            },
            {
                "historical_period": "Information Age",
                "future_timeframe": "2100",
                "technological_focus": "Biotechnology",
                "social_aspect": "Family Structures"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that analyzes historical societal trends and predicts future societal changes, focusing on the impact of technological advancements on social structures. Apply your system to analyze the transition from the {t['historical_period']} to the present day, and then predict societal changes up to the year {t['future_timeframe']}, with a specific focus on how {t['technological_focus']} might impact {t['social_aspect']}. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for temporal societal analysis.
   b) Explain how your system integrates historical data, current trends, and predictive modeling.
   c) Discuss any novel elements in your design that enable long-term societal predictions.
   d) Include a simple diagram or flowchart of your system architecture (describe it textually).

2. Historical Analysis (200-250 words):
   a) Explain how your system analyzes the transition from the {t['historical_period']} to the present day.
   b) Describe the key data sources and analytical methods used.
   c) Discuss how your system identifies and weighs significant societal trends and technological impacts.

3. Predictive Modeling (250-300 words):
   a) Detail the predictive modeling techniques your system uses to forecast societal changes up to {t['future_timeframe']}.
   b) Explain how your system accounts for potential technological disruptions and their societal impacts.
   c) Describe how the system handles uncertainty and multiple possible future scenarios.
   d) Include a brief example of a predictive algorithm or model used in your system.

4. Case Study: {t['technological_focus']} and {t['social_aspect']} (300-350 words):
   a) Apply your AI system to analyze how {t['technological_focus']} might impact {t['social_aspect']} by {t['future_timeframe']}.
   b) Provide a detailed prediction of potential changes, supported by your system's historical analysis and predictive modeling.
   c) Discuss any potential ethical implications or societal challenges that may arise from these predicted changes.
   d) Include at least one quantitative prediction (e.g., percentage change in a relevant metric) and explain its derivation.

5. Evaluation and Validation (150-200 words):
   a) Propose methods to evaluate the accuracy and reliability of your system's predictions.
   b) Discuss how you would validate your system's outputs against real-world data and expert opinions.
   c) Address potential biases or limitations in your approach.

6. Ethical Considerations (150-200 words):
   a) Discuss ethical implications of using AI to predict long-term societal changes.
   b) Address potential misuse or misinterpretation of your system's predictions.
   c) Propose guidelines for responsible development and use of temporal societal analysis AI systems.

7. Interdisciplinary Implications (150-200 words):
   a) Discuss how your system could contribute to fields such as sociology, economics, and public policy.
   b) Propose potential applications in areas like urban planning, education reform, or global development strategies.
   c) Suggest future research directions based on your system's approach.

Ensure your response demonstrates a deep understanding of historical analysis, sociological theories, and artificial intelligence. Use appropriate terminology and provide clear explanations for complex concepts. Be creative and speculative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section and subsections labeled a, b, c, etc., as appropriate. Your total response should be between 1450-1800 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of historical analysis, sociological theories, and artificial intelligence, specifically addressing the transition from {t['historical_period']} to the present and predictions up to {t['future_timeframe']}.",
            "The AI system design effectively integrates historical data analysis and predictive modeling for long-term societal changes.",
            f"The case study provides a detailed and plausible prediction of how {t['technological_focus']} might impact {t['social_aspect']} by {t['future_timeframe']}, including at least one quantitative prediction.",
            "The response addresses ethical considerations and proposes guidelines for responsible use of such AI systems.",
            "The interdisciplinary implications and potential applications are thoughtfully discussed.",
            "The response is creative and speculative while maintaining scientific plausibility.",
            "Appropriate technical terminology is used throughout with clear explanations provided.",
            "The response follows the specified format and word count requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
