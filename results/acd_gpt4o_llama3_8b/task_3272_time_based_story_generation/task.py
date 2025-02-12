class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "events": [
                    "John wakes up.",
                    "John has breakfast.",
                    "John goes to work.",
                    "John attends a meeting.",
                    "John has lunch with a colleague.",
                    "John completes a project.",
                    "John returns home.",
                    "John has dinner.",
                    "John goes to bed."
                ],
                "task_type": "generate"
            },
            "2": {
                "narrative": "John had dinner after he returned home from completing a project at work. Before the project, he had lunch with a colleague. His day started with waking up, having breakfast, and going to work where he attended a meeting.",
                "task_type": "interpret"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task_type"] == "generate":
            return f"""Generate a coherent narrative based on the following sequence of events. Ensure that the events are logically ordered and the story flows naturally.

Events:
{t['events']}

Submit your narrative as a plain text string in the following format:
'Story: [Your narrative here]'
"""
        elif t["task_type"] == "interpret":
            return f"""Interpret the given narrative and list the events in their correct chronological order. Ensure that the sequence is logically consistent with the narrative.

Narrative:
{t['narrative']}

Submit the chronological sequence as a plain text string in the following format:
'Sequence: [Event 1, Event 2, Event 3, ...]'
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["task_type"] == "generate":
            validation_criteria = ["The narrative should be coherent and logically ordered.", "The story should flow naturally and include all given events in a sensible sequence."]
        elif t["task_type"] == "interpret":
            validation_criteria = ["The sequence should be logically consistent with the narrative.", "All events should be correctly ordered in time."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
