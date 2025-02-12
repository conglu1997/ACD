from sympy import symbols, Function, Eq, dsolve, integrate

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "problem": "Solve the following differential equation: dy/dx = 3x^2 + 2x - 1, with the initial condition y(0) = 4."
            },
            "2": {
                "problem": "Calculate the definite integral of the function f(x) = 2x^3 - 3x^2 + x - 5 over the interval [1, 3]."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        problem = t["problem"]
        return f"Your task is to solve the following advanced calculus problem. Provide your solution in a clear and concise manner, showing all necessary steps and justifications. Here is the problem:\n\n{problem}\n\nEnsure your solution is accurate and complete. Provide your solution in plain text format."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge

        problem = t["problem"]
        instructions = TaskFamily.get_instructions(t)

        if "differential equation" in problem:
            x = symbols('x')
            y = Function('y')(x)
            differential_eq = Eq(y.diff(x), 3*x**2 + 2*x - 1)
            particular_solution = dsolve(differential_eq, ics={y.subs(x, 0): 4})
            criteria = [f"The solution should be y = {particular_solution.rhs}."]
        else:
            x = symbols('x')
            function = 2*x**3 - 3*x**2 + x - 5
            definite_integral = integrate(function, (x, 1, 3))
            criteria = [f"The solution should be {definite_integral}."]

        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
