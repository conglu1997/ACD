class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"event": "The Fall of the Roman Empire", "prompt": "Analyze the primary reasons behind the fall of the Roman Empire and speculate on how history might have changed if the empire had not fallen. Consider factors such as economic issues, military defeats, and internal strife."},
            "2": {"event": "The American Revolution", "prompt": "Analyze the key factors that led to the success of the American Revolution and speculate on how the world might be different if the revolution had failed. Consider factors such as the involvement of foreign powers, leadership, and colonial unity."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to analyze the following historical event and provide speculative reasoning on an alternative outcome:

Event: {t['event']}

{t['prompt']}

Your analysis should be detailed and cover the following aspects:
1. Key factors and reasons behind the event.
2. Speculative reasoning on how history might have changed if the event had unfolded differently.

Provide your response in plain text format without additional formatting. Ensure your analysis is clear, accurate, and insightful. Structure your response as follows:

- Key Factors: [Your analysis]
- Speculative Reasoning: [Your speculative reasoning]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The analysis should be detailed.", "The analysis should cover the key factors and reasons behind the historical event.", "The speculative reasoning should be insightful and plausible.", "The response should be clear and accurate.", "The response should be structured as instructed."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
