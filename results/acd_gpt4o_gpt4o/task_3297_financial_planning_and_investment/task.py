class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"parameters": {"income": 5000, "expenses": 3000, "savings": 10000, "investment_options": ["stocks", "bonds", "real estate", "mutual funds", "cryptocurrency"], "financial_goals": ["buy a house in 5 years", "retirement in 30 years", "children's college fund in 15 years"]}, "description": "Create a financial plan based on the provided parameters."},
            "2": {"strategy": "The individual has invested 50% in stocks, 20% in bonds, 10% in real estate, 10% in mutual funds, and 10% in cryptocurrency. The stocks have a high risk but high return, bonds have low risk but low return, real estate has moderate risk and return, mutual funds have moderate risk and return, and cryptocurrency has very high risk and high return. The individual aims to buy a house in 5 years, save for their children's college fund in 15 years, and retire in 30 years.", "description": "Evaluate the given investment strategy to determine if it aligns with the individual's financial goals."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'parameters' in t:
            return f"""Your task is to create a financial plan based on the provided parameters.

Parameters:
Income: ${t['parameters']['income']} per month
Expenses: ${t['parameters']['expenses']} per month
Savings: ${t['parameters']['savings']}
Investment Options: {', '.join(t['parameters']['investment_options'])}
Financial Goals: {', '.join(t['parameters']['financial_goals'])}

Ensure your financial plan includes:
1. A budget plan considering the income and expenses.
2. A savings strategy.
3. An investment strategy using the given options.
4. A plan to achieve the financial goals.

Provide your financial plan in plain text format.

Example response format:
Budget Plan: [Your budget plan here]
Savings Strategy: [Your savings strategy here]
Investment Strategy: [Your investment strategy here]
Goals Plan: [Your plan to achieve the financial goals here]
"""
        else:
            return f"""Your task is to evaluate the given investment strategy to determine if it aligns with the individual's financial goals.

Investment Strategy: {t['strategy']}

Ensure your evaluation includes:
1. Analysis of the risk and return of each investment option.
2. Assessment of the strategy's alignment with the financial goals.
3. Suggestions for improvement if necessary.

Provide your evaluation in plain text format.

Example response format:
Risk and Return Analysis: [Your analysis here]
Strategy Assessment: [Your assessment here]
Suggestions for Improvement: [Your suggestions here]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = None
        if 'parameters' in t:
            criteria = ["The budget plan should consider the given income and expenses.", "The savings strategy should be clear and feasible.", "The investment strategy should use the given options.", "The plan should aim to achieve the financial goals."]
        else:
            criteria = ["The evaluation should analyze the risk and return of each investment option.", "The assessment should determine if the strategy aligns with the financial goals.", "Suggestions for improvement should be relevant and practical."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
