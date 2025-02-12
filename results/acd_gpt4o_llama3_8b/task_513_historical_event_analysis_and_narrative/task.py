class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "event": "The signing of the Declaration of Independence on July 4, 1776.",
                "context": "The French Revolution in 1789."
            },
            "2": {
                "event": "The fall of the Berlin Wall on November 9, 1989.",
                "context": "The end of the Roman Empire in 476 AD."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following tasks:

1. Analyze the given historical event: {t['event']}. Provide a detailed analysis that includes the causes, key figures involved, major outcomes, and its impact on subsequent history.

2. Generate a narrative based on the given historical context: {t['context']}. Imagine how the given historical event might have unfolded differently if it had occurred in this context. Ensure the narrative is coherent, historically plausible, and captures the essence of the new context.

Submit your response as a plain text string in the following format:

Historical Event Analysis:
[Your analysis]

Alternative Historical Narrative:
[Your narrative]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The historical event analysis should be detailed, accurate, and cover causes, key figures, outcomes, and impact.",
            "The alternative historical narrative should be coherent, historically plausible, and capture the essence of the new context.",
            "The submission should be well-organized and clearly written."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
