class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task": "describe", "pattern": "****\n*  *\n*  *\n****"},
            "2": {"task": "generate", "description": "A 5x5 grid with a diagonal cross from the top left corner to the bottom right corner."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task"] == "describe":
            return f"Your task is to describe the following geometric pattern in detail: \n{t['pattern']}\nProvide a clear and detailed description of the pattern, including its shape, size, and any distinctive features."
        elif t["task"] == "generate":
            return f"Your task is to generate a geometric pattern based on the following description: {t['description']}\nProvide the pattern as a string representation, using '*' for filled spaces and ' ' for empty spaces. Each line of the pattern should be separated by a newline character. Ensure that the pattern fits within the specified grid size."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["task"] == "describe":
            criteria = [
                "The description should be clear and detailed.",
                "The description should accurately represent the given pattern, including shape, size, and distinctive features."
            ]
        elif t["task"] == "generate":
            criteria = [
                "The generated pattern should match the given description.",
                "The pattern should be represented using '*' for filled spaces and ' ' for empty spaces.",
                "The pattern should fit within the specified grid size."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
