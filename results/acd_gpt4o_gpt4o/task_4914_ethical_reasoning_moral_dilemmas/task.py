class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"dilemma": "A train is heading towards five workers on the track. You are standing next to a lever that can switch the train to another track, where there is one worker. Do you pull the lever?"},
            "2": {"dilemma": "A pharmaceutical company has developed a life-saving drug, but it is extremely expensive. Should the company be allowed to set any price it wants, or should there be regulations to make it affordable for all?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to analyze and provide a solution to the following moral dilemma: '{t["dilemma"]}'. Your response should include:

1. A clear statement of your decision or proposed solution.
2. A detailed explanation of the ethical principles and reasoning behind your decision.
3. Consideration of potential objections to your decision and your responses to those objections.
4. Any relevant examples or analogies that support your reasoning."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include a clear decision or proposed solution to the dilemma.",
            "The response should provide a detailed explanation of the ethical principles and reasoning behind the decision.",
            "The response should consider potential objections and provide responses to those objections.",
            "The response should use relevant examples or analogies to support the reasoning."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
