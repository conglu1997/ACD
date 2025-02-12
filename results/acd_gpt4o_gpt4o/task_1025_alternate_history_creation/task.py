class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"event": "The Roman Empire never fell.", "timeframe": "from 476 AD to the present"},
            "2": {"event": "The American Revolution failed.", "timeframe": "from 1776 to the present"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to create a detailed alternate historical timeline based on the following change in a historical event:

Event: {t['event']}
Timeframe: {t['timeframe']}

Please include the following elements in your alternate history:

1. Key Events: Describe at least five major events that occur as a result of the change.
2. Social Impact: Explain how society, culture, and daily life are affected by the change.
3. Technological Development: Discuss how technology advances or regresses in this alternate timeline.
4. Political Landscape: Describe the political entities and relationships that exist in this new history.
5. Comparison: Compare the alternate timeline to our actual history, highlighting key differences.

Ensure that your alternate history is internally consistent, logically plausible, and rich in detail."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The alternate history should include all required elements (key events, social impact, technological development, political landscape, comparison).",
                    "The timeline should be internally consistent and logically plausible.",
                    "The description should be rich in detail and demonstrate a thorough understanding of historical context.",
                    "The comparison should clearly highlight key differences between the alternate timeline and actual history."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
