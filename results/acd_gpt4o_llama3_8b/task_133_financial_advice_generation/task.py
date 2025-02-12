class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "A 30-year-old individual with a stable job wants to save for a down payment on a house in 5 years. They currently have $10,000 in savings and can save $1,000 per month. Provide a financial plan including savings strategies, potential investment options, and any other advice to help them reach their goal.",
            },
            "2": {
                "scenario": "A recent college graduate has $50,000 in student loan debt and just started a job with a $40,000 annual salary. They want to pay off their debt as quickly as possible while also saving for emergencies. Provide a financial plan including a budget, debt repayment strategy, and savings tips.",
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Provide a detailed financial plan for the following scenario:

{t['scenario']}

Your financial plan should include the following sections:
1. Budget: Outline a monthly budget considering the individual's income and expenses.
2. Savings Plan: Describe strategies for saving money, including any relevant savings accounts or tools.
3. Investment Options: Suggest potential investment options that align with the individual's goals and risk tolerance.
4. Debt Management (if applicable): Provide a strategy for managing and paying off any existing debts.
5. Additional Advice: Offer any other relevant financial advice that could help the individual achieve their goal.

Ensure the financial plan is clear, logical, and feasible. Provide enough detail in each section to demonstrate a thorough understanding of financial planning. Include detailed steps and calculations where applicable. Each section should be clearly labeled and well-organized.

Example response format:

Budget:
- Income: $4,000 per month
- Expenses: $2,500 per month (rent, utilities, food, transportation, etc.)
- Savings: $1,000 per month
- Discretionary: $500 per month

Savings Plan:
- Open a high-yield savings account
- Automate monthly transfers of $1,000 to the savings account

Investment Options:
- Consider low-risk investments such as index funds or bonds
- Allocate 20% of savings to a diversified investment portfolio

Debt Management (if applicable):
- Focus on paying off high-interest debt first
- Allocate $200 per month towards student loan repayment

Additional Advice:
- Review and adjust the budget periodically
- Consider consulting with a financial advisor for personalized advice

Ensure the response is detailed and follows this structure."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The budget should be realistic and based on the given income and expenses.",
            "The savings plan should include specific strategies and tools.",
            "Investment options should be appropriate for the individual's goals and risk tolerance.",
            "Debt management strategies (if applicable) should be practical and effective.",
            "Additional advice should be relevant and helpful for achieving the goal.",
            "Each section should be clearly labeled and well-organized."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
