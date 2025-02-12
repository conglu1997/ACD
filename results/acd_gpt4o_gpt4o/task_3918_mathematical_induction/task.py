class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "Prove the following statement using mathematical induction:", "statement": "For all natural numbers n, the sum of the first n odd numbers is n^2."},
            "2": {"description": "Verify the correctness of the given proof and identify any errors:", "proof": "Statement: For all natural numbers n, 2^n > n. Proof: Base case: For n = 1, 2^1 = 2 and 1 < 2, so the base case holds. Induction step: Assume that for some k ≥ 1, 2^k > k. Then for k + 1, 2^(k+1) = 2 * 2^k > 2 * k. Since 2 * k > k + 1 for all k ≥ 1, the statement holds for k + 1. By induction, the statement is true for all natural numbers n."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "statement" in t:
            instructions = f"""Your task is to prove the following statement using mathematical induction:

{t['statement']}

Provide your proof in plain text format, ensuring that each step is clear and logically follows from the previous step."""
        else:
            instructions = f"""Your task is to verify the correctness of the given proof and identify any errors:

{t['proof']}

Provide your verification in plain text format, clearly indicating any errors or confirming that the proof is correct."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "statement" in t:
            criteria = ["The proof should correctly use the principle of mathematical induction.", "Each step of the proof should be logically sound.", "The base case and induction step should be clearly identified."]
        else:
            criteria = ["The verification should correctly identify any errors in the proof or confirm its correctness.", "The reasoning should be clear and logically sound."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
