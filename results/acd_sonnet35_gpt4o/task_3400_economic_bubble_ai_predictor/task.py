import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_biases = [
            "confirmation bias",
            "herding behavior",
            "overconfidence",
            "anchoring",
            "availability heuristic",
            "loss aversion"
        ]
        market_sectors = [
            "cryptocurrency",
            "real estate",
            "tech startups",
            "commodities",
            "stock market",
            "NFTs"
        ]
        return {
            "1": {
                "cognitive_bias": random.choice(cognitive_biases),
                "market_sector": random.choice(market_sectors)
            },
            "2": {
                "cognitive_bias": random.choice(cognitive_biases),
                "market_sector": random.choice(market_sectors)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system to model and predict the emergence of economic bubbles based on collective cognitive biases and market psychology, with a focus on the {t['cognitive_bias']} in the {t['market_sector']} sector. Then, analyze its potential impact on financial systems and policy-making. Your response should include the following sections:

1. AI System Architecture (300-350 words):
   a) Describe the key components of your AI system for modeling and predicting economic bubbles.
   b) Explain how your system incorporates {t['cognitive_bias']} and other relevant psychological factors.
   c) Detail how your system models the {t['market_sector']} sector and its unique characteristics.
   d) Discuss any novel machine learning techniques or data sources your system uses.

2. Bubble Prediction Mechanism (250-300 words):
   a) Explain the process by which your AI system identifies potential bubble formation.
   b) Describe how your system quantifies the influence of {t['cognitive_bias']} on market behavior.
   c) Discuss how your system distinguishes between normal market fluctuations and bubble formation.
   d) Provide an example scenario of how your system might predict a bubble in the {t['market_sector']} sector.

3. Model Validation and Testing (200-250 words):
   a) Propose a method for validating your AI system's predictions using historical data.
   b) Describe potential challenges in testing the system and how you would address them.
   c) Discuss how you would measure the accuracy and reliability of your system's predictions.

4. Financial System Impact Analysis (200-250 words):
   a) Analyze how widespread adoption of your AI system could impact financial markets and investment strategies.
   b) Discuss potential unintended consequences of using AI to predict economic bubbles.
   c) Explore how your system might influence market psychology and potentially create self-fulfilling prophecies.

5. Policy Implications (200-250 words):
   a) Discuss how policymakers and regulatory bodies could use your AI system to inform decision-making.
   b) Propose specific policy recommendations based on the insights provided by your system.
   c) Analyze potential risks and ethical considerations of using AI predictions to guide economic policy.

6. Limitations and Future Directions (150-200 words):
   a) Identify key limitations of your current AI system and areas for improvement.
   b) Propose future research directions to enhance the system's predictive capabilities.
   c) Discuss how your approach could be adapted to model other complex economic phenomena.

Ensure your response demonstrates a deep understanding of behavioral economics, financial markets, machine learning, and complex systems modeling. Use technical terminology appropriately and provide clear explanations where necessary. Be innovative in your approach while maintaining scientific and economic plausibility.

Format your response with clear headings for each section and number your paragraphs within each section. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must demonstrate a clear understanding of {t['cognitive_bias']} and its potential influence on the {t['market_sector']} sector.",
            "The AI system design should be innovative yet scientifically and economically plausible.",
            "The bubble prediction mechanism should be logically sound and incorporate relevant psychological and economic factors.",
            "The model validation and testing approach should be comprehensive and address potential challenges.",
            "The financial system impact analysis should be thorough and consider multiple perspectives.",
            "The policy implications should be well-reasoned and consider potential risks and ethical issues.",
            "The limitations and future directions should be insightful and demonstrate a deep understanding of the field.",
            "The overall response should showcase interdisciplinary thinking and creative problem-solving."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
