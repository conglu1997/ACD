class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"pattern": "A star with five points"},
            "2": {"pattern": "A hexagon inside a circle"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        pattern = t["pattern"]
        instructions = f"""Your task is to describe in detail how to draw the following geometric pattern step by step:

Pattern: {pattern}

Your instructions should be clear, precise, and easy to follow. Ensure that each step is detailed enough for someone to replicate the pattern accurately. Focus on providing clear and unambiguous instructions. Provide your instructions in plain text format. Your response should be structured as follows:

Instructions: [Your detailed step-by-step instructions]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The instructions should be clear and precise.",
            "The instructions should allow someone to replicate the pattern accurately.",
            "The instructions should be detailed and easy to follow."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
