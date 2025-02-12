class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"phenomenon": "photosynthesis"},
            "2": {"phenomenon": "the greenhouse effect"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a detailed explanation of the scientific phenomenon '{t["phenomenon"]}'. Your explanation should include the underlying principles and mechanisms, and should be comprehensive enough to educate someone with a basic understanding of science. Ensure your explanation is clear, logically structured, and covers all important aspects of the phenomenon. The explanation should be at least 200 words long. Submit your explanation as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The explanation should include underlying principles and mechanisms.", "The explanation should be at least 200 words long."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
