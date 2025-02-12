class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"statement": "Prove that the sum of the first n odd numbers is equal to n^2."},
            "2": {"statement": "Prove or disprove: For any natural number n, n^2 + n + 41 is a prime number."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Interpret the given mathematical statement and provide a valid proof or disproof:\n\nStatement: {t['statement']}\n\nYour response should include:\n1. A clear and logically coherent proof or disproof.\n2. Any necessary intermediate steps and explanations.\n3. Ensure the proof or disproof is complete and addresses all aspects of the statement.\n\nSubmit your response as a plain text string in the following format:\n\nProof/Disproof: [Your proof or disproof]\n\nExample Format:\nProof/Disproof: [Example proof or disproof, explaining each step clearly and coherently]"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The proof or disproof should be logically valid and coherent.", "The response should address all necessary intermediate steps and explanations.", "The proof or disproof should be complete and address all aspects of the statement."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
