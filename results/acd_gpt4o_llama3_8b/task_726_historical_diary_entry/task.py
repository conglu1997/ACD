class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "figure": "Albert Einstein",
                "date": "November 7, 1919",
                "event": "Confirmation of General Relativity"
            },
            "2": {
                "figure": "Marie Curie",
                "date": "December 10, 1903",
                "event": "Receiving the Nobel Prize in Physics"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Write a diary entry from the perspective of {t['figure']} on {t['date']} about the following event: {t['event']}.

Ensure that the diary entry is historically accurate and captures the emotional and contextual nuances of the event. The entry should provide deep insights into the figure's thoughts, feelings, and experiences on that particular day. Include specific historical details and personal reflections. Submit your diary entry as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The diary entry should be historically accurate.",
            "The diary entry should capture the emotional and contextual nuances of the event.",
            "The diary entry should provide deep insights into the figure's thoughts, feelings, and experiences on that particular day.",
            "The diary entry should include specific historical details and personal reflections."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
