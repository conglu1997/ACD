class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"statement": "Prove that the sum of the first n odd numbers is n^2.", "explanation": "Explain the concept of a derivative in calculus in simple terms."},
            "2": {"statement": "Prove that the square root of 2 is irrational.", "explanation": "Explain the concept of a limit in calculus in simple terms."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task involves two parts: generating a mathematical proof for a given statement and explaining a mathematical concept in simple terms.

1. Provide a detailed mathematical proof for the following statement:
Statement: {t['statement']}

2. Explain the following mathematical concept in simple terms:
Concept: {t['explanation']}

Ensure that your proof is logically sound and coherent. For the explanation, use clear and simple language that would be understandable to someone without advanced mathematical knowledge.

Provide your response in the following format:
Proof: [Your proof]
Explanation: [Your explanation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The proof should be logically sound and coherent.",
            "The explanation should be clear, simple, and accurate.",
            "The explanation should be understandable to someone without advanced mathematical knowledge."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
