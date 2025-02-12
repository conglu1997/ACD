class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"role": "Buyer", "context": "negotiating the price and terms for purchasing a piece of real estate", "constraints": "Budget limit of $500,000, must include a home inspection clause"},
            "2": {"role": "Employee", "context": "negotiating a salary and benefits package for a new job offer", "constraints": "Minimum salary of $80,000, must include health insurance benefits"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        role = t["role"]
        context = t["context"]
        constraints = t["constraints"]
        return f"""You are a {role}. Your task is to negotiate the following scenario: {context}. You must reach an agreement that satisfies the following constraints: {constraints}. Conduct the negotiation as a structured dialogue, with each turn of dialogue clearly labeled as either 'You' or 'Counterparty'. Aim to reach a mutually beneficial agreement while adhering to the constraints. Submit your dialogue as a plain text string in the following format:

You: [Your initial proposal]
Counterparty: [Counterparty's response]
You: [Your response]
Counterparty: [Counterparty's response]
... and so on, until an agreement is reached. Clearly indicate the final agreement at the end of the dialogue."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The negotiation must be conducted as a structured dialogue.", "The final agreement must satisfy the specified constraints.", "The dialogue should demonstrate strategic thinking and persuasive negotiation tactics."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
