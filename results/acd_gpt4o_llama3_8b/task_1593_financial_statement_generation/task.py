class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "financial_data": {
                    "revenue": 150000,
                    "cost_of_goods_sold": 90000,
                    "operating_expenses": 30000,
                    "taxes": 10000
                }
            },
            "2": {
                "financial_data": {
                    "revenue": 250000,
                    "cost_of_goods_sold": 120000,
                    "operating_expenses": 50000,
                    "taxes": 20000
                }
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a financial statement based on the given financial data. Ensure that your financial statement is coherent and follows standard accounting conventions. The financial statement should include sections for Revenue, Cost of Goods Sold, Gross Profit, Operating Expenses, Operating Income, Taxes, and Net Income. Calculate the values as follows:\n\nGross Profit = Revenue - Cost of Goods Sold\nOperating Income = Gross Profit - Operating Expenses\nNet Income = Operating Income - Taxes\n\nSubmit your financial statement as a plain text string in the following format:\n\nRevenue: [Revenue]\nCost of Goods Sold: [COGS]\nGross Profit: [Gross Profit]\nOperating Expenses: [Operating Expenses]\nOperating Income: [Operating Income]\nTaxes: [Taxes]\nNet Income: [Net Income]\n\nFinancial Data: {t['financial_data']}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The financial statement should be coherent and follow standard accounting conventions.",
            "The financial statement should accurately reflect the given financial data.",
            "The calculations for Gross Profit, Operating Income, and Net Income should be correct."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
