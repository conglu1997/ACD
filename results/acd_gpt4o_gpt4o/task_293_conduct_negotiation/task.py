class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "You are negotiating a salary for a new job. Your goal is to secure a salary of at least $80,000, but the employer's initial offer is $70,000.", "requirements": "Negotiate effectively to reach a mutually beneficial agreement. Aim for a salary as close to $80,000 as possible. Ensure the negotiation involves multiple exchanges."},
            "2": {"scenario": "You are negotiating the price of a car. You are willing to pay up to $20,000, but the seller's asking price is $25,000.", "requirements": "Negotiate effectively to reach a mutually beneficial agreement. Aim for a price as close to $20,000 as possible. Ensure the negotiation involves multiple exchanges."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        scenario = t["scenario"]
        requirements = t["requirements"]
        instructions = f"""Your task is to engage in a negotiation based on the following scenario:

{scenario}

Ensure that your negotiation meets the following requirements:
{requirements}

Begin the negotiation and provide your responses in plain text format. Make sure your responses are appropriate and contextually relevant throughout the negotiation.

Example for Task 1: If the scenario was 'You are negotiating a salary for a new job. Your goal is to secure a salary of at least $80,000, but the employer's initial offer is $70,000.', you might start with:

Agent: 'Thank you for the offer. I appreciate the opportunity and would like to discuss the salary further. Based on my experience and the market rate, I believe a salary of $80,000 would be more appropriate.'

Employer: 'We value your skills and experience, but our budget is limited. How about we meet halfway at $75,000?'

Agent: 'I understand the budget constraints. Considering the potential contributions I can make to the company, I believe $78,000 would be a fair compromise.'

Employer: 'Let's finalize it at $78,000. Welcome aboard!'

This is just an example. Ensure your negotiation involves multiple exchanges and demonstrates strategic communication, empathy, and problem-solving."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The negotiation should be strategic.",
            "The negotiation should aim for a mutually beneficial outcome.",
            "The language should be empathetic and assertive.",
            "The negotiation should involve multiple exchanges.",
            "The final agreement should be as close to the target as possible."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
