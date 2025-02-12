class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Generate a non-trivial quadratic equation with integer coefficients and solve for its roots. Ensure that the roots are real numbers and the equation is not a perfect square."},
            "2": {"prompt": "Create a system of linear equations with two variables that has a unique solution. Ensure that the system is not trivial (e.g., not all coefficients are zero) and solve for the variables."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following task based on the prompt: '{t["prompt"]}'. Your response should include both the generated algebraic expression(s) and their solution(s). Ensure that the expressions are valid and the solutions are accurate. Submit your response in the following format:

Expression: [Your generated expression(s)]
Solution: [Your solution(s)]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The generated expression(s) should be valid and non-trivial.",
            "For the quadratic equation, ensure the roots are real and the equation is not a perfect square.",
            "For the system of linear equations, ensure it has a unique solution and is not trivial (e.g., not all coefficients are zero).",
            "The solution(s) should be accurate and match the generated expression(s)."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
