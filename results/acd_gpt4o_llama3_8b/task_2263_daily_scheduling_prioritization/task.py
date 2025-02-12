class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "tasks": [
                    {"name": "Meeting with manager", "duration": "1 hour", "priority": "high", "time_window": "09:00-17:00"},
                    {"name": "Lunch", "duration": "1 hour", "priority": "medium", "time_window": "12:00-14:00"},
                    {"name": "Project work", "duration": "3 hours", "priority": "high", "time_window": "09:00-17:00"},
                    {"name": "Gym", "duration": "1 hour", "priority": "low", "time_window": "17:00-20:00"},
                    {"name": "Emails", "duration": "30 minutes", "priority": "medium", "time_window": "09:00-17:00"},
                    {"name": "Call with client", "duration": "45 minutes", "priority": "high", "time_window": "10:00-11:00"}
                ],
                "constraints": {"work_hours": "09:00-17:00", "break_time": "12:00-13:00"}
            },
            "2": {
                "tasks": [
                    {"name": "Client presentation", "duration": "2 hours", "priority": "high", "time_window": "09:00-12:00"},
                    {"name": "Team meeting", "duration": "1 hour", "priority": "medium", "time_window": "13:00-15:00"},
                    {"name": "Report writing", "duration": "3 hours", "priority": "high", "time_window": "12:00-18:00"},
                    {"name": "Dinner with family", "duration": "2 hours", "priority": "high", "time_window": "18:00-20:00"},
                    {"name": "Exercise", "duration": "1 hour", "priority": "low", "time_window": "06:00-08:00"},
                    {"name": "Code review", "duration": "1.5 hours", "priority": "medium", "time_window": "15:00-17:00"}
                ],
                "constraints": {"work_hours": "09:00-18:00", "lunch_break": "12:00-13:00"}
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a daily schedule based on the given tasks, priorities, and constraints.

Tasks: {t['tasks']}

Constraints: {t['constraints']}

Your response should include:
1. A detailed schedule that includes all the tasks within the given time windows and constraints.
2. A brief explanation of why you prioritized tasks as you did.

Example response format:
- Schedule: [Your detailed schedule here]
- Explanation: [Your explanation here]

Ensure your schedule is practical, adheres to the given constraints, and clearly prioritizes higher priority tasks. Avoid any time conflicts in your schedule. Submit your response as a plain text string. Use the 24-hour time format for the schedule."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The schedule should include all given tasks.",
            "The schedule should adhere to the given constraints.",
            "Higher priority tasks should be prioritized appropriately.",
            "There should be no time conflicts in the schedule.",
            "The time format should be consistent and in 24-hour format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
