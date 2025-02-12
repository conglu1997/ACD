class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task_type": "solve", "problem": "Prove that the sum of the squares of any two sides of a right triangle is equal to the square of the hypotenuse."},
            "2": {"task_type": "solve", "problem": "Solve the integral of x^2 * e^(x^3) dx."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to solve the following mathematical problem and provide a detailed explanation of your solution process:\n\nProblem: {t['problem']}\n\nEnsure that your solution is correct and your explanation is clear and thorough. Provide your response in plain text format. Your response should include the following elements:\n1. The final solution.\n2. A step-by-step explanation of how you arrived at the solution.\n3. Any relevant mathematical principles or theorems used in your solution."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The solution must be correct.", "The explanation must be clear and thorough.", "All relevant mathematical principles or theorems must be correctly applied."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
