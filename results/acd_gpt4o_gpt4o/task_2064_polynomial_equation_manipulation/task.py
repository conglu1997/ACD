class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"equation": "x**3 - 6*x**2 + 11*x - 6", "operation": "factorize"},
            "2": {"equation": "2*x**2 - 3*x + 1", "operation": "find_roots"},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to perform the following operation on the given polynomial equation:

Equation: {t['equation']}
Operation: {t['operation']}

For the operation 'factorize', you should provide the factorized form of the polynomial. For the operation 'find_roots', you should provide the roots of the polynomial.

Ensure your response is accurate and in plain text format.

Format your response as follows:

Result: [Your result]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from sympy import symbols, solve, factor
        x = symbols('x')
        equation = t['equation']
        operation = t['operation']

        try:
            if operation == 'factorize':
                correct_result = str(factor(eval(equation)))
            elif operation == 'find_roots':
                correct_result = str(solve(eval(equation), x))
            else:
                return 0.0
        except Exception as e:
            return 0.0

        # Normalize results for comparison
        correct_result = correct_result.replace(' ', '')
        submission_result = submission.strip().replace('Result:', '').replace(' ', '')

        return 1.0 if submission_result == correct_result else 0.0
