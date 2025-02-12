class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "event": "A wedding reception",
                "requirements": [
                    "Date: June 20, 2023",
                    "Venue: Outdoor garden",
                    "Guest count: 100",
                    "Catering: Vegetarian menu",
                    "Entertainment: Live band",
                    "Decorations: Floral theme"
                ]
            },
            "2": {
                "event": "A corporate conference",
                "requirements": [
                    "Date: September 15, 2023",
                    "Venue: Hotel conference hall",
                    "Guest count: 200",
                    "Catering: Buffet lunch",
                    "Entertainment: Keynote speaker",
                    "Decorations: Professional and modern"
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a detailed plan for the following event: {t['event']}. Ensure the plan meets all the given requirements. The plan should include the following sections:

1. Introduction: Brief overview of the event.
2. Date and Time: Detailed schedule of the event.
3. Venue: Description of the venue setup and arrangements.
4. Guest Management: Plan for managing and accommodating the guests.
5. Catering: Detailed catering plan matching the given requirements.
6. Entertainment: Detailed plan for the entertainment activities.
7. Decorations: Description of the decorations and theme.

Ensure that each section is well-structured, comprehensive, and meets the given requirements. Submit your plan as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The plan should be well-structured and comprehensive.",
            "The plan should meet all the given requirements.",
            "Each section should be detailed and contextually appropriate."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
