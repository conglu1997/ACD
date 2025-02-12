class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task_type": "proof_construction", "premises": ["If P, then Q.", "P."], "conclusion": "Q.", "rules": "Use Modus Ponens to derive the conclusion from the premises."},
            "2": {"task_type": "proof_construction", "premises": ["If A, then B.", "If B, then C.", "A."], "conclusion": "C.", "rules": "Use hypothetical syllogism and modus ponens to derive the conclusion from the premises."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        premises = ' '.join(t['premises'])
        return f"Given the premises: {premises}, derive the conclusion: {t['conclusion']}. {t['rules']} Submit your proof in the following format: 1. [First step], 2. [Second step], ..., N. [Nth step].\nExample: 1. If P then Q (Premise), 2. P (Premise), 3. Q (Conclusion by Modus Ponens)"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The proof should correctly apply the specified logical rules.", "The proof should be logically sound and valid.", "The proof should lead to the correct conclusion."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
