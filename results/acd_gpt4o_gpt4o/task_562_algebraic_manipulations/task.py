class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "expression": "2x + 3x - 4 + x**2 - x**2 + 6"
            },
            "2": {
                "equation": "2*x**2 + 3*x - 5"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "expression" in t:
            return (
                "Your task is to simplify the following algebraic expression as much as possible: \n\n"
                "Expression: {expression}\n"
                "Provide your simplified expression in plain text format.").format(expression=t['expression'])
        elif "equation" in t:
            return (
                "Your task is to solve the following algebraic equation for x: \n\n"
                "Equation: {equation} = 0\n"
                "Provide your solution for x in plain text format. If there are multiple solutions, list all of them.").format(equation=t['equation'])
        return ""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from sympy import symbols, simplify, Eq, solve
        from src.eval_helper import eval_with_llm_judge

        x = symbols('x')
        instructions = TaskFamily.get_instructions(t)
        criteria = []

        if "expression" in t:
            try:
                simplified_expr = str(simplify(t['expression']))
                criteria.append(f"The simplified expression should be {simplified_expr}.")
            except Exception as e:
                return 0.0
        elif "equation" in t:
            try:
                equation = Eq(2*x**2 + 3*x - 5, 0)  # Directly constructing the equation using SymPy
                solution = solve(equation, x)
                criteria.append(f"The solution for the equation should be {solution}.")
            except Exception as e:
                return 0.0

        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
