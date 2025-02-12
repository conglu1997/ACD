class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "You are an AI assistant in a customer service setting. A customer is calling to complain about a recent order they received. The customer is upset because the product was damaged. Manage the conversation to address the customer's concerns and provide a resolution.",
                "criteria": "The dialogue should be coherent, empathetic, and effectively address the customer's issue. The assistant should offer a reasonable resolution and maintain a polite and professional tone throughout the conversation."},
            "2": {
                "scenario": "You are an AI assistant in a medical setting. A patient is calling to inquire about the side effects of a medication they have been prescribed. Manage the conversation to provide accurate information and reassure the patient.",
                "criteria": "The dialogue should be informative, reassuring, and accurate regarding the medication's side effects. The assistant should prioritize the patient's well-being, provide relevant information, and maintain a calm and empathetic tone throughout the conversation."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Simulate and manage a conversation for the following scenario based on the given criteria:

Scenario: {t["scenario"]}

Ensure that the conversation is coherent and addresses the specified criteria. Submit your response as a plain text dialogue script in the following format:

AI: [AI's response]
Customer: [Customer's response]
AI: [AI's response]
...

Example:

AI: Hello! How can I assist you today?
Customer: I received a damaged product in my recent order.
AI: I'm sorry to hear that. Could you please provide me with your order number so I can look into this for you?
Customer: Sure, it's 123456.
AI: Thank you. I see that the product was indeed damaged. We can offer you a replacement or a full refund. Which would you prefer?
Customer: I'd like a replacement, please.
AI: Certainly. I will process that for you right away. You should receive the replacement within 5-7 business days. Is there anything else I can assist you with?
Customer: No, that's all. Thank you.
AI: You're welcome! Have a great day!
..."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [t["criteria"]]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
