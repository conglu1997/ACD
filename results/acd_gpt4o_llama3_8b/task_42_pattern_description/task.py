class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"pattern": "A large square with a smaller square inside it, centered within the larger square."},
            "2": {"pattern": "An equilateral triangle with a circle inscribed within it, the circle touching all three sides."},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Describe the following geometric pattern in detail: {t["pattern"]}

Your description should be comprehensive and cover all aspects of the pattern. Use clear and precise language to ensure the pattern can be easily visualized based on your description. The description should be at least 30 words long."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The description should accurately represent the given geometric pattern.", "The description should be clear, precise, and comprehensive.", "The description should be at least 30 words long."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
