class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "You are a cheerful and optimistic person. Respond to the following situation: You are in a long queue at the supermarket, and someone ahead of you is taking a very long time. Other people in the queue are getting impatient."},
            "2": {"scenario": "You are a grumpy and impatient person. Respond to the following situation: You are at a restaurant, and the waiter has just informed you that your order will be delayed by 30 minutes."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Simulate a character with specific personality traits and generate a response that is consistent with those traits. Here is the scenario:

{t['scenario']}

Ensure that the response is natural, relevant, and maintains the character's personality traits throughout."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should be consistent with the specified personality traits.", "The response should be natural and relevant to the situation."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
