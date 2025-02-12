class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem": "A triangle has sides of lengths 7 cm, 24 cm, and 25 cm. Calculate the area of the triangle."},
            "2": {"problem": "A circle has a radius of 10 cm. Calculate the circumference and the area of the circle."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the following geometry word problem. Provide your solution with clear explanations and calculations.

Problem: {t['problem']}

Your response should be in the following format:
Explanation: [Your explanation]
Calculations: [Step-by-step calculations]
Answer: [Final answer with units]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0
