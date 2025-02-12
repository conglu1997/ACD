class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "Organize a virtual meeting for a project team with members in different time zones.", "outcome": "A schedule and agenda for the meeting."},
            "2": {"scenario": "Plan a small garden with a variety of vegetables.", "outcome": "A planting schedule and layout for the garden."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are provided with the following scenario: {t['scenario']} Your task is to first generate a set of detailed instructions to achieve the specified outcome. Ensure that your instructions are clear and logically sequenced. After generating the instructions, follow them to complete the related task and achieve the outcome: {t['outcome']}. Submit both your instructions and the completed task as a plain text string in the following format:

Instructions:
[Your detailed instructions]

Outcome:
[Your completed task]

Example format:

Instructions:
1. Step one: Describe the first step in detail.
2. Step two: Describe the second step in detail.

Outcome:
1. Result of step one: Describe what was achieved in the first step.
2. Result of step two: Describe what was achieved in the second step.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0
