class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"process": "Set up a home Wi-Fi network from scratch."},
            "2": {"process": "Troubleshoot a computer that won't turn on."},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to describe the steps to complete or troubleshoot the following technical process:

{t["process"]}

Make sure your instructions are clear, concise, and easy to follow. Provide each step in a logical order and include any necessary details or precautions. Number or list each step for clarity."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include clear and concise instructions.",
            "The steps should be provided in a logical order.",
            "The response should include any necessary details or precautions.",
            "The steps should be numbered or listed for clarity."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
