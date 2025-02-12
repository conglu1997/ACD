class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"topic": "Should we implement universal basic income?"},
            "2": {"topic": "Is nuclear energy a viable solution to climate change?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to present balanced arguments and counterarguments on the following controversial topic:

Topic: {t['topic']}

Your response should include:
1. A clear and coherent argument in favor of the topic.
2. A clear and coherent argument against the topic.
3. A conclusion that summarizes both perspectives without bias.

Each argument should be detailed and provide at least three supporting points or examples. Ensure your response is thoughtful, balanced, and demonstrates a clear understanding of the multiple perspectives involved. Format your response as follows:

1. Argument in favor:
2. Argument against:
3. Conclusion:"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should present clear and coherent arguments in favor and against the topic.",
            "Each argument should include at least three supporting points or examples.",
            "The conclusion should summarize both perspectives without showing bias."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
