class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"event": "World War II", "change": "Germany did not invade Poland in 1939"},
            "2": {"event": "American Civil War", "change": "Abraham Lincoln was not assassinated in 1865"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to analyze the historical event of {t['event']} and provide a detailed alternative scenario based on the following change: {t['change']}. Your response should include:

1. A brief explanation of the original event.
2. A detailed description of how the specified change might have affected the course of history.
3. Potential short-term and long-term implications of this change.
4. Any other relevant factors or events that might have been influenced by this change.

Ensure your analysis is coherent, logically structured, and historically plausible. Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The analysis should be coherent and logically structured.", "The alternative scenario should be historically plausible and detailed.", "The submission should cover the potential short-term and long-term implications."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
