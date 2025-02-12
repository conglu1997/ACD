class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"expression": "(2*x + 3)*(x - 4)"},
            "2": {"expression": "(a + b)**2 - (a - b)**2"},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Simplify the following algebraic expression: {t["expression"]}. Provide your answer as a plain text string in its simplest form, without any spaces."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from sympy import simplify
        from sympy.abc import x, a, b

        expected = str(simplify(t["expression"])).replace(' ', '')
        return 1.0 if submission.replace(' ', '') == expected else 0.0
