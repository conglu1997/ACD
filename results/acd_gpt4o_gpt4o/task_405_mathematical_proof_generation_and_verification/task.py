class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theorem": "Prove that the product of two odd numbers is odd.", "verification": False},
            "2": {"proof": "Given a right triangle with legs of length a and b and hypotenuse of length c, by the Pythagorean theorem, we have a^2 + b^2 = c^2. Suppose a = 3 and b = 4, then c = 5. Therefore, a^2 + b^2 = 9 + 16 = 25 = c^2, verifying the theorem.", "verification": True}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['verification']:
            return f"""Your task is to verify the correctness of the following mathematical proof:

Proof: {t['proof']}

Provide a clear, step-by-step explanation of the rationale behind each step of the proof. Ensure your explanation is detailed and logically sound. Provide your response in plain text format."""
        else:
            return f"""Your task is to generate a mathematical proof for the following theorem:

Theorem: {t['theorem']}

Your proof should be rigorous, logically sound, and clearly structured. Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['verification']:
            criteria = ["The explanation should accurately verify the correctness of the given proof.", "The explanation should be detailed and logically sound."]
        else:
            criteria = ["The generated proof should be rigorous and logically sound.", "The proof should clearly demonstrate the theorem."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
