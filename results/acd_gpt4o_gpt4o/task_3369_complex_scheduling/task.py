class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"constraints": "You have the following events to schedule for your day: (1) Meeting with Bob from 10:00 AM to 11:00 AM, (2) Project work for 3 hours, (3) Lunch with Sarah from 12:00 PM to 1:00 PM, (4) Gym for 1 hour, (5) Reading for 2 hours. Ensure that there is at least a 30-minute break between consecutive events."},
            "2": {"constraints": "You have the following events to schedule for your day: (1) Doctor's appointment from 9:00 AM to 10:00 AM, (2) Team meeting from 2:00 PM to 3:00 PM, (3) Study session for 2 hours, (4) Dinner with family from 6:00 PM to 7:00 PM, (5) Free time for 1 hour. Ensure that no two events overlap and there is at least 15 minutes of buffer time between them."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to create a detailed schedule for a given day based on the specified constraints. Here are the constraints:

{t['constraints']}

Ensure that the schedule meets all the specified constraints and is logically organized. Provide your response in plain text format as follows:

Schedule:
[Your detailed schedule here]

Each event should be listed with its start and end time, and there should be clear breaks as specified in the constraints."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The schedule should meet all the specified constraints.", "The schedule should be logically organized and free from overlaps.", "There should be appropriate breaks between events as specified.", "Each event should be listed with its start and end time."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
