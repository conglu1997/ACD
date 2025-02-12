class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Describe love as a metaphor."},
            "2": {"prompt": "Create an analogy to explain the concept of time."},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a metaphor or analogy based on the following prompt:

Prompt: {t['prompt']}

Provide a clear, coherent, and creative response. The metaphor or analogy should be meaningful and effectively convey the essence of the prompt. Provide your response in plain text format without additional formatting."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should be clear and coherent.", "The response should be creative.", "The response should effectively convey the essence of the prompt."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0