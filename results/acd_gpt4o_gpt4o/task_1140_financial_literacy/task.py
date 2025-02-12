class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"financial_statement": "Revenue: $120,000\nExpenses: $80,000\nNet Income: $40,000\nAssets: $150,000\nLiabilities: $50,000", "question": "What is the equity of the company?"},
            "2": {"financial_statement": "Savings: $10,000\nMonthly Income: $4,000\nMonthly Expenses: $3,500\nGoal: Save $5,000 in 6 months", "question": "Is it feasible to save $5,000 in 6 months with the given financial data? Explain your reasoning."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to interpret the provided financial statement and answer the question based on the data.

Financial Statement:
{t['financial_statement']}

Question: {t['question']}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['question'] == "What is the equity of the company?":
            criteria = ["The response should correctly calculate the equity as Assets minus Liabilities."]
        elif t['question'] == "Is it feasible to save $5,000 in 6 months with the given financial data? Explain your reasoning.":
            criteria = ["The response should correctly analyze the monthly savings potential and determine feasibility based on the given data."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
