class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "problem": "A company needs to allocate its budget across three projects (A, B, and C) to maximize profit. Each project requires a different investment and yields a different return on investment (ROI). The total budget is $100,000. Project A requires $30,000 and has an ROI of 20%, Project B requires $50,000 and has an ROI of 25%, and Project C requires $20,000 and has an ROI of 15%. Determine the optimal allocation of the budget to maximize the total profit.",
                "constraints": "The total budget cannot exceed $100,000."
            },
            "2": {
                "problem": "A transportation company needs to determine the optimal route for delivering goods from a warehouse to three different destinations (X, Y, and Z) to minimize transportation costs. The cost per mile to destination X is $10, to destination Y is $15, and to destination Z is $20. The distances are as follows: warehouse to X is 100 miles, warehouse to Y is 200 miles, and warehouse to Z is 150 miles. Determine the optimal route and the total cost.",
                "constraints": "Each destination must be visited exactly once."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        problem = t["problem"]
        constraints = t["constraints"]
        instructions = f"""Your task is to solve the following optimization problem:

Problem: {problem}

Constraints: {constraints}

Provide a detailed solution explaining the steps you took to find the optimal solution. Ensure that your solution adheres to the given constraints. Your solution should include the following:
1. A clear statement of the problem and constraints.
2. The mathematical formulation of the optimization problem.
3. The steps and calculations you took to solve the problem.
4. The final optimal solution with justification.

Provide your solution in the following format:

Solution:
[Your solution here]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The solution must adhere to the given constraints.",
            "The solution must provide a clear and logical explanation of the steps taken.",
            "The solution must include the mathematical formulation of the problem.",
            "The solution must correctly identify the optimal allocation or route.",
            "The solution must maximize profit or minimize cost as required by the problem.",
            "The solution must include calculations or logical steps to justify the answer."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
