class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "type": "contract clause",
                "requirements": "Include a non-disclosure agreement (NDA) clause for a software development contract, specifying the parties involved, the scope of confidentiality, and the duration of the agreement."
            },
            "2": {
                "type": "legal notice",
                "requirements": "Draft a legal notice to a tenant for non-payment of rent, specifying the amount due, the date by which payment must be made, and potential legal actions if the payment is not received."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a {t['type']} based on the following requirements: {t['requirements']}.

Ensure that the document follows legal standards, is precise in language, and adheres to the specified requirements. The document should be clear, professionally formatted, and legally coherent. Submit your document as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The document should follow legal standards.",
            "The document should be precise in language.",
            "The document should adhere to the specified requirements.",
            "The document should be clear, professionally formatted, and legally coherent."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
