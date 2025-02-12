class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"event": "The fall of the Berlin Wall in 1989", "question": "Analyze the significance of the fall of the Berlin Wall and draw parallels to a contemporary event that represents a significant political change."},
            "2": {"event": "The signing of the Treaty of Versailles in 1919", "question": "Discuss the impact of the Treaty of Versailles on post-World War I Europe and draw parallels to a modern-day treaty or agreement that has had significant geopolitical consequences."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the following historical event and answer the question provided. Draw parallels to a contemporary issue, providing a detailed and well-reasoned explanation:

Historical Event: {t['event']}

Question: {t['question']}
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should accurately analyze the historical event.",
            "The response should draw a relevant and coherent parallel to a contemporary issue.",
            "The explanation should be detailed and well-reasoned.",
            "The response should be in plain text format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
