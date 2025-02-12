class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "topic": "The benefits of remote work outweigh the drawbacks."
            },
            "2": {
                "arguments": [
                    "Argument 1: Remote work leads to decreased productivity due to numerous distractions at home.",
                    "Argument 2: Remote work allows for better work-life balance, leading to increased job satisfaction and retention."
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "topic" in t:
            return f"""Generate a persuasive argument for the following topic:

{t['topic']}

Ensure your argument is well-structured, logically sound, and persuasive. Your response should be at least 150 words. Submit your argument as a plain text string."""
        else:
            return """Evaluate the following arguments for their strength and persuasiveness:

Argument 1: Remote work leads to decreased productivity due to numerous distractions at home.

Argument 2: Remote work allows for better work-life balance, leading to increased job satisfaction and retention.

Provide your evaluation of each argument, discussing their strengths, weaknesses, and overall persuasiveness. Then, indicate which argument you find more persuasive and why. Submit your evaluation as a plain text string in the following format:

Evaluation of Argument 1:
[Your evaluation here]

Evaluation of Argument 2:
[Your evaluation here]

Most Persuasive Argument: [Argument 1 or Argument 2]
Reasoning: [Your reasoning here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'topic' in t:
            validation_criteria = [
                "The argument should be well-structured and logically sound.",
                "The argument should be at least 150 words.",
                "The argument should be persuasive and relevant to the topic."]
        else:
            validation_criteria = [
                "The strengths and weaknesses of each argument should be clearly discussed.",
                "The final choice of the most persuasive argument should be justified with clear reasoning.",
                "The evaluation should be presented in the specified format."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
