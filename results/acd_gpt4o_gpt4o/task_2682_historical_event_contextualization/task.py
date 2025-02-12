class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "event": "The fall of the Berlin Wall"
            },
            "2": {
                "event": "The signing of the Magna Carta in 1215"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to provide a detailed context, significance, and explanation of the following historical event: '{t['event']}'.\n\nYour response should include:\n1. A brief overview of the event.\n2. The historical context leading up to the event.\n3. The significance of the event at the time it occurred.\n4. The long-term impact of the event on history.\n\nYour response should be at least 300 words long and provide in-depth insights. Ensure your response is coherent, well-structured, and provides insightful explanations. Provide your response in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include a brief overview of the event.",
            "The response should provide the historical context leading up to the event.",
            "The response should explain the significance of the event at the time it occurred.",
            "The response should discuss the long-term impact of the event on history.",
            "The response should be coherent and well-structured.",
            "The response should be at least 300 words long."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
