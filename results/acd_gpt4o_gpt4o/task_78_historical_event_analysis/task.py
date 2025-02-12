class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"event": "Fall of the Berlin Wall", "related_event": "Reunification of Germany"},
            "2": {"event": "American Civil War", "related_event": "Abolition of Slavery"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        event = t["event"]
        related_event = t["related_event"]
        instructions = f"""Your task is to analyze the following historical event and discuss its causes and consequences. Additionally, draw connections to a related event.

Historical Event: {event}
Related Event: {related_event}

In your analysis, you should:
1. Provide a brief overview of the historical event.
2. Discuss the main causes that led to the event.
3. Explain the immediate and long-term consequences of the event.
4. Draw connections to the related event and explain how they are linked.

Your analysis should be at least 300 words long and provide a detailed and well-structured examination of the event. Each section should be clearly labeled and elaborated upon.

Provide your analysis in a clear and structured format, with each section clearly labeled."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The overview should accurately describe the historical event.",
            "The causes should be clearly explained and relevant.",
            "The consequences should be logically derived from the event.",
            "The connection to the related event should be clearly established and explained.",
            "The analysis should be at least 300 words long.",
            "The analysis should be detailed and well-structured."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
