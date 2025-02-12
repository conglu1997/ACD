class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"type": "creation", "constraints": "Include addition and subtraction within the context of a shopping scenario. Ensure the problem involves at least three mathematical operations."},
            "2": {"type": "solution", "prompt": "John has 5 apples. He buys 7 more apples and then gives away 3 apples. How many apples does John have now?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["type"] == "creation":
            constraints = t["constraints"]
            return f"""Create a mathematical word problem based on the following constraints: {constraints}. Ensure that the problem is coherent, logically consistent, and solvable with elementary arithmetic operations. Provide the word problem and its solution in a step-by-step manner in the following format:

Word Problem: [Your word problem]
Solution: [Step-by-step solution to your word problem]"""
        elif t["type"] == "solution":
            prompt = t["prompt"]
            return f"""Solve the following mathematical word problem. Provide a step-by-step explanation leading to the solution:
'{prompt}'

Solution: [Your step-by-step solution]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["type"] == "creation":
            criteria = [
                "The word problem should include addition and subtraction.",
                "The word problem should be based within the context of a shopping scenario.",
                "The problem should involve at least three mathematical operations.",
                "The solution should be provided in a step-by-step manner and correctly solve the word problem." 
            ]
        elif t["type"] == "solution":
            criteria = [
                "The solution should include a correct step-by-step explanation.",
                "The final answer must be correct."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
