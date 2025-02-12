class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "math_concept": "addition and subtraction",
                "context": "a treasure hunt"
            },
            "2": {
                "math_concept": "multiplication and division",
                "context": "a space adventure"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate an engaging mathematical word problem based on the given mathematical concept and context:

Mathematical Concept: {t['math_concept']}
Context: {t['context']}

Ensure the word problem is clear, engaging, and appropriate for a middle school audience. The problem should require the use of the given mathematical concept to solve and should involve multiple steps. Submit your word problem as a plain text string in the following format:

Problem: [Your word problem]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The word problem should be clear and engaging.",
            "The word problem should be appropriate for a middle school audience.",
            "The word problem should require the use of the given mathematical concept to solve.",
            "The word problem should involve multiple steps.",
            "The word problem should be in the format: Problem: [Your word problem]."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
