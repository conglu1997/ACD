class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "You are organizing a one-day conference with multiple speakers, workshops, and breaks. The conference starts at 9 AM and ends at 5 PM. You need to create a schedule that includes three keynote speeches (each 1 hour), four workshops (each 1.5 hours), lunch break (1 hour), and two coffee breaks (30 minutes each). Ensure no overlap between events. All events must be scheduled within the 9 AM to 5 PM time frame.", "type": "conference"},
            "2": {"scenario": "You are planning a week-long training program for new employees. The program runs from Monday to Friday, 9 AM to 5 PM each day. You need to create a schedule that includes daily team-building activities (1 hour), five different training sessions (each 2 hours), lunch breaks (1 hour), and daily review sessions (1 hour). Ensure no overlap between events. All events must be scheduled within the 9 AM to 5 PM time frame.", "type": "training"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["type"] == "conference":
            return f"""Create a detailed schedule for the following conference scenario:

Scenario: {t["scenario"]}

Your schedule should include the exact timing for each event, ensuring no overlaps. Submit your schedule as a plain text string in the following format:

Example:
9:00 AM - 10:00 AM: Keynote Speech 1
10:00 AM - 11:30 AM: Workshop 1
11:30 AM - 12:00 PM: Coffee Break
12:00 PM - 1:00 PM: Keynote Speech 2
1:00 PM - 2:00 PM: Lunch Break
2:00 PM - 3:30 PM: Workshop 2
3:30 PM - 4:00 PM: Coffee Break
4:00 PM - 5:00 PM: Keynote Speech 3

Note: Ensure all events are scheduled within the 9 AM to 5 PM time frame."""
        else:
            return f"""Create a detailed schedule for the following training program scenario:

Scenario: {t["scenario"]}

Your schedule should include the exact timing for each event, ensuring no overlaps. Submit your schedule as a plain text string in the following format:

Example:
Monday
9:00 AM - 10:00 AM: Team-building Activity
10:00 AM - 12:00 PM: Training Session 1
12:00 PM - 1:00 PM: Lunch Break
1:00 PM - 3:00 PM: Training Session 2
3:00 PM - 4:00 PM: Daily Review Session

Tuesday
9:00 AM - 10:00 AM: Team-building Activity
10:00 AM - 12:00 PM: Training Session 3
12:00 PM - 1:00 PM: Lunch Break
1:00 PM - 3:00 PM: Training Session 4
3:00 PM - 4:00 PM: Daily Review Session

Note: Ensure all events are scheduled within the 9 AM to 5 PM time frame."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The schedule should include all specified events.",
            "The timing of events should be coherent and follow the given constraints.",
            "There should be no overlaps between events.",
            "The schedule should be clearly and logically presented.",
            "All events must be scheduled within the 9 AM to 5 PM time frame."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
