class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "A factory produces three types of products: A, B, and C. The factory has a limited number of hours available for production each week (100 hours). Each product requires a different amount of time to produce: A takes 2 hours, B takes 3 hours, and C takes 5 hours. The profit for each product is different: A generates $50 profit, B generates $70 profit, and C generates $120 profit. In addition, at least 10 units of product A and 5 units of product B must be produced each week to meet contractual obligations. Develop a production plan that maximizes the factory's profit without exceeding the available production hours."
            },
            "2": {
                "scenario": "A delivery company needs to deliver packages to 10 different locations in a city. The company has 3 delivery trucks, each with a different capacity and speed. Truck 1 can carry 5 packages and travels at 40 km/h, Truck 2 can carry 3 packages and travels at 50 km/h, and Truck 3 can carry 2 packages and travels at 60 km/h. The goal is to minimize the total delivery time while ensuring all packages are delivered. Develop a delivery plan that minimizes the total delivery time, considering the capacities and speeds of the trucks."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Develop an optimization strategy for the following scenario:

Scenario: {t['scenario']}

Your strategy should clearly outline the steps and considerations involved in optimizing the process or system described. Provide a detailed explanation of your approach, including any mathematical calculations, assumptions, and reasoning behind your decisions. Ensure that your strategy is feasible and logically sound.

Your response should be structured as follows:
1. Introduction: [Brief overview of the problem and objectives]
2. Assumptions: [List any assumptions you are making]
3. Calculations: [Show all relevant calculations with clear steps]
4. Strategy: [Detailed explanation of the optimization strategy]
5. Conclusion: [Summary of your strategy and its expected outcomes]

Example Response:
Optimization Strategy:
1. Introduction: The goal is to maximize the factory's profit while adhering to the constraints of production hours and minimum production requirements.
2. Assumptions: Assume all products can be sold at the profit rates given.
3. Calculations: Calculate the maximum possible units of each product that can be produced within the 100-hour limit. For example, if producing only product A, the maximum is 50 units (100 hours / 2 hours per unit), which would yield a profit of $2500. Repeat similar calculations for combinations of products while ensuring contractual obligations are met.
4. Strategy: Based on the calculations, prioritize producing the most profitable combination of products while meeting the minimum production requirements. For example, produce 10 units of product A (20 hours), 5 units of product B (15 hours), and use the remaining 65 hours for product C, resulting in a specific number of units and total profit.
5. Conclusion: This strategy ensures maximum profit while staying within the production limits and meeting contractual obligations.

Submit your response as a plain text string in the following format:

Optimization Strategy: [Your strategy here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The strategy should clearly outline the steps and considerations involved in optimizing the process or system.",
            "The explanation should include detailed mathematical calculations, assumptions, and reasoning behind the decisions.",
            "The strategy should be feasible and logically sound.",
            "The strategy should aim to maximize profit (for Task 1) or minimize total delivery time (for Task 2) within the given constraints."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
