class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"project": "Build a simple birdhouse"},
            "2": {"project": "Create a homemade lava lamp"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate detailed, step-by-step instructions for the following DIY project. Ensure that your instructions are clear, accurate, and easy to follow. Additionally, explain the rationale behind each step to help the reader understand why it is necessary.

DIY Project: {t['project']}

Your response should include:
1. A list of required materials and tools.
2. Detailed, step-by-step instructions.
3. An explanation of the rationale behind each step.

Ensure that the explanations for each step are detailed and that the steps are logically ordered.

Provide your instructions and explanations in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The instructions should be clear and detailed.", "The rationale behind each step should be explained.", "The steps should be logically ordered."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
