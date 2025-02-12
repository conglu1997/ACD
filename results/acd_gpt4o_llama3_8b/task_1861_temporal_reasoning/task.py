class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "events": [
                    {"event": "Breakfast", "time": "8:00 AM"},
                    {"event": "Morning Meeting", "time": "9:30 AM"},
                    {"event": "Project Work", "time": "11:00 AM"},
                    {"event": "Lunch", "time": "12:30 PM"},
                    {"event": "Afternoon Meeting", "time": "2:00 PM"},
                    {"event": "Report Writing", "time": "3:30 PM"},
                    {"event": "End of Workday", "time": "5:00 PM"}
                ],
                "instructions": "Organize the following events into a timeline, ensuring the sequence of events is logical and time-ordered. Submit your response as a plain text string with events ordered by time in the format: 'Event: [time]'."
            },
            "2": {
                "events": [
                    {"event": "Wake up", "time": "7:00 AM"},
                    {"event": "Exercise", "time": "7:30 AM"},
                    {"event": "Shower", "time": "8:00 AM"},
                    {"event": "Breakfast", "time": "8:30 AM"},
                    {"event": "Work on Project", "time": "9:00 AM"},
                    {"event": "Meeting with Team", "time": "10:00 AM"},
                    {"event": "Lunch", "time": "12:00 PM"},
                    {"event": "Afternoon Work", "time": "1:00 PM"},
                    {"event": "Finish Work", "time": "5:00 PM"}
                ],
                "instructions": "Organize the following events into a timeline, ensuring the sequence of events is logical and time-ordered. Submit your response as a plain text string with events ordered by time in the format: 'Event: [time]'."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"{t['instructions']}\n\nEvents:\n" + "\n".join([f"- {event['event']} at {event['time']}" for event in t['events']])

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The timeline should follow a logical sequence based on the given times.",
            "Each event should be placed correctly according to its specified time."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
