class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"argument": "If we don't reduce our carbon emissions, the world will end in 10 years. Therefore, we must ban all cars immediately."},
            "2": {"argument": "My opponent suggests that we should use renewable energy sources. But I say, why should we listen to someone who eats meat every day?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to identify and explain the logical fallacy present in the following argumentative statement:

Argument: {t['argument']}

Your response should include:
1. The name of the logical fallacy.
2. A brief explanation of why this argument is fallacious.

Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response correctly identifies the logical fallacy.", "The response provides an accurate explanation of why the argument is fallacious."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
