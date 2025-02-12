class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"criteria": "Create a non-compete clause for an employment contract that is valid for 1 year and applies to the same industry.", "modification": "Modify the clause to extend the restriction period to 2 years and include a geographical restriction of 50 miles."},
            "2": {"criteria": "Create a confidentiality clause for a business partnership agreement that applies during the term of the agreement and for 2 years after its termination.", "modification": "Modify the clause to apply indefinitely and include a clause for breach of confidentiality."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a legal clause based on the given criteria and then modify it according to the specified changes.

Criteria: {t['criteria']}

After generating the legal clause, modify it as specified while adhering to the original constraints. Provide your response in plain text format with the following structure:

Original Clause:
[Your original clause here]

Modified Clause:
[Your modified clause here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The original clause should meet the given criteria.",
            "The modified clause should follow the specified changes and maintain the original constraints.",
            "Both clauses should be clear, coherent, and legally sound."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
