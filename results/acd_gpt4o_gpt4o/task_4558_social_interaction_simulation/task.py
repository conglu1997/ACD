class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {'scenario': 'Alice and Bob are colleagues working on a project. Alice has been consistently doing more work, and Bob has been taking it easy. One day, Alice confronts Bob about this. Predict the possible outcomes of this confrontation.'},
            '2': {'scenario': 'Sarah is hosting a dinner party and invites her friends, including Mark who is known for his controversial opinions. During the dinner, Mark starts sharing his views loudly. Predict the possible reactions of the other guests and the overall outcome of the dinner party.'}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to simulate and predict the outcomes of the following social interaction scenario:

Scenario: {t['scenario']}

Your response should include:
1. A detailed prediction of the possible outcomes.
2. The reasoning behind each predicted outcome.

Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response includes detailed predictions of the possible outcomes.", "The response provides clear reasoning behind each predicted outcome."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
