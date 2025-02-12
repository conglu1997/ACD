class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "event_sequence": "John woke up, had breakfast, went to work, attended a meeting, had lunch, finished work, went to the gym, had dinner, went to bed.",
                "task_type": "interpret"
            },
            "2": {
                "description": "A person starts their day with a workout, goes to the office, attends a team meeting, works on a project, has lunch with a colleague, continues working until evening, goes home, prepares dinner, watches a movie, and then has dinner again before going to sleep.",
                "task_type": "generate"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task_type"] == "interpret":
            return f"""Interpret the following sequence of events and identify the key temporal relationships. Provide a detailed description of the sequence, highlighting the order and timing of events. Your interpretation should be clear and logically organized.

Event Sequence:
{t['event_sequence']}

Submit your interpretation as a plain text string in the following format:
'Temporal Relationships: [Your interpretation here]'"""
        elif t["task_type"] == "generate":
            return f"""Generate a detailed sequence of events based on the following description. Ensure that the sequence captures all key temporal relationships and events as described. Your sequence should be clear and logically ordered.

Description:
{t['description']}

Submit your sequence as a plain text string in the following format:
'Event Sequence: [Your sequence here]'"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["task_type"] == "interpret":
            validation_criteria = ["The interpretation should accurately capture the order and timing of events in the sequence.", "The interpretation should be coherent and logically organized."]
        elif t["task_type"] == "generate":
            validation_criteria = ["The generated sequence should accurately reflect the described events and their temporal relationships.", "The sequence should be clear and logically ordered."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
