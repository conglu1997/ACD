class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"requirement": "Generate a non-compete clause for an employment contract that restricts the employee from working with competitors for 1 year within a 50-mile radius."},
            "2": {"legal_text": "In the event of a breach of this contract, the breaching party shall be liable for liquidated damages in the amount of $10,000. Furthermore, this contract shall be governed by the laws of the State of California. Additionally, any disputes arising out of or related to this contract shall be resolved through binding arbitration in the State of California.", "question": "What are the consequences of breaching the contract?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "requirement" in t:
            return f"""Generate a legal clause based on the following requirement: {t['requirement']}. Ensure the clause is legally sound, clear, and adheres to standard legal drafting conventions. The clause should be precise and cover all necessary aspects of a non-compete agreement. Submit your clause as a plain text string."""
        else:
            return f"""Interpret the following legal text and answer the accompanying question:

Legal Text: {t['legal_text']}

Question: {t['question']}

Ensure your answer is precise, based on the given legal text, and clearly addresses the question. Submit your answer as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "requirement" in t:
            criteria = ["The clause should be legally sound and adhere to the given requirement.", "The clause should be precise and cover all necessary aspects of a non-compete agreement."]
        else:
            criteria = ["The answer should be precise and based on the provided legal text.", "The answer should clearly address the question of the consequences of breaching the contract."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
