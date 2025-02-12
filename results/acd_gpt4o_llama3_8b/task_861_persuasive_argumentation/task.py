class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"topic": "The benefits of remote work outweigh the drawbacks."},
            "2": {"topic": "Social media has a more positive than negative impact on society."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following task based on the given topic:

Topic: {t['topic']}

Your task is to generate both a persuasive argument in favor of the topic and a counterargument against it. Each argument should be well-structured and supported by relevant evidence or reasoning. Ensure that your arguments are clear, coherent, and compelling.

Submit your response as a plain text string in the following format:

Argument: [Your argument in favor of the topic]
Counterargument: [Your counterargument against the topic]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The argument should be well-structured and supported by relevant evidence or reasoning.", "The counterargument should also be well-structured and supported by relevant evidence or reasoning.", "Both arguments should be clear, coherent, and compelling."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
