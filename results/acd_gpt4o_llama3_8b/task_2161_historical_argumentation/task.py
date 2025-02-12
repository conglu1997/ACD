class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "historical_event": "The signing of the Treaty of Versailles in 1919",
                "task_type": "construct"
            },
            "2": {
                "argument": "The Industrial Revolution had a predominantly positive impact on society.",
                "task_type": "analyze"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task_type"] == "construct":
            return f"""Construct a logical and well-reasoned argument either in favor of or against the following historical event. Make sure to include relevant historical facts, reasoning, and critical thinking to support your stance.

Historical Event:
{t['historical_event']}

Submit your argument as a plain text string in the following format:
'Stance: [In favor/Against]'
'Argument: [Your argument here]'
Ensure that your argument is at least 200 words long."""
        elif t["task_type"] == "analyze":
            return f"""Analyze the following argument. Identify the main points and evaluate the strength of the reasoning and evidence provided. Discuss any potential weaknesses or counterarguments.

Argument:
{t['argument']}

Submit your analysis as a plain text string in the following format:
'Main Points: [The main points of the argument]'
'Strengths: [The strengths of the argument]'
'Weaknesses: [Any weaknesses or potential counterarguments]'
Ensure that your analysis is at least 200 words long."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["task_type"] == "construct":
            validation_criteria = ["The argument must be logical, well-reasoned, and supported by historical facts."]
        elif t["task_type"] == "analyze":
            validation_criteria = ["The analysis must accurately identify the main points, evaluate the strengths and weaknesses, and discuss potential counterarguments."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
