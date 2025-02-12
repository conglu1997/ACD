class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "events": [
                    {"event": "Meeting with team", "start_time": "09:00", "end_time": "10:00"},
                    {"event": "Lunch", "start_time": "12:00", "end_time": "13:00"},
                    {"event": "Client call", "start_time": "11:30", "end_time": "12:30"},
                    {"event": "Project presentation", "start_time": "10:15", "end_time": "11:15"}
                ],
                "instructions": "Identify any conflicting events and suggest a new schedule that resolves the conflicts. Submit your new schedule in the following format:\n[event1: new_start_time - new_end_time, event2: new_start_time - new_end_time, ...]"
            },
            "2": {
                "timeline": [
                    {"event": "Event A", "time": "08:00"},
                    {"event": "Event B", "time": "09:30"},
                    {"event": "Event C", "time": "11:00"},
                    {"event": "Event D", "time": "10:30"},
                    {"event": "Event E", "time": "09:00"}
                ],
                "instructions": "Construct a chronological sequence of events based on the given timeline. Submit your sequence in the following format:\n[event1, event2, event3, ...]"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""{t['instructions']}

Events/Timeline:
{t['events'] if 'events' in t else t['timeline']}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The submission should accurately identify any conflicts and provide a viable new schedule." if 'events' in t else "The submission should correctly sequence the events chronologically."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
