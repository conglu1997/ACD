class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"revenue": [1000, 1500, 2000, 2500], "expenses": [500, 700, 900, 1100]},
            "2": {"revenue": [1200, 1800, 2400, 3000], "expenses": [600, 800, 1000, 1200]},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return """You are given the revenue and expenses for a company over four quarters. Your task is to calculate the total profit for each quarter and provide a brief analysis of the company's financial performance. The analysis should include insights on trends and any recommendations for improving profitability. Here are the data:

Revenue: {t['revenue']}
Expenses: {t['expenses']}

Your response should be in the following format:
1. Total profit for each quarter: [list the profits]
2. Analysis: [provide insights on trends in revenue and expenses]
3. Recommendations: [provide actionable recommendations for improving profitability]

Example response format:
1. Total profit for each quarter: [500, 800, 1100, 1400]
2. Analysis: The revenue shows a consistent increase each quarter, while the expenses also rise but at a slower rate. This indicates improved efficiency over time.
3. Recommendations: To further improve profitability, consider optimizing the supply chain to reduce expenses in the earlier quarters."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include the total profit for each quarter.",
            "The analysis should identify trends in revenue and expenses.",
            "The recommendations should be relevant and actionable."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
