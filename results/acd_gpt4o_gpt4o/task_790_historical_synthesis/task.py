class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"event": "The French Revolution (1789-1799)", "contemporary_issue": "Modern political protests and movements."},
            "2": {"event": "The Industrial Revolution (1760-1840)", "contemporary_issue": "The rise of artificial intelligence and automation."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        event = t["event"]
        contemporary_issue = t["contemporary_issue"]
        instructions = f"""Your task is to analyze the historical event provided and synthesize insights or parallels with the contemporary issue mentioned.

Historical Event: {event}

Contemporary Issue: {contemporary_issue}

Your analysis should be clear, logical, and insightful. Draw meaningful connections between the historical event and the contemporary issue. Ensure your analysis is historically accurate and provides a deep understanding of both the historical event and the contemporary issue. Provide your response in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The analysis should draw meaningful connections between the historical event and the contemporary issue.",
            "The analysis should be clear, logical, and insightful.",
            "The analysis should be historically accurate and provide a deep understanding of both the historical event and the contemporary issue."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
