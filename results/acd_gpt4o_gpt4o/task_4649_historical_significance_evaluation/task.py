class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"event": "The signing of the Magna Carta in 1215"},
            "2": {"event": "The fall of the Berlin Wall in 1989"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to evaluate the significance of the following historical event and provide a reasoned explanation for your evaluation.

Historical Event: {t['event']}

In your response, consider the following aspects:
1. Immediate impact of the event.
2. Long-term consequences.
3. Influence on subsequent historical developments.
4. Any changes in societal, political, or economic structures resulting from the event.

Provide your response in plain text format. Structure your response as follows:
1. Immediate Impact:
2. Long-Term Consequences:
3. Influence on Subsequent Developments:
4. Changes in Structures:
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should provide a reasoned evaluation of the historical event.",
            "The response should consider immediate impact, long-term consequences, and influence on subsequent historical developments.",
            "The response should be coherent and well-structured.",
            "The response should demonstrate a good understanding of historical context and significance."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
