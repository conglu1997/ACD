class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Generate a timeline for a day in the life of a high school student, from waking up to going to bed."},
            "2": {"prompt": "Generate a timeline for the key events in the life of an astronaut from training to returning to Earth after a space mission."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a coherent and logically consistent timeline of events based on the following prompt:

{t['prompt']}

The timeline should include at least five key events and should be presented in chronological order. Each event should be described in one or two sentences. Ensure that the timeline is logically consistent and follows a natural progression of events. Provide your response in plain text format with each event on a new line labeled 'Event 1', 'Event 2', and so on."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The timeline should include at least five key events.", "The events should be presented in chronological order.", "The timeline should be logically consistent and follow a natural progression of events."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
