class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"premises": ["If it rains, the ground will be wet.", "If the ground is wet, the flowers will bloom.", "It is raining."], "conclusion": "The flowers will bloom."},
            "2": {"premises": ["All humans are mortal.", "All Greeks are humans.", "Socrates is a Greek."], "conclusion": "Socrates is mortal."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to construct a logical proof based on the following premises and conclusion. Your proof should use formal logical steps and demonstrate a clear understanding of logical reasoning. Ensure that your proof is valid and sound.

Premises:
1. {t['premises'][0]}
2. {t['premises'][1]}
3. {t['premises'][2] if len(t['premises']) > 2 else ''}

Conclusion: {t['conclusion']}

Provide your proof in plain text format, clearly indicating each logical step."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The proof should be valid and sound.",
            "The proof should use formal logical steps.",
            "The proof should demonstrate a clear understanding of logical reasoning."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
