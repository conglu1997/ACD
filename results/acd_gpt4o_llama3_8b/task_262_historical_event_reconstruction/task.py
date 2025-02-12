class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"event_name": "The Mysterious Disappearance of the Roanoke Colony", "details": "In 1587, a group of settlers established the Roanoke Colony. However, when supply ships returned in 1590, the colony was found abandoned with no trace of the settlers."},
            "2": {"event_name": "The Rise of the Byzantine Empire", "details": "In the early 4th century, the city of Byzantium was transformed into the capital of a new empire. The empire's rise was marked by significant cultural, military, and economic developments."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a detailed and plausible narrative of the following fictional historical event: '{t["event_name"]}'. The narrative should include:
1. A clear description of the event's background and context.
2. Key figures involved in the event and their roles.
3. Significant actions, decisions, and outcomes related to the event.
4. A conclusion that ties the narrative together and reflects on the event's impact.

Ensure that the narrative is coherent, historically plausible, and engaging. Submit your narrative as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The narrative should include a clear description of the event's background and context.", "The narrative should include key figures involved in the event and their roles.", "The narrative should include significant actions, decisions, and outcomes related to the event.", "The narrative should include a conclusion that ties the narrative together and reflects on the event's impact.", "The narrative should be coherent, historically plausible, and engaging."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
