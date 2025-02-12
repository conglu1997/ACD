class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "Solve the following algebraic equation for x and show all your steps clearly, such as factoring, using the quadratic formula, or completing the square: 3x^2 - 12x + 9 = 0. Provide your answer in the following format: \nSteps: [Step-by-step solution] \nAnswer: [Final answer]"},
            "2": {"description": "Determine if the number 561 is a prime number or a composite number. If it is composite, provide its prime factorization and a brief justification explaining why it is composite, including the method used to determine its primality and the steps for the factorization. Provide your answer in the following format: \nPrime or Composite: [Answer] \nFactorization (if composite): [Prime factors] \nJustification: [Explanation]"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the following mathematical problem. Provide your answer in the specified format:

{t['description']}

Format: [Answer]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The answer should be in the correct format, accurate, and include all required steps or justifications."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
