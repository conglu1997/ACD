class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "You are planning a small party with a budget of $100. You need to buy snacks, drinks, and decorations. Each category must have at least one item. Snacks cost $2 each, drinks cost $3 each, and decorations cost $5 each. Provide a list of items and their quantities that fit within the budget and maximize the variety of items.",
                "constraints": "You can only buy whole items. List the items and their quantities in the format: 'Snacks: [quantity], Drinks: [quantity], Decorations: [quantity]'. The total cost should not exceed $100."
            },
            "2": {
                "scenario": "You are organizing a one-day workshop with a budget of $500. You need to allocate funds for venue rental, refreshments, and speaker fees. The venue rental costs $200, refreshments cost $10 per person, and each speaker charges $100. You expect 20 attendees and want to have at least 2 speakers. Provide a budget allocation that meets these requirements and maximizes the number of speakers.",
                "constraints": "Provide the allocation in the format: 'Venue: [amount], Refreshments: [amount], Speakers: [amount]'. The total cost should not exceed $500."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are given the following scenario:

Scenario: {t['scenario']}

Constraints: {t['constraints']}

Instructions:
1. Carefully analyze the scenario and constraints.
2. Calculate the optimal decision that fits within the budget and meets the requirements.
3. Ensure your decision is practical and maximizes the specified criteria (variety of items for Task 1, number of speakers for Task 2).
4. Submit your decision in the specified format: Snacks: [quantity], Drinks: [quantity], Decorations: [quantity] (for Task 1) or Venue: [amount], Refreshments: [amount], Speakers: [amount] (for Task 2)."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The decision must fit within the constraints provided.",
            "The total cost should not exceed the given budget.",
            "The solution should maximize the variety of items (for Task 1) or the number of speakers (for Task 2).",
            "The submission format should match the specified format exactly."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
