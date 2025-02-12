class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"premises": ["All humans are mortal.", "Socrates is a human."], "conclusion": "Socrates is mortal.", "is_valid": True},
            "2": {"premises": ["All birds can fly.", "Penguins are birds."], "conclusion": "Penguins can fly.", "is_valid": False}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "is_valid" in t:
            return f"""Your task is to evaluate the validity of the following argument based on the given premises. Provide your response as 'Valid' or 'Invalid'.

Premises: {', '.join(t['premises'])}
Conclusion: {t['conclusion']}

Response format: Valid/Invalid"""
        else:
            return f"""Your task is to generate a logically coherent argument based on the given premises. Ensure that your argument is logically valid and follows from the premises. Provide the conclusion of your argument in plain text format.

Premises: {', '.join(t['premises'])}

Response format: [Your conclusion]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "is_valid" in t:
            correct_response = "Valid" if t["is_valid"] else "Invalid"
            criteria = [f"The response should be '{correct_response}'."]
        else:
            criteria = ["The argument should be logically valid and coherent based on the given premises.", "The conclusion should logically follow from the premises."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
