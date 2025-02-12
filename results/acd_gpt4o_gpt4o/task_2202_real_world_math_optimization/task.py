class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "You are organizing a charity event and need to allocate a budget of $10,000. The event includes food, entertainment, and venue rental. The goal is to maximize attendee satisfaction while staying within budget. Food costs $20 per person, entertainment costs a flat rate of $2,000, and venue rental costs $500 per hour. The event will last 5 hours. How will you allocate the budget to maximize attendee satisfaction?"},
            "2": {"scenario": "You are managing a factory that produces two types of products: A and B. Product A sells for $50 and Product B sells for $70. Each product A requires 2 hours of labor and 3 units of raw material, while each product B requires 3 hours of labor and 2 units of raw material. Your factory has a maximum of 100 hours of labor and 120 units of raw material available per week. How many of each product should you produce to maximize revenue?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to solve the following real-world problem by applying mathematical optimization techniques:

Scenario: {t['scenario']}

Provide a detailed explanation of your solution, including the mathematical principles and calculations used to arrive at your answer. Ensure that your solution addresses the problem statement clearly and is practical. Format your response as follows:

Solution: [Your detailed solution, including calculations and reasoning]

Make sure your response is at least 150 words long."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should provide a detailed and practical solution to the problem.", "The solution should include the mathematical principles and calculations used.", "The solution should address the problem statement and be at least 150 words long."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
