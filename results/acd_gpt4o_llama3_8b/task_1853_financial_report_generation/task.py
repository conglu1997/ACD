class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "financial_data": {
                    "revenue": 500000,
                    "expenses": 300000,
                    "net_income": 200000,
                    "assets": 1000000,
                    "liabilities": 400000,
                    "equity": 600000
                },
                "business_context": "ABC Corp is a mid-sized manufacturing company specializing in consumer electronics. The company has seen a steady growth in revenue over the past year, but also an increase in operational costs."
            },
            "2": {
                "financial_data": {
                    "revenue": 750000,
                    "expenses": 450000,
                    "net_income": 300000,
                    "assets": 1500000,
                    "liabilities": 500000,
                    "equity": 1000000
                },
                "business_context": "XYZ Ltd is a software development firm that has recently launched a new product line. The company has invested heavily in research and development, resulting in increased expenses but also significant revenue growth."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        financial_data = t['financial_data']
        business_context = t['business_context']
        return f"""Generate a financial report based on the following financial data and business context:

Financial Data:
- Revenue: ${financial_data['revenue']}
- Expenses: ${financial_data['expenses']}
- Net Income: ${financial_data['net_income']}
- Assets: ${financial_data['assets']}
- Liabilities: ${financial_data['liabilities']}
- Equity: ${financial_data['equity']}

Business Context:
{business_context}

Your financial report should include the following sections:
1. Executive Summary
2. Financial Analysis (including key metrics and ratios)
3. Business Context and Implications
4. Conclusion and Recommendations

Ensure that your report is structured, coherent, and accurately interprets the given data and context. Submit your report as a plain text string formatted with section headers."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The report should be structured with the specified sections.",
            "The financial analysis should include key metrics and ratios.",
            "The report should accurately interpret the given financial data and business context.",
            "The report should be coherent and well-written."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
