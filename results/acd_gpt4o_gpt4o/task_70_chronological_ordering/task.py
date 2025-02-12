class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"events": ["Start of World War II", "Fall of Berlin Wall", "Moon Landing", "Invention of the Internet"], "correct_order": ["Start of World War II", "Moon Landing", "Invention of the Internet", "Fall of Berlin Wall"]},
            "2": {"events": ["Discovery of Penicillin", "First Transatlantic Flight", "Signing of the Declaration of Independence", "Fall of the Roman Empire"], "correct_order": ["Fall of the Roman Empire", "Signing of the Declaration of Independence", "Discovery of Penicillin", "First Transatlantic Flight"]},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return "Arrange the following events in the correct chronological order: " + ", ".join(t["events"]) + ". Provide your answer as a comma-separated list of the events in chronological order, e.g., 'Event1, Event2, Event3, Event4'."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [f"The response should list the events in the correct chronological order."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
