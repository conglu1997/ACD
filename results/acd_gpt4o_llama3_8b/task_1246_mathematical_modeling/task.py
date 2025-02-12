class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "A farmer has a rectangular field with a length 3 times its width. The farmer wants to fence the field and also divide it into 3 equal rectangular sections using two dividers parallel to the width. Formulate a mathematical model to determine the total length of the fence required and solve it."},
            "2": {"prompt": "A company produces cylindrical cans and wants to minimize the cost of production. The cost is proportional to the surface area of the cans. Given that each can must have a volume of 1 liter, formulate a mathematical model to determine the dimensions (radius and height) that minimize the cost and solve it."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following task based on the given prompt:

{t['prompt']}

Formulate a mathematical model to solve the problem. Clearly define the variables, equations, and constraints. Then, solve the model to find the required values. Submit your response as a plain text string in the following format:

Model: [Your mathematical model here]
Solution: [Your solution here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []
        if "field" in t["prompt"]:
            criteria = ["The model should correctly define the variables and equations for the total length of the fence.", "The solution should correctly calculate the total length of the fence required, considering the given constraints."]
        else:
            criteria = ["The model should correctly define the variables and equations for the surface area and volume of the cylindrical can.", "The solution should correctly calculate the dimensions (radius and height) that minimize the surface area while maintaining the given volume."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
