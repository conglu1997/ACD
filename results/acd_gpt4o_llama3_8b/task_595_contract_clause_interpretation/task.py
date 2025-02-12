class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "clause": "The contractor shall complete the work within 90 days of the commencement date. In the event of delay due to unforeseen circumstances, the contractor must notify the client in writing within 5 days of the delay, and the completion date shall be extended by a reasonable period mutually agreed upon by both parties.",
                "instructions": "Interpret the provided contract clause. Explain the obligations of the contractor and the conditions under which the completion date can be extended. Submit your response as a plain text string."
            },
            "2": {
                "clause": "The tenant shall be responsible for all routine maintenance and repairs of the premises, excluding structural repairs. In the event of structural damage, the landlord shall be notified immediately and shall commence repairs within 30 days of receiving notice.",
                "instructions": "Interpret the provided contract clause. Explain the responsibilities of the tenant and the landlord regarding maintenance and repairs. Submit your response as a plain text string."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Interpret the following contract clause: {t["clause"]}. Explain the obligations and responsibilities specified in the clause. Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The response should accurately interpret the provided contract clause.",
            "The response should clearly explain the obligations and responsibilities specified in the clause."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
