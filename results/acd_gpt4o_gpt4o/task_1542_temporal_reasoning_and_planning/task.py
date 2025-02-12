class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"events": [
                {"name": "Meeting with client", "start": "09:00", "end": "10:00"},
                {"name": "Team stand-up", "start": "10:15", "end": "10:45"},
                {"name": "Lunch break", "start": "12:00", "end": "13:00"},
                {"name": "Project work", "start": "13:30", "end": "17:00"},
                {"name": "Gym", "start": "18:00", "end": "19:00"}
            ],
            "constraints": [
                "The day starts at 08:00 and ends at 20:00.",
                "No two events can overlap.",
                "There should be at least 15 minutes of break between consecutive events."]},
            "2": {"events": [
                {"name": "Doctor's appointment", "start": "08:30", "end": "09:30"},
                {"name": "Client call", "start": "10:00", "end": "11:00"},
                {"name": "Coding session", "start": "11:30", "end": "13:00"},
                {"name": "Lunch", "start": "13:00", "end": "14:00"},
                {"name": "Team meeting", "start": "14:30", "end": "15:30"},
                {"name": "Review work", "start": "16:00", "end": "17:00"}
            ],
            "constraints": [
                "The day starts at 08:00 and ends at 18:00.",
                "No two events can overlap.",
                "There should be at least 30 minutes of break between consecutive events."]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        events_str = '\n'.join([f"{event['name']} ({event['start']} to {event['end']})" for event in t['events']])
        constraints_str = '\n'.join(t['constraints'])
        return f"Your task is to create a valid plan or schedule for the given sequence of events and constraints. Ensure that your plan adheres to all the constraints provided. Here are the details:\n\nEvents:\n{events_str}\n\nConstraints:\n{constraints_str}\n\nProvide your response in plain text format, listing the events in the order they should occur, including any necessary breaks as per the constraints."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The plan should adhere to all given time constraints.",
            "The plan should ensure no two events overlap.",
            "The plan should include necessary breaks between events as specified."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
