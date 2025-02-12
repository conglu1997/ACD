class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"initial_event": "A person wakes up in the morning."},
            "2": {"initial_event": "It starts raining heavily."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a logical sequence of events starting from the following initial event: '{t["initial_event"]}'. Ensure that each event logically follows from the previous one, forming a coherent series of events. The sequence should consist of at least five events, each described in a single sentence, and not exceed 200 words. Write the sequence in prose format. Avoid including any unrelated events or logical inconsistencies."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The sequence of events should be logical.",
            "Each event should follow coherently from the previous one.",
            "The sequence should consist of at least five events.",
            "Each event should be described in a single sentence.",
            "The submission should not exceed 200 words.",
            "The sequence should not contain unrelated events or logical inconsistencies."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
