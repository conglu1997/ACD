class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"financial_data": "Company: XYZ Corp\nRevenue: $500,000\nExpenses: $350,000\nNet Profit: $150,000\nAssets: $1,200,000\nLiabilities: $600,000\nMarket Trends: Increasing demand for tech products.", "criteria": "Propose an investment strategy for XYZ Corp considering the given market trends."},
            "2": {"financial_data": "Company: ABC Inc\nRevenue: $1,200,000\nExpenses: $1,000,000\nNet Profit: $200,000\nAssets: $2,500,000\nLiabilities: $1,500,000\nMarket Trends: Decreasing interest in traditional retail.", "criteria": "Propose an investment strategy for ABC Inc considering the given market trends."},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the following financial data and propose an investment strategy based on the specified criteria:

Financial Data:
{t["financial_data"]}
Criteria: {t["criteria"]}

Ensure that your strategy is logical, based on the financial data, and aligns with the market trends. Provide your response in the following format:

Investment Strategy: [Your strategy here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The strategy should be logical and based on the provided financial data.",
            "The strategy should align with the specified market trends.",
            "The strategy should consider the company's financial health (e.g., net profit, assets, liabilities).",
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
