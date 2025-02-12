class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "task": "generate_equation",
                "constraints": "Create an algebraic equation with two variables that includes a quadratic term and can be solved for both variables."
            },
            "2": {
                "task": "solve_equation",
                "equation": "x^2 + y = 10, x + y = 4"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task'] == 'generate_equation':
            return f"Generate an algebraic equation based on the following constraints: {t['constraints']} Ensure the equation includes a quadratic term and is solvable for both variables. Submit your equation as a plain text string in the following format: 'Equation: [Your equation]'."
        elif t['task'] == 'solve_equation':
            return f"Solve the following algebraic equations: {t['equation']} Provide the values of the variables as a plain text string in the format: 'Solution: x = [value], y = [value]'."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['task'] == 'generate_equation':
            validation_criteria = [
                "The equation should involve two variables.",
                "The equation should include a quadratic term.",
                "The equation should be solvable for both variables.",
                "The equation should be in the correct format: 'Equation: [Your equation]'."
            ]
        elif t['task'] == 'solve_equation':
            validation_criteria = [
                "The solution should be correct.",
                "The solution should be concise and clearly stated.",
                "The solution should be in the correct format: 'Solution: x = [value], y = [value]'."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
