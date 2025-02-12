class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "description": "You are planning a rectangular garden and have 40 meters of fencing material. You want to maximize the area of the garden. Create a mathematical model for this problem and solve it to find the dimensions of the garden that maximize the area.",
                "variables": ["length", "width"],
                "constraints": "2*length + 2*width = 40",
                "objective": "maximize length * width"
            },
            "2": {
                "description": "A company makes two types of products, A and B. The profit from product A is $3 per unit, and the profit from product B is $5 per unit. Each unit of product A requires 2 hours of labor, and product B requires 3 hours of labor. The company has a total of 60 hours of labor available per week. Create a mathematical model to maximize the profit and solve it to find how many units of each product should be produced.",
                "variables": ["A", "B"],
                "constraints": "2*A + 3*B <= 60",
                "objective": "maximize 3*A + 5*B"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""{t['description']}\n\nUse the given variables and constraints to create a mathematical model. Solve the model and provide the solution in terms of the variables with numerical values. Ensure that your solution adheres to the given constraints and achieves the specified objective.\n\nSubmit your solution as a plain text string in the following format:\n[length] = [value], [width] = [value] (for Task 1)\n[A] = [value], [B] = [value] (for Task 2)"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The solution should correctly solve the mathematical model based on the given constraints and objective."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
