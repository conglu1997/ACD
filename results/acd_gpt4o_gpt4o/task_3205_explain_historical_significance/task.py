class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"event": "The Fall of the Berlin Wall", "audience": "a high school history class"},
            "2": {"event": "The Signing of the Magna Carta", "audience": "a group of tourists visiting a historical museum"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to explain the significance of the following historical event tailored for the given audience:

Event: {t['event']}
Audience: {t['audience']}

Ensure that your explanation is clear, accurate, and appropriate for the specified audience. Aim to make the explanation engaging and informative. Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The explanation should be clear and accurate.", "The explanation should be appropriate for the given audience.", "The explanation should be engaging and informative."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
