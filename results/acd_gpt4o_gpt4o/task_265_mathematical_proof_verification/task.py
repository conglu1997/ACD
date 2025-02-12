class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"proof": "Prove that the sum of any two even numbers is even.\n\nProof: Let the first even number be 2m and the second even number be 2n, where m and n are integers. The sum of these two numbers is 2m + 2n. Factoring out the 2, we get 2(m + n), which is clearly an even number since it is 2 times an integer. Therefore, the sum of any two even numbers is even."},
            "2": {"proof": "Prove that the square of any odd number is odd.\n\nProof: Let the odd number be represented as 2k + 1, where k is an integer. The square of this number is (2k + 1)^2. Expanding the square, we get 4k^2 + 4k + 1. Factoring out the 2 from the first two terms, we get 2(2k^2 + 2k) + 1, which is clearly an odd number since it is of the form 2 times an integer plus 1. Therefore, the square of any odd number is odd."},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to verify the correctness of the following mathematical proof:

{t["proof"]}

Make sure to carefully check each step of the proof for logical consistency and mathematical accuracy. Provide a clear statement on whether the proof is correct or incorrect, and justify your reasoning. Format your response as follows:

Correctness: [Correct/Incorrect]
Explanation: [Your detailed explanation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should clearly state whether the proof is correct or incorrect.",
            "The response should provide a detailed explanation of the reasoning.",
            "The response should identify any logical or mathematical errors if the proof is incorrect."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
