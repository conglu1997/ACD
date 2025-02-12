class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"event": "What if the Roman Empire never fell?"},
            "2": {"event": "What if the Cuban Missile Crisis led to a nuclear war?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to speculate on how the course of history might have been altered if the following event had a different outcome:

Event: {t['event']}

Ensure that your speculation is logically coherent and creatively explores the potential ripple effects of this altered event. Provide your response in plain text format with the following structure:

1. Introduction to the original historical event: Briefly describe the actual historical event as it happened.
2. Speculation on the altered outcome: Clearly state the alternative outcome of the event.
3. Logical reasoning behind the potential ripple effects: Provide detailed reasoning on how this altered event would affect subsequent historical events and societal changes.
4. Creative exploration of the new historical narrative: Develop a creative and coherent alternative history storyline based on the altered event and its ripple effects.

Be thorough in your reasoning and creative in your storytelling."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The introduction should accurately describe the original event.", "The speculation should be logically coherent.", "The exploration should be creative.", "The response should address potential ripple effects.", "The narrative should be historically plausible based on the altered event."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
