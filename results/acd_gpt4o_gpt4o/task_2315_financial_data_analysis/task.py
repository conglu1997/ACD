class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "financial_data": {
                    "AAPL": {"price": [150, 155, 160, 158, 162], "volume": [1000000, 1100000, 1050000, 1080000, 1070000], "PE_ratio": 32.5, "market_cap": 2.5E12, "dividend_yield": 0.6, "EPS": 5.2, "beta": 1.2},
                    "GOOG": {"price": [2800, 2820, 2830, 2840, 2850], "volume": [500000, 510000, 520000, 530000, 540000], "PE_ratio": 28.7, "market_cap": 1.8E12, "dividend_yield": 0.0, "EPS": 90.5, "beta": 1.1}
                },
                "investment_goal": "short-term growth"
            },
            "2": {
                "financial_data": {
                    "MSFT": {"price": [300, 305, 310, 315, 320], "volume": [900000, 920000, 940000, 930000, 950000], "PE_ratio": 35.2, "market_cap": 2.3E12, "dividend_yield": 1.0, "EPS": 8.1, "beta": 0.9},
                    "AMZN": {"price": [3300, 3350, 3400, 3450, 3500], "volume": [400000, 420000, 410000, 430000, 440000], "PE_ratio": 60.1, "market_cap": 1.6E12, "dividend_yield": 0.0, "EPS": 52.6, "beta": 1.3}
                },
                "investment_goal": "long-term stability"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return "Your task is to analyze the given financial data and provide investment advice based on the investment goal. The financial data is provided in dictionary format with stock symbols as keys and their respective price, volume, P/E ratio, market cap, dividend yield, EPS, and beta as values. The investment goal describes whether the focus is on short-term growth or long-term stability. Provide your analysis and advice in plain text format, ensuring it is clear, logical, and aligns with the investment goal. Structure your response as follows:\n\nAnalysis: [Your analysis of the data]\nAdvice: [Your investment advice based on the analysis]"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The analysis should accurately interpret the financial data.",
            "The investment advice should align with the given investment goal.",
            "The reasoning should be clear and logical."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
