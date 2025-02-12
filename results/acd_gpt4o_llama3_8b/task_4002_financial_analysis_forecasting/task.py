class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "data": {
                    "Revenue": [1000, 1300, 1600, 1900, 2200],
                    "Expenses": [700, 850, 950, 1100, 1250],
                    "Quarter": ["Q1", "Q2", "Q3", "Q4", "Q5"]
                },
                "instructions": "Analyze the given financial data for the past 5 quarters. Calculate the profit for each quarter and determine the overall trend in profit. Additionally, provide a brief analysis of the financial health of the company based on this data. Submit your response as a plain text string in the format:\n\nQuarterly Profits: [list of profits]\nTrend Analysis: [your trend analysis]\nFinancial Health: [your financial health assessment]"
            },
            "2": {
                "data": {
                    "Revenue": [2000, 2400, 2600, 2800, 3000],
                    "Expenses": [1500, 1700, 1800, 2000, 2100],
                    "Quarter": ["Q1", "Q2", "Q3", "Q4", "Q5"]
                },
                "instructions": "Using the provided financial data for the past 5 quarters, forecast the revenue and expenses for the next 2 quarters. Explain the method you used for forecasting and any assumptions you made. Submit your response as a plain text string in the format:\n\nForecasted Revenue: [forecasted revenue for next 2 quarters]\nForecasted Expenses: [forecasted expenses for next 2 quarters]\nMethod and Assumptions: [your explanation of the method and assumptions]"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Perform financial analysis and make forecasts based on the given financial data.\n\nFinancial Data: {t['data']}\n\nInstructions: {t['instructions']}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The analysis should accurately reflect the calculations based on the data provided.",
            "The trend analysis and financial health assessment should be coherent and logical.",
            "The forecast should be based on a reasonable method, such as linear regression or moving averages, and clearly explain any assumptions made.",
            "The response should adhere to the specified format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
