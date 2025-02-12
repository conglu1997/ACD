class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "A farmer wants to build a rectangular fence around his field to maximize the area. He has 100 meters of fencing material. What should be the dimensions of the rectangle to maximize the area? Provide your answer in the format: Length = X meters, Width = Y meters. Ensure that your solution includes the necessary mathematical calculations and reasoning needed to determine the dimensions."},
            "2": {"prompt": "A company produces two products, A and B. The profit from product A is $3 per unit, and the profit from product B is $5 per unit. The company can produce a maximum of 40 units of product A and 30 units of product B per day. Additionally, the total production capacity is limited to 50 units per day. How many units of each product should be produced to maximize profit? Provide your answer in the format: Product A = X units, Product B = Y units. Ensure that your solution includes the necessary mathematical calculations and reasoning needed to determine the optimal production quantities."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to solve the following practical problem using mathematical modeling. Ensure that your solution includes the necessary mathematical calculations and reasoning needed to determine the optimal solution:\n\n{t['prompt']}\n"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include the correct dimensions of the rectangle to maximize the area.",
            "The response should include the correct number of units of each product to maximize profit."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
