class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "task_description": "Analyze the given historical stock price data for Company XYZ and provide insights.",
                "data": "Date,Close\n2023-01-01,150\n2023-02-01,155\n2023-03-01,160\n2023-04-01,158\n2023-05-01,162\n2023-06-01,165\n2023-07-01,170\n2023-08-01,175\n2023-09-01,180\n2023-10-01,185",
                "instructions": "Analyze the following historical stock price data for Company XYZ and provide insights on the trends you observe. Your insights should include: 1. Identification of any significant trends or patterns. 2. Possible reasons for these trends based on historical market events. 3. Predictions for future stock movements based on the observed data. Submit your analysis as a plain text string in the following format:\n\nInsights:\n[Your insights]\n"
            },
            "2": {
                "task_description": "Compare the stock performance of Company ABC and Company DEF over the past year and provide a detailed analysis.",
                "data": "Company ABC\nDate,Close\n2023-01-01,100\n2023-02-01,105\n2023-03-01,110\n2023-04-01,108\n2023-05-01,115\n2023-06-01,120\n2023-07-01,125\n2023-08-01,130\n2023-09-01,135\n2023-10-01,140\n\nCompany DEF\nDate,Close\n2023-01-01,200\n2023-02-01,195\n2023-03-01,190\n2023-04-01,185\n2023-05-01,180\n2023-06-01,175\n2023-07-01,170\n2023-08-01,165\n2023-09-01,160\n2023-10-01,155",
                "instructions": "Compare the stock performance of Company ABC and Company DEF over the past year using the provided data. Your analysis should include: 1. A comparison of the overall performance of both companies. 2. Identification of any significant differences or similarities in their stock movements. 3. Possible reasons for these differences or similarities, considering market and company-specific events. Submit your analysis as a plain text string in the following format:\n\nAnalysis:\n[Your analysis]\n"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the following stock market data: {t['task_description']}. Ensure that your analysis includes the specified components. Here are the detailed instructions:\n\n{t['instructions']}\n\nData:\n{t['data']}\n"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The analysis should be clear and logically structured.",
            "The analysis should accurately cover the specified components.",
            "The insights/predictions should be reasonable and based on the provided data."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
