class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "historical_event": "The signing of the Declaration of Independence in 1776.",
                "task_type": "create"
            },
            "2": {
                "scenario": "In 1941, the United States did not enter World War II after the attack on Pearl Harbor.",
                "task_type": "analyze"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task_type"] == "create":
            return f"""Based on the following historical event, create a plausible alternative historical scenario. Your scenario should be detailed, logically consistent, and consider the historical context of the event. Additionally, explain the reasoning behind your scenario and the potential implications it might have had on subsequent history.

Historical Event:
{t['historical_event']}

Submit your scenario and reasoning as a plain text string in the following format:

Scenario: [Your scenario]
Reasoning: [Your reasoning]"""
        elif t["task_type"] == "analyze":
            return f"""Analyze the following alternative historical scenario. Your analysis should include the potential outcomes, the impact on historical events, and the reasoning behind your analysis. Consider both short-term and long-term implications of the scenario. Discuss at least two different perspectives or potential outcomes.

Scenario:
{t['scenario']}

Submit your analysis as a plain text string in the following format:

Analysis: [Your analysis]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["task_type"] == "create":
            validation_criteria = ["The scenario should be plausible and logically consistent.", "The reasoning should explain the historical context and potential implications."]
        elif t["task_type"] == "analyze":
            validation_criteria = ["The analysis should include potential outcomes and impacts on historical events.", "The reasoning should be logical and well-supported.", "The analysis should discuss at least two different perspectives or potential outcomes."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
