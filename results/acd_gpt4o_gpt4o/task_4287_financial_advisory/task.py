class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"type": "advice", "scenario": "A 30-year-old individual with a monthly income of $3000 wants to save for a house down payment of $60,000 in 5 years. Provide a detailed savings plan."},
            "2": {"type": "plan", "goal": "retirement savings", "details": {"age": 40, "current_savings": 50000, "monthly_contribution": 500, "retirement_age": 65, "desired_retirement_fund": 500000}}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["type"] == "advice":
            instructions = f"""Your task is to provide detailed financial advice based on the following scenario:

{t['scenario']}

Ensure your advice includes practical steps, detailed calculations, and any assumptions you make. Provide your response in the following format:

Financial Advice:
1. Steps: [List of practical steps]
2. Calculations: [Detailed calculations]
3. Assumptions: [Any assumptions made]

Provide your response in plain text format."""
        elif t["type"] == "plan":
            instructions = f"""Your task is to create a savings plan for the following goal:

Goal: {t['goal']}
Details: {t['details']}

Ensure your plan includes a monthly savings target, detailed calculations, and any assumptions you make. Provide your response in the following format:

Savings Plan:
1. Monthly Savings Target: [Amount]
2. Calculations: [Detailed calculations]
3. Assumptions: [Any assumptions made]

Provide your response in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["type"] == "advice":
            criteria = ["The advice should include practical steps.", "The calculations should be detailed and accurate.", "The assumptions should be clearly stated."]
        elif t["type"] == "plan":
            criteria = ["The plan should include a realistic monthly savings target.", "The calculations should be detailed and accurate.", "The assumptions should be clearly stated."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
