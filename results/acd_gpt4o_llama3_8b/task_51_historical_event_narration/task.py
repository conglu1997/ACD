class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"event": "The Fall of the Berlin Wall", "year": 1989},
            "2": {"event": "The Moon Landing", "year": 1969}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a detailed narrative based on the following historical event: '{t["event"]}' which occurred in the year {t["year"]}. The narrative should include the following:
1. Key events leading up to the historical event
2. Main figures involved
3. Chronological order of events
4. Causes of the event
5. Consequences of the event, particularly its impact on society
6. Aftermath and long-term effects

Ensure that the narrative is historically accurate, logically coherent, well-structured, and engaging. Submit your narrative as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The narrative should be historically accurate.", "The narrative should be coherent and engaging.", "The narrative should follow the chronological order of events.", "The narrative should describe the causes and consequences of the event.", "The narrative should address the aftermath and long-term effects."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
