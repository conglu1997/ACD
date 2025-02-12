class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"dilemma": "You are a doctor with one dose of life-saving medication and two patients in critical condition. One is a young child with a high chance of survival with the medication, and the other is an elderly person who has contributed greatly to society but has a lower chance of survival. Who do you choose to save and why?"},
            "2": {"dilemma": "You are a bystander at a train junction. A runaway train is heading towards five workers on the track. You can pull a lever to divert the train onto another track, but it will kill one worker on that track. Do you pull the lever and why?"},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Resolve the following ethical dilemma by providing a well-reasoned response that balances conflicting values:

{t["dilemma"]}

Your response should clearly state your decision and provide the reasoning behind it. Ensure that your reasoning addresses the key ethical principles and values involved. The response should be at least 150 words long. Submit your response as a plain text string in the following format: 'Decision: [Your decision] Reasoning: [Your reasoning]'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should clearly state the decision.", "The response should provide a well-reasoned explanation for the decision.", "The reasoning should address the key ethical principles and values involved.", "The response should be at least 150 words long."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
