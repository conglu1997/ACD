class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"premises": ["All humans are mortal.", "Socrates is a human.", "If Socrates is mortal, then he will die.", "If Socrates dies, then he no longer teaches."], "conclusion": "Socrates no longer teaches."},
            "2": {"premises": ["If it rains, the ground gets wet.", "If the ground is wet, the grass grows.", "If the grass grows, the cows will have food.", "It rains.", "If the cows have food, they produce milk."], "conclusion": "The cows produce milk."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        premises = " ".join(t["premises"])
        conclusion = t["conclusion"]
        return f"""Solve the following logical deduction puzzle based on the given premises: {premises} Your goal is to determine if the conclusion '{conclusion}' logically follows from the premises. Submit 'True' if the conclusion follows logically, and 'False' otherwise. Submit your answer as a single word: 'True' or 'False'. Ensure your reasoning follows the logical sequence presented in the premises."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should be either 'True' or 'False'.",
            "The response should correctly determine if the conclusion follows logically from the premises."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
