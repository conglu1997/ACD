import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        policies = [
            {
                "policy": "Increase in minimum wage by 20%",
                "economic_variables": {
                    "unemployment_rate": 5.2,
                    "inflation_rate": 2.1,
                    "gdp_growth": 2.8,
                    "consumer_spending": 68.2,
                    "business_investment": 17.5
                }
            },
            {
                "policy": "Reduction in corporate tax rate from 25% to 20%",
                "economic_variables": {
                    "unemployment_rate": 4.8,
                    "inflation_rate": 1.9,
                    "gdp_growth": 3.1,
                    "consumer_spending": 70.1,
                    "business_investment": 18.2
                }
            }
        ]
        return {str(i+1): policy for i, policy in enumerate(policies)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the potential effects of the following economic policy change in a simulated economy:

Policy: {t['policy']}

Current economic variables:
{', '.join([f'{k}: {v}%' for k, v in t['economic_variables'].items()])}

Your task:
1. Predict the likely changes in each economic variable over the next 12 months as a result of this policy. Provide a brief explanation for each prediction.
2. Describe potential secondary effects or unintended consequences of this policy.
3. Suggest one additional policy that could be implemented to mitigate any negative effects you've identified.

Format your response as follows:

Predictions:
[List each economic variable with its predicted value and a brief explanation]

Secondary Effects:
[Your analysis of potential secondary effects or unintended consequences]

Mitigating Policy:
[Your suggestion for an additional policy to mitigate negative effects]

Ensure your analysis is economically sound, considers the interdependencies between variables, and is clearly explained."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding of economic principles and the interdependencies between variables",
            "The predictions are logically consistent and well-explained",
            "The analysis of secondary effects shows depth of economic reasoning",
            "The suggested mitigating policy is relevant and well-justified",
            "The overall response is clear, coherent, and demonstrates strong economic analysis skills"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
