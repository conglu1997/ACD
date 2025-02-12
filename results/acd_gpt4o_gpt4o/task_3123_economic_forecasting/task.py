class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "data": {
                    "GDP_growth_rate": 2.5,
                    "unemployment_rate": 5.0,
                    "inflation_rate": 1.8,
                    "interest_rate": 0.5,
                    "consumer_confidence_index": 103.4,
                    "trade_balance": -2.8
                },
                "forecast_period": "next 5 years",
                "objective": "Analyze the provided economic indicators and forecast the economic conditions for the next 5 years. Provide recommendations for monetary and fiscal policy adjustments to maintain economic stability."
            },
            "2": {
                "data": {
                    "GDP_growth_rate": -1.2,
                    "unemployment_rate": 8.5,
                    "inflation_rate": 3.5,
                    "interest_rate": 1.0,
                    "consumer_confidence_index": 87.6,
                    "trade_balance": -4.5
                },
                "forecast_period": "next 3 years",
                "objective": "Analyze the provided economic indicators and forecast the economic conditions for the next 3 years. Provide recommendations for policy measures to combat economic recession and promote recovery."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to analyze the following economic data and provide a forecast and recommendations based on the given indicators.

Economic Data: {t['data']}

Forecast Period: {t['forecast_period']}

Objective: {t['objective']}

Provide a detailed analysis and forecast of the economic conditions for the specified period. Include recommendations for monetary and fiscal policy adjustments to achieve the objective. Your analysis should be logical, well-structured, and demonstrate a clear understanding of economic principles. Provide your response in plain text format with the following sections:

1. Economic Analysis
2. Forecast
3. Policy Recommendations"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The analysis should be based on the provided economic indicators.",
            "The forecast should cover the specified period.",
            "The recommendations should address the specified objective.",
            "The analysis should demonstrate an understanding of economic principles and their interdependencies.",
            "The response should be clear, logical, and well-structured.",
            "The response should include sections for Economic Analysis, Forecast, and Policy Recommendations."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
