class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "premises": ["All humans are mortal.", "Socrates is a philosopher."],
                "conclusion": "Socrates is mortal."
            },
            "2": {
                "premises": ["If it rains, the ground will be wet.", "The ground is wet."],
                "conclusion": "It has rained."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Construct a logical argument based on the given premises and conclusion. Ensure that your argument is coherent and logically valid. Also, provide a detailed analysis explaining why the argument is valid or invalid and any assumptions made.

Premises: {', '.join(t['premises'])}
Conclusion: {t['conclusion']}

Submit your response as a plain text string in the following format:
Argument: [Your logical argument]
Analysis: [Your detailed analysis]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = ["The argument should be logically valid based on the given premises.", "The analysis should explain why the argument is valid or invalid and mention any assumptions made."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
