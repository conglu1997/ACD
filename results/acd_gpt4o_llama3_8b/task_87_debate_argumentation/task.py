class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"topic": "Should social media platforms be regulated by the government?"},
            "2": {"topic": "Is universal basic income a viable solution to economic inequality?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following task based on the given topic:

Debate Topic: {t['topic']}

Generate persuasive arguments for both sides of the debate. Your response should include:
1. A clear and concise argument in favor of the topic, with at least two supporting points.
2. A clear and concise argument against the topic, with at least two supporting points.

Each argument should be well-reasoned, logically structured, and supported by relevant examples or evidence. Ensure that each argument is coherent and persuasive.

Submit your response as a plain text string with clearly labeled sections for 'Argument For' and 'Argument Against'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should include a clear and concise argument in favor of the topic, with at least two supporting points.", "The response should include a clear and concise argument against the topic, with at least two supporting points.", "Each argument should be well-reasoned, logically structured, and supported by relevant examples or evidence.", "Each argument should be coherent and persuasive."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
