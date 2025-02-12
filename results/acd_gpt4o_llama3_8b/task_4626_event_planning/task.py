class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "event": "Corporate Workshop",
                "requirements": [
                    "Opening speech by CEO (15 minutes)",
                    "Two 1-hour training sessions with a 30-minute break in between",
                    "Lunch for all participants (1 hour)",
                    "Q&A session at the end (30 minutes)",
                    "Networking session (45 minutes)"
                ],
                "constraints": [
                    "Event must start at 9:00 AM and end by 3:00 PM",
                    "Lunch should be served at 12:00 PM",
                    "Training sessions should not be back-to-back",
                    "Networking session should be before the Q&A session"
                ]
            },
            "2": {
                "event": "Wedding Reception",
                "requirements": [
                    "Welcome drinks (30 minutes)",
                    "Buffet dinner (1.5 hours)",
                    "Speeches by the bride and groom (30 minutes)",
                    "First dance (15 minutes)",
                    "Live band performance (1 hour)",
                    "Cake cutting ceremony (15 minutes)"
                ],
                "constraints": [
                    "Event must start at 6:00 PM and end by 11:00 PM",
                    "Dinner should be served at 7:30 PM",
                    "The live band performance should not start before 9:00 PM",
                    "Cake cutting ceremony should be after the speeches"
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are required to plan a detailed schedule for the following event, considering the given requirements and constraints.

Event: {t['event']}

Requirements:
- {t['requirements'][0]}
- {t['requirements'][1]}
- {t['requirements'][2]}
- {t['requirements'][3]}
- {t['requirements'][4]}

Constraints:
- {t['constraints'][0]}
- {t['constraints'][1]}
- {t['constraints'][2]}
- {t['constraints'][3]}

Submit your schedule as a plain text string in the following format:

[Time] - [Activity]

Example:
9:00 AM - Opening speech by CEO
9:15 AM - Training session 1
10:15 AM - Break
10:45 AM - Training session 2
11:45 AM - Networking session
12:00 PM - Lunch
1:00 PM - Q&A session
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The schedule should meet all given requirements and constraints.",
            "The activities should be logically sequenced and time-allocated appropriately.",
            "The time slots should be clearly specified and cover the entire duration of the event."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
