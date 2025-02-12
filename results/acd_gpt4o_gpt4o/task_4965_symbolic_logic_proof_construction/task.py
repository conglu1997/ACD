class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Prove the following statement using symbolic logic: (P → Q) ∧ (Q → R) ⊢ P → R"},
            "2": {"prompt": "Prove the following statement using symbolic logic: ¬(P ∧ Q) ⊢ ¬P ∨ ¬Q"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to construct a formal proof for the given logical statement using symbolic logic. Use standard logical symbols and notation (e.g., → for implication, ∧ for and, ∨ for or, ¬ for not). Ensure that your proof is valid, logically structured, and adheres to the rules of symbolic logic. Justify each step in your proof clearly. Provide your response in plain text format.\n\nStatement: {t['prompt']}\n\nStructure your response as follows:\n1. Introduction: [Your introduction]\n2. Proof: [Your step-by-step proof, with justifications]\n3. Conclusion: [Your conclusion]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The proof should be valid and logically structured.", "Each step in the proof should be clearly justified.", "The proof should adhere to the rules of symbolic logic."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
