class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "task_type": "summary",
                "event": "The signing of the Declaration of Independence in 1776"
            },
            "2": {
                "task_type": "diary_entry",
                "figure": "Thomas Jefferson",
                "event": "The drafting of the Declaration of Independence"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task_type'] == 'summary':
            return f"""Summarize the following historical event in a coherent and concise manner:

Event: {t['event']}

Ensure your summary captures the key points, context, and significance of the event. Your summary should be between 150-200 words. Submit your summary as a plain text string."""
        else:
            return f"""Generate a fictional diary entry from the perspective of the following historical figure involved in the given event:

Figure: {t['figure']}
Event: {t['event']}

Ensure the diary entry captures the figure's thoughts, emotions, and perspective on the event. The entry should be between 200-300 words and written in a style appropriate for the historical period. Submit your diary entry as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['task_type'] == 'summary':
            validation_criteria = [
                "The summary should accurately capture the key points and significance of the event.",
                "The summary should be coherent, concise, and within the word limit.",
                "The summary should not contain any factual inaccuracies."
            ]
        else:
            validation_criteria = [
                "The diary entry should capture the thoughts, emotions, and perspective of the historical figure.",
                "The diary entry should be coherent, within the word limit, and written in an appropriate style for the historical period.",
                "The diary entry should not contain any anachronisms or factual inaccuracies."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
