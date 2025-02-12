class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "theorem": "Prove that the sum of the first n natural numbers is (n*(n+1))/2.",
                "hint": "Consider using mathematical induction." 
            },
            "2": {
                "proof": "Given: \nTheorem: The sum of the first n odd numbers is n^2.\nProof: We prove this by induction.\nBase Case: For n=1, the sum of the first odd number is 1, which is 1^2. Hence, the base case holds.\nInduction Hypothesis: Assume the statement holds for some k, i.e., the sum of the first k odd numbers is k^2.\nInduction Step: Consider the (k+1)th odd number, which is 2(k+1)-1. Adding this to the sum of the first k odd numbers, we get k^2 + 2(k+1) - 1 = k^2 + 2k + 1 = (k+1)^2. Hence, the statement holds for k+1.\nThus, by induction, the theorem is proved.",
                "correctness": "True"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "theorem" in t:
            return f"""Generate a proof for the following theorem:

Theorem: {t['theorem']}
Hint: {t['hint']}

Ensure your proof is clear, logically structured, and mathematically sound. Submit your proof as a plain text string."""
        else:
            return f"""Verify the correctness of the following proof:

Proof: {t['proof']}

Determine whether the proof is correct or incorrect. If incorrect, briefly explain why. Submit your answer as 'Correct' or 'Incorrect' followed by a brief explanation if applicable. For example: 'Incorrect: The induction step is flawed because...'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "theorem" in t:
            validation_criteria = [
                "The proof should be clear, logically structured, and mathematically sound."
            ]
        else:
            correct_answer = "Correct" if t['correctness'] == "True" else "Incorrect"
            validation_criteria = [
                f"The response should be '{correct_answer}' if the proof is correct, otherwise provide a brief explanation of the error."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
