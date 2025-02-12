class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "You are a manager at a company where a conflict has arisen between two team members. One team member feels that their work is not being recognized, while the other feels overwhelmed by their responsibilities. Your task is to mediate the conflict and propose a solution that addresses both team members' concerns.", "roles": {"manager": "You", "team_member_1": "Alice", "team_member_2": "Bob"}},
            "2": {"scenario": "You are a customer service representative for a tech company. A customer is frustrated because their new device is not working as expected. They have tried multiple troubleshooting steps without success and are now demanding a refund. Your task is to handle the situation, empathize with the customer, and find a satisfactory resolution.", "roles": {"customer_service_rep": "You", "customer": "John"}}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to engage in a role-playing scenario and navigate the situation described below:

Scenario: {t['scenario']}

Roles:
{t['roles']}

Provide a detailed response that demonstrates empathy, effective decision-making, and adaptability. Your response should include:
1. An initial approach to address the situation.
2. Steps to resolve the conflict or issue.
3. Consideration of the emotional states of all parties involved.
4. A final resolution that aims to satisfy everyone involved.

Provide your response in plain text format, clearly separating each of the four components.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should demonstrate empathy.",
            "The response should include effective decision-making steps.",
            "The response should show adaptability to the situation.",
            "The response should aim to satisfy all parties involved.",
            "The response should address the emotional states of all parties involved."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
