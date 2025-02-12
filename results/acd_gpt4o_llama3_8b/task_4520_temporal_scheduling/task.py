class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "events": [
                    {"name": "Event A", "duration": 2, "constraints": ["must start after 9 AM"]},
                    {"name": "Event B", "duration": 1, "constraints": ["must end before 12 PM"]},
                    {"name": "Event C", "duration": 1, "constraints": ["must start after Event A"]},
                    {"name": "Event D", "duration": 1, "constraints": ["must end before 3 PM", "must start after 11 AM"]}
                ],
                "time_range": "9 AM to 5 PM"
            },
            "2": {
                "events": [
                    {"name": "Task 1", "duration": 2, "constraints": ["must be completed before 3 PM"]},
                    {"name": "Task 2", "duration": 1, "constraints": ["must start after Task 1"]},
                    {"name": "Task 3", "duration": 1, "constraints": ["must start after 1 PM"]},
                    {"name": "Task 4", "duration": 1, "constraints": ["must start after Task 2", "must end before 5 PM"]}
                ],
                "time_range": "10 AM to 6 PM"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = "Organize the following events within the given time range, ensuring no conflicts and meeting all specified constraints. Use 12-hour AM/PM format for times."
        events_description = "\n".join([f"{event['name']}: {event['duration']} hour(s), Constraints: {', '.join(event['constraints'])}" for event in t['events']])
        example_schedule = "Event A -> 9 AM -> 11 AM\nEvent B -> 11 AM -> 12 PM"
        return f"""{instructions}

Events:
{events_description}

Time Range: {t['time_range']}

Submit your schedule in the following format:
[Event name] -> [Start time (e.g., 9 AM)] -> [End time (e.g., 11 AM)]

Example:
{example_schedule}

Ensure that all constraints are satisfied and there are no conflicts in the schedule."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from datetime import datetime, timedelta
        try:
            lines = submission.strip().split('\n')
            schedule = []
            for line in lines:
                parts = line.split(' -> ')
                event_name = parts[0]
                start_time = datetime.strptime(parts[1], '%I %p')
                end_time = datetime.strptime(parts[2], '%I %p')
                schedule.append((event_name, start_time, end_time))

            events_dict = {event['name']: event for event in t['events']}
            for event_name, start_time, end_time in schedule:
                event = events_dict[event_name]
                # Check duration
                duration = (end_time - start_time).total_seconds() / 3600
                if duration != event['duration']:
                    return 0.0
                # Check constraints
                for constraint in event['constraints']:
                    if 'must start after' in constraint:
                        if 'AM' in constraint or 'PM' in constraint:
                            constraint_time = datetime.strptime(constraint.split('after ')[1], '%I %p')
                            if start_time <= constraint_time:
                                return 0.0
                        else:
                            constraint_event = constraint.split('after ')[1]
                            for scheduled_event, scheduled_start, scheduled_end in schedule:
                                if scheduled_event == constraint_event and start_time <= scheduled_end:
                                    return 0.0
                    elif 'must end before' in constraint:
                        constraint_time = datetime.strptime(constraint.split('before ')[1], '%I %p')
                        if end_time >= constraint_time:
                            return 0.0
            # Check for conflicts
            for i in range(len(schedule)):
                for j in range(i + 1, len(schedule)):
                    if schedule[i][2] > schedule[j][1] and schedule[i][1] < schedule[j][2]:
                        return 0.0
            return 1.0
        except Exception as e:
            return 0.0
