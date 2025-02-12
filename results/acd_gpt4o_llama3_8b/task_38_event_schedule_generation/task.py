class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "activities": [
                    {"name": "Opening Ceremony", "duration": 60},
                    {"name": "Keynote Speech", "duration": 45},
                    {"name": "Lunch Break", "duration": 90},
                    {"name": "Workshop 1", "duration": 60},
                    {"name": "Workshop 2", "duration": 60},
                    {"name": "Closing Remarks", "duration": 30}
                ],
                "constraints": [
                    "The event should start at 9:00 AM and end by 5:00 PM.",
                    "There should be a 30-minute break between each activity.",
                    "Lunch Break should be scheduled at 12:00 PM.",
                    "The Keynote Speech should follow the Opening Ceremony.",
                    "Workshops should not be scheduled at the same time."
                ]
            },
            "2": {
                "activities": [
                    {"name": "Registration", "duration": 30},
                    {"name": "Panel Discussion", "duration": 90},
                    {"name": "Coffee Break", "duration": 30},
                    {"name": "Breakout Session 1", "duration": 60},
                    {"name": "Breakout Session 2", "duration": 60},
                    {"name": "Networking", "duration": 60},
                    {"name": "Dinner", "duration": 120}
                ],
                "constraints": [
                    "The event should start at 8:00 AM and end by 8:00 PM.",
                    "There should be a 15-minute break between each activity.",
                    "Coffee Break should be scheduled at 10:30 AM.",
                    "Dinner should be the last activity.",
                    "Breakout Sessions should not overlap.",
                    "Networking should follow the Breakout Sessions."
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a detailed event schedule based on the given activities and constraints: {t['activities']}. Ensure that the schedule meets all the constraints and is logically sequenced. Provide the start and end times for each activity, and include breaks as specified. Submit your schedule as a plain text string with each activity on a new line in the following format: 'Activity Name: Start Time - End Time'. Use the 24-hour time format (e.g., 09:00 for 9:00 AM). Ensure that no activities overlap and that all breaks are included.

Example Submission:
Opening Ceremony: 09:00 - 10:00
Break: 10:00 - 10:30
Keynote Speech: 10:30 - 11:15
Break: 11:15 - 11:45
Lunch Break: 12:00 - 13:30
Workshop 1: 13:30 - 14:30
Break: 14:30 - 15:00
Workshop 2: 15:00 - 16:00
Break: 16:00 - 16:30
Closing Remarks: 16:30 - 17:00"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The schedule should start and end within the specified times.",
            "All activities should be included in the schedule.",
            "The schedule should include the specified breaks.",
            "Activities should be logically sequenced and not overlap.",
            "All constraints should be satisfied.",
            "The duration between activities should include the specified breaks."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
