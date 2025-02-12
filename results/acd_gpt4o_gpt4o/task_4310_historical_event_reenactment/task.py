class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"event": "The signing of the Declaration of Independence", "figures": ["Thomas Jefferson", "John Adams", "Benjamin Franklin"]},
            "2": {"event": "The fall of the Berlin Wall", "figures": ["Mikhail Gorbachev", "Ronald Reagan", "Helmut Kohl"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Your task is to generate a dialogue between the following historical figures discussing the specified event. Ensure that the dialogue reflects their personalities, historical context, and is coherent and plausible.\nEvent: {t['event']}\nFigures: {', '.join(t['figures'])}\nPlease provide the dialogue in plain text format as follows:\n\n[Character Name]: [Dialogue]\n[Character Name]: [Dialogue]\n..."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The dialogue should accurately reflect the personalities of the historical figures and the context of the event.", "The dialogue should be coherent and historically plausible."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
