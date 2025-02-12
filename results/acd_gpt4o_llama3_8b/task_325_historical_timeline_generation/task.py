class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "topic": "American Civil War",
                "start_year": 1860,
                "end_year": 1865
            },
            "2": {
                "topic": "Industrial Revolution",
                "start_year": 1760,
                "end_year": 1840
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a chronological timeline of key events related to the given historical topic.

Topic: {t['topic']}
Timeframe: {t['start_year']} to {t['end_year']}

Ensure that your timeline includes at least 5 significant events. Each event should be described in one or two sentences and should include the year it occurred. Submit your timeline as a plain text string in the following format:

[Year]: [Event description]
[Year]: [Event description]
..."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The timeline should include at least 5 significant events.",
            "Each event should be described in one or two sentences.",
            "Each event should include the year it occurred.",
            "The events should be relevant to the given topic and within the specified timeframe.",
            "The events should be in chronological order."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
