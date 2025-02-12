class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "expression": "3x^2 - 5x + 2 = 0"
            },
            "2": {
                "expression": "2a^4 - 4a^3 + 6a^2 - 8a + 10 = 0"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Solve the following algebraic equation for its roots. Show all steps involved in solving the equation, including any factorization and use of the quadratic formula or other relevant methods. Submit your response as a plain text string in the following format:\n\nEquation: {t['expression']}\nSolution: [Provide your detailed solution here]"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The solution should include all steps involved in solving the equation.",
            "Any factorization or use of the quadratic formula or other relevant methods should be clearly shown.",
            "The final roots of the equation should be correct and clearly stated."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
