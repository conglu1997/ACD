class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "You are negotiating the terms of a job offer. Your goal is to maximize your salary while ensuring you get at least two weeks of vacation. The employer's initial offer is $50,000 per year with one week of vacation. Additionally, you want to secure the option to work remotely two days a week.",
                "constraints": {
                    "initial_offer": "$50,000 per year with one week of vacation",
                    "minimum_vacation": "two weeks",
                    "remote_work": "two days a week"
                }
            },
            "2": {
                "scenario": "You are negotiating the price of a used car. Your goal is to purchase the car for the lowest possible price while ensuring it includes a one-year warranty. The seller's initial asking price is $10,000 with no warranty. Additionally, you want to negotiate for the car to be fully serviced before delivery.",
                "constraints": {
                    "initial_offer": "$10,000 with no warranty",
                    "minimum_warranty": "one year",
                    "full_service": "before delivery"
                }
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to simulate a negotiation scenario based on the given details. Here are the specifics:

Scenario: {t['scenario']}

Constraints: {t['constraints']}

Instructions:
1. Initiate the negotiation with a greeting and a counteroffer.
2. Engage in a back-and-forth conversation to negotiate the terms.
3. Ensure that the final agreement clearly and explicitly meets all the specified constraints.
4. Provide a summary of the negotiation and the final agreement.

Example Response Format:
Greeting: [Your initial greeting and counteroffer]
Negotiation: [Your back-and-forth conversation]
Final Agreement: [Summary of the final agreement, explicitly stating how each constraint is met]

Ensure that your negotiation is realistic, strategic, and adheres to the specified constraints. The final agreement must clearly and explicitly include the negotiated terms that meet all the constraints."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The negotiation should start with a greeting and a counteroffer.",
            "The conversation should include multiple back-and-forth exchanges.",
            "The final agreement should clearly and explicitly meet all the specified constraints.",
            "The negotiation should be realistic and strategic."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
