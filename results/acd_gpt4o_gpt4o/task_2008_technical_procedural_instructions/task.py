class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task": "How to install Python on Windows 10"},
            "2": {"task": "How to set up a basic web server using Python's http.server module"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate detailed, step-by-step instructions for performing the following technical task: {t['task']}.

Your instructions should be clear, concise, and easy to follow. Ensure you cover all necessary steps and include any important details or prerequisites. Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The instructions should be clear and concise.",
            "The instructions should cover all necessary steps.",
            "The instructions should include any important details or prerequisites."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
