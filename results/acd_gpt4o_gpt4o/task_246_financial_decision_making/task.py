class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "You have $10,000 to invest. You are presented with three investment options: a high-risk stock with a potential return of 20% per year, a moderate-risk mutual fund with a potential return of 10% per year, and a low-risk savings account with a return of 2% per year. Analyze the risk and return of each option and decide how to allocate your $10,000.", "data": {"high_risk": {"return": 0.20, "risk": "high"}, "moderate_risk": {"return": 0.10, "risk": "moderate"}, "low_risk": {"return": 0.02, "risk": "low"}}},
            "2": {"scenario": "You are planning to buy a car and have two financing options: a loan with a fixed interest rate of 3% for 5 years, or a lease with monthly payments of $300 for 3 years. Analyze the total costs of each option and decide which is more financially advantageous.", "data": {"loan": {"interest_rate": 0.03, "term_years": 5}, "lease": {"monthly_payment": 300, "term_years": 3}}}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to analyze the following financial scenario and make a sound financial decision based on the given data:

Scenario: {t['scenario']}

Provide a detailed explanation of your decision, including the reasoning behind your choice and any calculations you performed. Ensure your decision is practical, financially sound, and well-justified. Your explanation should include the following elements:

1. Clear identification of the financial options.
2. Detailed calculations for each option.
3. Reasoning for your final decision.

Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The decision should be financially sound.", "The explanation should include reasoning and calculations.", "The decision should be practical."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
