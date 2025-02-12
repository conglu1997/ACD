class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "theorem": "Prove that the sum of the interior angles of a triangle is 180 degrees."
            },
            "2": {
                "problem": "Prove that in a right-angled triangle, the square of the hypotenuse is equal to the sum of the squares of the other two sides (Pythagorean theorem)."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'theorem' in t:
            return f"""Generate a geometric proof for the following theorem:

Theorem: {t['theorem']}

Ensure that the proof is logically coherent, uses appropriate geometric principles, and follows a structured format. Your proof should include:
1. A clear statement of what is to be proved.
2. A list of given information and any assumptions.
3. Step-by-step logical reasoning and justification for each step.
4. A conclusion that clearly follows from the previous steps.

Submit your proof as a plain text string."""
        elif 'problem' in t:
            return f"""Generate a geometric proof for the following problem statement:

Problem: {t['problem']}

Ensure that the proof is logically coherent, uses appropriate geometric principles, and follows a structured format. Your proof should include:
1. A clear statement of what is to be proved.
2. A list of given information and any assumptions.
3. Step-by-step logical reasoning and justification for each step.
4. A conclusion that clearly follows from the previous steps.

Submit your proof as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The proof should be logically coherent.",
            "The proof should use appropriate geometric principles.",
            "The proof should be presented in a clear and structured format.",
            "The proof should include step-by-step reasoning and justification for each step.",
            "The proof should include a clear conclusion that follows logically from the steps."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
