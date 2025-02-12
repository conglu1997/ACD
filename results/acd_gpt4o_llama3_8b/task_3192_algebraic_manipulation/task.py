class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "equation": "4(x - 2) + 3 = 3x + 5"
            },
            "2": {
                "inequality": "5(2x - 3) <= 4x + 7"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'equation' in t:
            return f"Solve the following algebraic equation and provide the value of the variable as your answer:\n\nEquation: {t['equation']}\n\nSubmit your answer as a plain text string in the format: 'Answer: [Your answer]'."
        elif 'inequality' in t:
            return f"Solve the following algebraic inequality and provide the range of values for the variable that satisfy the inequality:\n\nInequality: {t['inequality']}\n\nSubmit your answer as a plain text string in the format: 'Answer: [Your answer]'."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'equation' in t:
            criteria = ["The answer should be the correct value of the variable that satisfies the equation."]
        elif 'inequality' in t:
            criteria = ["The answer should be the correct range of values for the variable that satisfy the inequality."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
