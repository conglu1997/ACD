class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"event": "The signing of the Declaration of Independence in 1776.", "figure": "Thomas Jefferson"},
            "2": {"event": "The construction of the Great Wall of China during the Qin Dynasty.", "figure": "Emperor Qin Shi Huang"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to create a short historical fiction story based on the following historical event. Ensure that your story is historically accurate and engaging.

Historical Event: {t['event']}
Historical Figure: {t['figure']}

Your story should include:
1. A clear setting that reflects the historical period.
2. Characters that could have plausibly existed during the time, including the mentioned historical figure.
3. A plot that is engaging, coherent, and includes conflict and resolution.
4. Accurate historical details and context.
5. A narrative that incorporates the mentioned historical figure in a meaningful way.

Provide your story in plain text format. Ensure your narrative is between 300-500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The story should include a clear setting that reflects the historical period.",
            "The characters should be plausible for the historical time, including the mentioned historical figure.",
            "The plot should be engaging, coherent, and include conflict and resolution.",
            "The story should include accurate historical details and context.",
            "The narrative should be between 300-500 words.",
            "The historical figure should be incorporated in a meaningful way."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
