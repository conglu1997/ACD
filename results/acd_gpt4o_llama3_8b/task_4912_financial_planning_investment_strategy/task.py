class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "You are given a starting capital of $50,000. Your goal is to grow this capital to $100,000 in 5 years. Devise a financial plan and investment strategy to achieve this goal. Consider the following constraints: 1) You can invest in stocks, bonds, and mutual funds. 2) You should maintain a diversified portfolio. 3) You can rebalance your portfolio annually. Provide a detailed plan including the types of investments, percentage allocations, and expected returns.",
                "criteria": "The plan should include a diversified portfolio with detailed percentage allocations and expected returns for each type of investment. It should also include an annual rebalancing strategy. The plan should be realistic and achievable within the given timeframe."
            },
            "2": {
                "prompt": "You are planning for retirement and have a current savings of $200,000. You want to retire in 20 years with a retirement fund of $1,000,000. Devise a financial plan and investment strategy to achieve this goal. Consider the following constraints: 1) You can invest in real estate, stocks, and bonds. 2) You should consider inflation and market risks. 3) You can adjust your investments every 5 years. Provide a detailed plan including the types of investments, percentage allocations, and expected returns.",
                "criteria": "The plan should consider inflation and market risks, include a diversified portfolio with detailed percentage allocations and expected returns for each type of investment, and outline adjustments every 5 years. The plan should be realistic and achievable within the given timeframe."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are tasked with devising a financial plan and investment strategy based on the given prompt. Your plan should be coherent, logically structured, and explore the given criteria in depth.

Prompt: {t['prompt']}

Submit your response in the following format:
Financial Plan: [Your detailed financial plan and investment strategy]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            t['criteria']
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
