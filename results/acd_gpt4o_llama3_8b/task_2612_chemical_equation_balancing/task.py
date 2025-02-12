class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"equation": "H2 + O2 -> H2O"},
            "2": {"equation": "C3H8 + O2 -> CO2 + H2O"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Balance the following chemical equation. Ensure that the number of atoms for each element is the same on both sides of the equation. Submit your balanced equation in plain text format.

Equation: {t['equation']}

Example format of a balanced equation: '2H2 + O2 -> 2H2O'

Submit your response as a plain text string in the following format:

[Balanced Equation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The balanced equation must have the same number of atoms for each element on both sides.",
            "The equation should be chemically valid.",
            "The equation should be in its simplest form.",
            "The coefficients should be the smallest set of integers possible."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
