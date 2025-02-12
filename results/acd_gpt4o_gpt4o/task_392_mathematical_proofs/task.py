class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"statement": "Prove that the sum of two even numbers is always even."},
            "2": {"statement": "Prove that the square root of 2 is irrational."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        statement = t["statement"]
        instructions = f"""Your task is to construct a formal mathematical proof for the following statement:

Statement: {statement}

Ensure your proof is clear, logically structured, and follows the conventions of formal mathematical writing. Do not assume any unproven statements. Include all necessary steps and logical justifications. Provide your proof in plain text format.

Provide your response in the following format:

Proof:
[Your proof]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0
