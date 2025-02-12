class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "Calculate the monthly payment for a car loan. The loan amount is $20,000, the annual interest rate is 5%, and the loan term is 5 years. Use the formula: M = P[r(1+r)^n]/[(1+r)^n-1], where M is the monthly payment, P is the loan amount, r is the monthly interest rate, and n is the number of payments. Note: Convert the annual interest rate to a monthly rate by dividing by 12. Example: For an annual rate of 5%, the monthly rate is 0.05/12."},
            "2": {"scenario": "Calculate the future value of an investment. The initial investment amount is $10,000, the annual interest rate is 6%, and the investment period is 10 years. Use the formula: FV = P(1 + r)^n, where FV is the future value, P is the initial investment, r is the annual interest rate, and n is the number of years. Ensure to compound the interest annually. Note: Use the exact formula without any shortcuts. Example: For an initial investment of $10,000 at 6% annual interest for 10 years, the calculation would be FV = 10000*(1 + 0.06)^10."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        scenario = t["scenario"]
        return f"""Solve the following financial calculation problem based on the given scenario:\n\n{scenario}\n\nSubmit your solution as a plain text string in the following format:\n\nSolution: [Your solution]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The solution should correctly apply the given formula to the scenario.", "The final answer should be accurate to two decimal places.", "All necessary conversions and steps should be explicitly shown in the solution."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
