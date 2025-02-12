class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"historical_data": [100, 105, 110, 115, 120, 125, 130, 135, 140, 145], 
                    "question": "Based on the historical data provided, forecast the next 5 data points using a linear trend model."},
            "2": {"historical_data": [150, 145, 140, 135, 130, 125, 120, 115, 110, 105], 
                    "question": "Analyze the historical data and provide a forecast for the next 5 data points, explaining any observed trend."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to analyze the provided historical financial data and generate a forecast based on the observed trends.\n\nHistorical Data: {t['historical_data']}\n\n{t['question']}\n\nProvide your forecast in a list format (e.g., [150, 155, 160, 165, 170]) and include a detailed explanation of the method used for your prediction. Ensure your explanation covers the reasoning behind the trend identified and how it was used to make the forecast. Avoid any assumptions not supported by the data. Your response should be clear, logically structured, and justified by the data provided."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        historical_data = t['historical_data']
        if 'linear trend' in t['question'].lower():
            criteria = ["The forecast should follow a linear trend based on the historical data.", "The forecast should consist of 5 data points.", "The explanation should clearly describe the linear trend method used.", "The explanation should be logically structured and justified by the data."]
        else:
            criteria = ["The forecast should analyze and explain any observed trend in the historical data.", "The forecast should consist of 5 data points.", "The explanation should clearly describe the trend observed and how it was used for forecasting.", "The explanation should be logically structured and justified by the data."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
