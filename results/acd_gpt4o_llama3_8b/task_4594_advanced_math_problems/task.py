class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {'problem': 'Compute the integral of the function f(x) = 3x^2 - 4x + 1 from x = 0 to x = 2.'},
            '2': {'problem': 'Find the eigenvalues and eigenvectors of the matrix A = [[2, 1], [1, 2]].'}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Solve the following mathematical problem: {t['problem']}\n\nSubmit your response as a plain text string containing:\nSolution: [Your solution]\nExplanation: [Your explanation]"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from sympy import integrate, symbols, Matrix, S
        x = symbols('x')
        if 'integral' in t['problem']:
            correct_solution = integrate(3*x**2 - 4*x + 1, (x, 0, 2))
            try:
                user_solution_str = submission.split('Solution:')[1].split('Explanation:')[0].strip()
                user_solution = S(user_solution_str)
                return 1.0 if user_solution == correct_solution else 0.0
            except Exception as e:
                return 0.0
        elif 'eigenvalues' in t['problem']:
            correct_matrix = Matrix([[2, 1], [1, 2]])
            correct_eigenvalues = correct_matrix.eigenvals()
            correct_eigenvectors = correct_matrix.eigenvects()
            try:
                user_solution_eigenvalues_str = submission.split('Eigenvalues:')[1].split('Eigenvectors:')[0].strip()
                user_solution_eigenvectors_str = submission.split('Eigenvectors:')[1].strip()
                user_solution_eigenvalues = {S(k): v for k, v in eval(user_solution_eigenvalues_str).items()}
                user_solution_eigenvectors = [(S(k), v[0], [S(vec) for vec in v[2]]) for k, v in eval(user_solution_eigenvectors_str)]
                return 1.0 if user_solution_eigenvalues == correct_eigenvalues and user_solution_eigenvectors == correct_eigenvectors else 0.0
            except Exception as e:
                return 0.0
        return 0.0
