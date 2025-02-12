class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"statement": "If P implies Q and Q implies R, then P implies R.", "instruction": "Prove the given logical statement using formal logic."},
            "2": {"statement": "Prove that the sum of the first n natural numbers is (n*(n+1))/2.", "instruction": "Provide a formal proof for the given mathematical statement."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to provide a formal proof for the following statement:

Statement: {t['statement']}

{t['instruction']}

Ensure that your proof is logically sound, clearly structured, and follows formal proof techniques. Provide your proof in plain text format. Your proof should be structured as follows:
1. State the given statement clearly.
2. Provide the logical steps or mathematical derivations leading to the conclusion.
3. Conclude with a summary of the proof.

Example format:
Statement: If P implies Q and Q implies R, then P implies R.
Proof:
1. Assume P is true.
2. Since P implies Q, Q must also be true.
3. Since Q implies R, R must also be true.
4. Therefore, if P implies Q and Q implies R, then P implies R."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The proof should be logically sound and correctly structured.",
            "The proof should follow formal proof techniques.",
            "The proof should include all necessary logical steps or mathematical derivations."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
