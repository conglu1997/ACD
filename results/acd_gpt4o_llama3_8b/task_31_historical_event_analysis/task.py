class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "event": "The Fall of the Berlin Wall in 1989."
            },
            "2": {
                "event": "The signing of the Declaration of Independence in 1776."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the following historical event:

{t['event']}

Your analysis should include the causes of the event, its immediate and long-term consequences, and its significance in history. Ensure your response is comprehensive, logically structured, and at least 200 words long. Mention key figures involved and specific dates where relevant. Submit your analysis as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = ["The analysis should be at least 200 words long.", "The analysis should cover the causes, consequences, and significance of the event.", "The analysis should mention key figures involved and specific dates where relevant."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
