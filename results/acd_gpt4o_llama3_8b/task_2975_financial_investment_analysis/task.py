class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "financial_data": {
                    "Company": ["A", "B", "C"],
                    "Stock Price": [150, 200, 100],
                    "P/E Ratio": [15, 20, 10],
                    "Dividend Yield": [2.5, 1.8, 3.0]
                },
                "guidelines": "Prioritize companies with low P/E ratios and high dividend yields."
            },
            "2": {
                "financial_data": {
                    "Company": ["X", "Y", "Z"],
                    "Stock Price": [250, 300, 150],
                    "P/E Ratio": [25, 30, 12],
                    "Dividend Yield": [1.5, 1.2, 4.0]
                },
                "guidelines": "Focus on companies with moderate stock prices and stable dividend yields."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        financial_data_str = "\n".join([f"Company: {t['financial_data']['Company'][i]}, Stock Price: {t['financial_data']['Stock Price'][i]}, P/E Ratio: {t['financial_data']['P/E Ratio'][i]}, Dividend Yield: {t['financial_data']['Dividend Yield'][i]}" for i in range(len(t['financial_data']['Company']))])
        return f"""You are tasked with analyzing the following financial data and making investment recommendations based on the provided guidelines.

Financial Data:
{financial_data_str}

Guidelines:
{t['guidelines']}

Your recommendation should include:
1. Identification of the best investment option based on the guidelines.
2. Explanation of why you chose this option, considering the given financial metrics.

Submit your response as a plain text string in the following format:
Recommendation: [Your recommendation]
Explanation: [Your explanation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The recommendation should align with the provided guidelines.",
            "The explanation should consider the given financial metrics and justify the choice.",
            "The response should follow the specified format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
