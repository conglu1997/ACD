class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "customer_inquiry": "I received a damaged product in my recent order. I need a replacement, but I'm concerned about the turnaround time. What should I do?"
            },
            "2": {
                "customer_inquiry": "I need to change the shipping address for my order, but it has already been dispatched. Can you help me with that?"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are a customer service representative. Please respond to the following customer inquiry:

Customer Inquiry: {t['customer_inquiry']}

Your response should be polite, helpful, and address the customer's concern effectively. Provide clear instructions or solutions to resolve the issue. Submit your response as a plain text string in the following format:

Response: [Your response here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = ["The response should be polite and professional.", "The response should address the customer's concern effectively.", "The response should provide clear instructions or solutions to resolve the issue.", "The response should consider the customer's specific concerns (e.g., turnaround time, address change after dispatch)."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
