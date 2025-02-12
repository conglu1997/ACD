class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem": "You are given a circuit with a 9-volt battery, a 100-ohm resistor, and a light bulb in series. Calculate the current flowing through the circuit and explain the steps involved."},
            "2": {"problem": "A 2-kilogram object is dropped from a height of 10 meters. Calculate the velocity of the object just before it hits the ground and explain the principles involved."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        problem = t["problem"]
        instructions = f"""Your task is to solve the following scientific problem and explain the underlying principles:

{problem}

Ensure your response is accurate, detailed, and clearly explains the steps and principles involved in solving the problem. Provide your response in plain text format with the following structure:

1. Solution: [Your solution]
2. Explanation: [Detailed explanation of the principles and steps involved]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The solution should accurately solve the problem.",
            "The explanation should be clear and include the scientific principles involved."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
