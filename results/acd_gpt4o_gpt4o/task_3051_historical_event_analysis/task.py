class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "historical_event": "The fall of the Berlin Wall in 1989",
                "contemporary_issue": "The increasing trend of global nationalism"
            },
            "2": {
                "historical_event": "The Great Depression in the 1930s",
                "contemporary_issue": "The 2008 financial crisis"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        historical_event = t["historical_event"]
        contemporary_issue = t["contemporary_issue"]
        instructions = f"""Your task is to analyze the following historical event and draw parallels to the given contemporary issue.

Historical Event: {historical_event}
Contemporary Issue: {contemporary_issue}

Provide a detailed analysis that includes:
1. An overview of the historical event, including its causes, key figures, and consequences.
2. A discussion of the contemporary issue, its context, and key aspects.
3. Parallels between the historical event and the contemporary issue, highlighting similarities and differences.
4. Insights or lessons that can be learned from the historical event and applied to understanding or addressing the contemporary issue.

Your response should be clear, well-structured, and insightful. Provide your analysis in plain text format with the following structure:

- Overview of Historical Event
- Discussion of Contemporary Issue
- Parallels
- Insights or Lessons"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The analysis should include an overview of the historical event.",
            "The analysis should discuss the contemporary issue in its context.",
            "The analysis should draw clear parallels between the historical event and the contemporary issue.",
            "The insights or lessons drawn from the historical event should be relevant and applicable to the contemporary issue."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
