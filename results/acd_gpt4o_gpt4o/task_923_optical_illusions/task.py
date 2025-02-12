class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"illusion": "Penrose Stairs", "description": "The Penrose Stairs, also known as the Impossible Staircase, is an optical illusion created by Lionel Penrose and his son Roger Penrose. It depicts a staircase that appears to ascend or descend endlessly in a loop."},
            "2": {"illusion": "Café Wall Illusion", "description": "The Café Wall Illusion is an optical illusion where the parallel horizontal lines between staggered rows of black and white tiles appear to be sloped. This illusion was first described by Richard Gregory."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to describe the given optical illusion and explain the underlying principles that make it work. Ensure that your description is clear, detailed, and includes an explanation of why the illusion occurs. Provide your response in plain text format.\n\nOptical Illusion: {t['illusion']}\nDescription: {t['description']}\n\nResponse format:\n1. Description: [Your detailed description of the illusion]\n2. Explanation: [Explanation of the underlying principles]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The description should be clear and detailed.", "The explanation should accurately describe the underlying principles of the optical illusion."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
