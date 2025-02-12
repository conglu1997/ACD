class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "A customer is calling to complain about a defective product they received. The product is a smartphone that keeps shutting down unexpectedly. The customer is frustrated and wants a solution. Additionally, they mention that they have already tried contacting support before but did not receive a satisfactory response."},
            "2": {"scenario": "A customer is seeking assistance with a billing issue. They were charged twice for the same service and are anxious about getting their money back. The customer mentions that they have recently moved to a new address and are worried that this might complicate the refund process."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        scenario = t["scenario"]
        instructions = f"""Your task is to simulate a customer service interaction based on the following scenario:

Scenario: {scenario}

Provide your response in the following format:

Response: [Your response to the customer]

Ensure that your response is:
1. Empathetic and understanding of the customer's situation.
2. Provides a clear and helpful solution to the problem.
3. Maintains a polite and professional tone throughout the interaction."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should be empathetic and understanding.",
            "The response should provide a clear and helpful solution to the problem.",
            "The response should maintain a polite and professional tone."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
