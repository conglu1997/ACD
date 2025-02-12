class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"statement": "Prove that the sum of the cubes of the first n natural numbers is (n(n+1)/2)^2."},
            "2": {"proof": "To prove that the sum of the cubes of the first n natural numbers is (n(n+1)/2)^2, we use mathematical induction. Base case (n=1): 1^3 = (1(1+1)/2)^2 = 1. Inductive step: Assume the formula holds for n=k. For n=k+1, we have S = 1^3 + 2^3 + ... + k^3 + (k+1)^3. By the inductive hypothesis, S = (k(k+1)/2)^2 + (k+1)^3. Simplifying this, we get ((k+1)(k/2 + 1/2))^2, which completes the induction step and proves the formula."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'statement' in t:
            return f"""Your task is to generate a mathematical proof for the following statement:

Statement: {t['statement']}

Ensure that your proof is clear, logically coherent, and includes all necessary steps. Provide your proof in plain text format without additional formatting."""
        else:
            return f"""Your task is to understand and explain the following mathematical proof:

Proof: {t['proof']}

Provide a detailed explanation that clarifies each step of the proof, ensuring that your explanation is coherent and logically sound. Provide your explanation in plain text format without additional formatting."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'statement' in t:
            criteria = ["The proof should be clear.", "The proof should be logically coherent.", "The proof should include all necessary steps.", "The proof should demonstrate understanding of mathematical induction.", "The proof should correctly simplify algebraic expressions."]
        else:
            criteria = ["The explanation should be detailed.", "The explanation should clarify each step of the proof.", "The explanation should be coherent and logically sound.", "The explanation should demonstrate understanding of mathematical induction.", "The explanation should correctly interpret algebraic expressions."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
