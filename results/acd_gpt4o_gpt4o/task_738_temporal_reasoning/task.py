class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "You have a flight to catch that departs at 3:00 PM. The airport is 1 hour away, and you need to arrive at least 2 hours before the departure time. If it takes you 30 minutes to get ready and another 10 minutes to book a cab, what is the latest time you should start getting ready to ensure you catch your flight on time?"},
            "2": {"scenario": "You have a project deadline on Friday at 5:00 PM. You estimate that you need 15 hours of work to complete the project. If you can work on the project only between 9:00 AM and 6:00 PM from Monday to Friday, how should you distribute your work hours throughout the week to meet the deadline on time?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        scenario = t["scenario"]
        instructions = f"""Your task is to solve the following temporal reasoning problem:

{scenario}

Provide your response in plain text format, clearly explaining your reasoning and calculations. Format your response as follows:

Answer: [Your calculated answer]
Reasoning: [A detailed explanation of your reasoning and calculations]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should correctly solve the temporal reasoning problem.",
            "The response should include clear and logical reasoning and calculations."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
