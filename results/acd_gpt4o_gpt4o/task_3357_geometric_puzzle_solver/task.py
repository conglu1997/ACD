class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task_type": "triangle_puzzle", "description": "Given a right-angled triangle with sides a, b, and hypotenuse c, find the length of the hypotenuse c if a = 3 units and b = 4 units."},
            "2": {"task_type": "square_puzzle", "description": "If a square has a diagonal of length 10 units, find the length of one side of the square."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to solve the following geometric puzzle:

{t['description']}

Provide your solution in plain text format, showing all necessary steps and calculations. Format your response as follows:

Solution: [Your solution here]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['task_type'] == 'triangle_puzzle':
            criteria = ["The solution should correctly apply the Pythagorean theorem.", "The hypotenuse should be calculated correctly."]
        else:
            criteria = ["The solution should correctly apply the properties of a square.", "The side length should be calculated correctly."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
