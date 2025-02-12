class TaskFamily:
    import random

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem": "Prove that the sum of the squares of any two sides of a right triangle is equal to the square of the hypotenuse.", "type": "proof"},
            "2": {"problem": "Find the derivative of the function f(x) = x^3 - 3x^2 + 5x - 7 and provide a detailed explanation of each step.", "type": "solution"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["type"] == "proof":
            return f"""Provide a detailed proof for the following mathematical statement:

Problem: {t["problem"]}

Your proof should include all necessary steps, logical reasoning, and any relevant theorems or lemmas. Submit your proof as a plain text string in the following format:

Proof: [Your detailed proof]"""
        else:
            return f"""Solve the following mathematical problem and provide a detailed explanation of each step:

Problem: {t["problem"]}

Your solution should include all necessary steps, intermediate calculations, and final answer. Submit your solution as a plain text string in the following format:

Solution: [Your detailed solution]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = None
        if t["type"] == "proof":
            criteria = [
                "The proof should include all necessary steps.",
                "The logical reasoning should be sound.",
                "Any relevant theorems or lemmas should be correctly applied.",
                "The final conclusion should directly follow from the steps provided.",
                "The proof should be clearly and coherently presented."
            ]
        else:
            criteria = [
                "The solution should include all necessary steps.",
                "Intermediate calculations should be shown.",
                "The final answer should be correct and clearly stated.",
                "The reasoning behind each step should be explained.",
                "The solution should be clearly and coherently presented."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
