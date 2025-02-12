class TaskFamily:
    import time

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "initial_time": "2023-01-01 09:00:00",
                "events": [
                    {"time": "09:10:00", "description": "Meeting with client A"},
                    {"time": "09:15:00", "description": "Urgent call from the boss"},
                    {"time": "09:20:00", "description": "Follow-up with client B"}
                ]
            },
            "2": {
                "initial_time": "2023-01-01 10:00:00",
                "events": [
                    {"time": "10:05:00", "description": "Report submission deadline"},
                    {"time": "10:10:00", "description": "Team meeting"},
                    {"time": "10:15:00", "description": "Email from client C"}
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to manage a series of dynamic events in real-time. You will be given an initial time and a list of events with their respective times and descriptions. Your goal is to handle each event appropriately and efficiently, considering the time constraints and priorities.

Initial Time: {t['initial_time']}
Events:
"""
        for event in t['events']:
            instructions += f"- {event['time']}: {event['description']}\n"
        instructions += "\nGuidelines:\n1. Prioritize urgent events when necessary. For example, an urgent call from the boss should be prioritized over a regular meeting.\n2. Ensure all events are handled within their respective time frames. If two events overlap, provide a clear rationale for how you handle them.\n3. Provide your response in the following format:\nEvent time: [Your action]\nExample Response:\n09:10:00: Attend the meeting with client A.\n09:15:00: Answer the urgent call from the boss.\n09:20:00: Follow up with client B."
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response prioritizes urgent events appropriately.",
            "All events are handled within their respective time frames.",
            "The response demonstrates efficient time management.",
            "The actions are logically consistent with the event descriptions.",
            "The response provides a clear rationale for handling overlapping events, if any."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
