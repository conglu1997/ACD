class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "freedom"},
            "2": {"theme": "unity"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to create a piece of symbolic art that represents the following theme:\n\n{t['theme']}\n\nYour art should be described in detail, including the symbols used and their meanings. Ensure that your description is clear and conveys how the art represents the given theme. Submit your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The description should clearly explain the symbolic art.",
            "The symbols used should be relevant and coherent with the theme.",
            "The description should convincingly convey how the art represents the given theme.",
            "The submission should be well-structured and logically coherent."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
