class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"proof": "Proof: Let x be an integer. If x is even, then x^2 is even. Proof: Suppose x is even. Then x = 2k for some integer k. Therefore, x^2 = (2k)^2 = 4k^2, which is even."},
            "2": {"proof": "Proof: Let a and b be real numbers. If a < b, then a^2 < b^2. Proof: Suppose a < b. Then a^2 < ab < b^2."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        proof = t["proof"]
        return f"""Verify the correctness of the given mathematical proof by identifying any logical errors or confirming its validity:

{proof}

Submit your evaluation as a plain text string in the following format:

Correct: [Yes/No]
Explanation: [Detailed explanation of any errors or confirmation of correctness]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The evaluation should correctly identify any logical errors or confirm the validity of the proof.",
            "The explanation should be detailed and logically sound."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
