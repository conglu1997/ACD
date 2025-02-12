class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {'equation': '2*x + 3 = 11', 'type': 'solve'},
            '2': {'equation': 'x**2 - 4*x + 4 = 0', 'type': 'solve'}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to solve the following algebraic equation: {t['equation']}. Provide a detailed step-by-step solution and the final value(s) of the variable(s)."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from sympy import sympify, Eq, solve
        from src.eval_helper import eval_with_llm_judge

        instructions = TaskFamily.get_instructions(t)
        criteria = ["The solution should include detailed steps and the correct final value(s) of the variable(s)."]

        # Validate the submission by solving the equation using sympy
        equation = t['equation']
        lhs, rhs = equation.split('=')
        lhs, rhs = sympify(lhs.strip()), sympify(rhs.strip())
        eq = Eq(lhs, rhs)
        correct_solution = solve(eq)

        # Check if the submission includes the correct solution and detailed steps
        if all(str(sol) in submission for sol in correct_solution):
            return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
        return 0.0
