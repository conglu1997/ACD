class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"type": "generate_speech", "event": "The signing of the Declaration of Independence", "role": "Thomas Jefferson"},
            "2": {"type": "interpret_event", "event": "The fall of the Berlin Wall"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["type"] == "generate_speech":
            event = t["event"]
            role = t["role"]
            instructions = f"""Your task is to generate a historically accurate speech given by {role} during {event}.

Ensure that the speech reflects the historical context, the persona of the speaker, and the significance of the event. The speech should be between 300 and 500 words. Provide your speech in plain text format."""
        elif t["type"] == "interpret_event":
            event = t["event"]
            instructions = f"""Your task is to interpret the significance of the following historical event: {event}.

Provide a detailed analysis of the event's impact, including its historical context, key figures involved, and long-term consequences. Your interpretation should be 300-500 words, accurate, comprehensive, and well-structured. Provide your response in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["type"] == "generate_speech":
            criteria = [
                "The speech should accurately reflect the historical context.",
                "The speech should be consistent with the persona of the speaker.",
                "The speech should convey the significance of the event.",
                "The speech should be between 300 and 500 words."
            ]
        elif t["type"] == "interpret_event":
            criteria = [
                "The interpretation should be historically accurate.",
                "The analysis should be comprehensive and well-structured.",
                "The interpretation should include the event's impact, historical context, key figures, and long-term consequences.",
                "The interpretation should be between 300 and 500 words."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
