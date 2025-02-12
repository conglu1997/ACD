class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"criteria": "Generate an analogy to explain the concept of photosynthesis to a child. The analogy should be simple, relatable, and help the child understand the basic process."},
            "2": {"criteria": "Create an analogy to describe the workings of a computer's CPU to someone unfamiliar with technology. The analogy should be clear, engaging, and make the concept easier to grasp."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate an analogy based on the given criteria:

Criteria: {t["criteria"]}

Provide a detailed and creative analogy in plain text format. Ensure that your analogy is clear, relatable, and effectively communicates the concept to the target audience."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The analogy should be clear and easy to understand.",
            "The analogy should be creative and engaging.",
            "The analogy should accurately represent the concept being explained.",
            "The analogy should be suitable for the target audience."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
