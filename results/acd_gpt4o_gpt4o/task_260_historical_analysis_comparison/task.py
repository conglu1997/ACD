class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "event1": "The French Revolution",
                "event2": "The American Revolution"
            },
            "2": {
                "event1": "The Great Depression",
                "event2": "The 2008 Financial Crisis"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze and compare the following historical events:

Event 1: {t['event1']}
Event 2: {t['event2']}

Your analysis should include the following elements:
1. A brief summary of each event.
2. The main causes of each event.
3. The key outcomes and impacts of each event.
4. Similarities and differences between the two events.

Submit your analysis in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The analysis should include a brief summary of each event.",
            "The analysis should include the main causes of each event.",
            "The analysis should include the key outcomes and impacts of each event.",
            "The analysis should identify similarities and differences between the two events."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0