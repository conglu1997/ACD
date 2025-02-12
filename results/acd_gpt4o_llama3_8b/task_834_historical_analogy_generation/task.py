class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"event": "The fall of the Roman Empire.", "task_type": "generate_analogy"},
            "2": {"event": "The Industrial Revolution.", "task_type": "generate_analogy"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a historical analogy by comparing the given historical event with another event or period that shares similar characteristics.

Event: {t['event']}

Your analogy should:
1. Clearly identify the historical event or period being compared to the given event.
2. Highlight the key similarities and differences between the two events or periods.
3. Provide a brief explanation of why this analogy is effective and what can be learned from the comparison.

Submit your response as a plain text string with clearly labeled sections for 'Analogy', 'Similarities', 'Differences', and 'Explanation'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should identify a historical event or period being compared to the given event.",
            "The response should highlight the key similarities and differences between the two events or periods.",
            "The response should include a brief explanation of why the analogy is effective and what can be learned from the comparison.",
            "The response should exhibit a deep understanding of both historical events or periods."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
