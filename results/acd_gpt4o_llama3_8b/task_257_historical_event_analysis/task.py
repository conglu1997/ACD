class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"event1": "Fall of the Roman Empire", "event2": "Renaissance"},
            "2": {"event1": "Industrial Revolution", "event2": "World War I"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        event1 = t["event1"]
        event2 = t["event2"]
        return f"""Analyze the connection between '{event1}' and '{event2}'. Explain how the first event influenced the second, highlighting any significant impacts or changes that occurred as a result. Your analysis should be well-structured, historically accurate, and provide a clear connection between the events. Submit your analysis as a plain text string in a single paragraph."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The analysis should be well-structured and historically accurate.",
            "The analysis should clearly explain the connection between the two events.",
            "The analysis should highlight significant impacts or changes that occurred as a result of the first event."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
