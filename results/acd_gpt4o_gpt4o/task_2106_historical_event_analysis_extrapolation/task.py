class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"event": "Fall of the Berlin Wall", "hypothetical_change": "The Berlin Wall never fell."},
            "2": {"event": "Discovery of Penicillin", "hypothetical_change": "Penicillin was never discovered."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        event = t["event"]
        hypothetical_change = t["hypothetical_change"]
        instructions = f"""Your task is to analyze the following historical event and then extrapolate potential future consequences based on a hypothetical change in the event:

Historical Event: {event}
Hypothetical Change: {hypothetical_change}

1. Provide a detailed analysis of the original historical event, including its significance and impact on subsequent events.
2. Extrapolate and describe the potential future consequences if the hypothetical change had occurred. Ensure your extrapolation is logical and considers various aspects such as social, political, economic, and cultural impacts.

Provide your response in the following format:

Analysis: [Your detailed analysis of the original event]
Extrapolation: [Your extrapolated consequences based on the hypothetical change]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The analysis should be detailed and accurate.",
            "The extrapolation should be logical and consider various aspects such as social, political, economic, and cultural impacts."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
