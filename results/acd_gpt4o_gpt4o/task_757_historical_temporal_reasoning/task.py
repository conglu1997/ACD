class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"events": ["The fall of the Berlin Wall", "The signing of the Treaty of Versailles", "The first moon landing", "The assassination of Archduke Franz Ferdinand"]},
            "2": {"events": ["The invention of the printing press", "The signing of the Magna Carta", "The discovery of America by Columbus", "The beginning of the Industrial Revolution"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        events = t["events"]
        instructions = f"""Your task is to determine the chronological order of the following historical events and provide a brief explanation of their significance:

Events: {', '.join(events)}

Your response should be structured as follows:
1. Chronological Order: [List the events in chronological order, each on a new line]
2. Explanation: [Provide a brief explanation (1-2 sentences) of the significance of each event in the order you listed them]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The chronological order of the events should be correct.",
            "The explanation for each event should be brief and accurate."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
