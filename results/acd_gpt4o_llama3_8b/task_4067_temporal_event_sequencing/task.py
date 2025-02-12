class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "constraints": "Create a sequence of events for a typical school day. The sequence should start at 8:00 AM and end at 3:00 PM. Include at least 5 distinct events, and ensure that they are logically ordered and temporally coherent."
            },
            "2": {
                "constraints": "Create a sequence of events for a birthday party. The sequence should start at 2:00 PM and end at 7:00 PM. Include at least 5 distinct events, and ensure that they are logically ordered and temporally coherent."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a sequence of events based on the given constraints: {t["constraints"]}. Ensure the sequence is properly formatted and includes all required events. Here is an example of the expected format:

Example for a school day sequence of events:

1. 8:00 AM - Students arrive at school.
2. 8:30 AM - Morning assembly.
3. 9:00 AM - First class begins.
4. 12:00 PM - Lunch break.
5. 3:00 PM - School day ends.

Example for a birthday party sequence of events:

1. 2:00 PM - Guests arrive.
2. 2:30 PM - Games and activities.
3. 4:00 PM - Cake cutting.
4. 5:00 PM - Gift opening.
5. 7:00 PM - Party ends.

Ensure that the events are clearly separated and well-formatted. The events should be sequential and temporally coherent."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The events should be sequential and temporally coherent.",
            "The sequence should include at least 5 distinct events.",
            "The events should logically follow the given temporal constraints."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
