class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem": "Solve the following system of equations:\n\n3x + 4y = 10\n2x - y = 1\n\nProvide the values of x and y."},
            "2": {"problem": "Calculate the area of a triangle with sides of lengths 7, 8, and 9 using Heron's formula. Provide the area rounded to two decimal places."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        problem = t["problem"]
        return f"""Solve the following mathematical problem:\n\n{problem}\n\nEnsure your solution is clear, accurate, and shows all necessary steps. Submit your solution as a plain text string in the following format:\n\nSolution: [Your Solution Here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []
        if t["problem"].startswith("Solve the following system of equations"):
            criteria = ["The solution should correctly include the values of x and y.", "All steps to reach the solution should be shown clearly."]
        elif t["problem"].startswith("Calculate the area of a triangle"):
            criteria = ["The solution should correctly include the area rounded to two decimal places.", "All steps to reach the solution should be shown clearly."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
