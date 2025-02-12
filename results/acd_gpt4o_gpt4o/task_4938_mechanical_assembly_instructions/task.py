class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"parts": ["a base plate with 4 holes", "4 screws", "a motor", "a small fan blade", "a battery pack", "2 wires"]},
            "2": {"parts": ["a wooden frame", "4 nails", "a hammer", "a small mirror", "a glue stick", "2 hinges"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        parts = ', '.join(t['parts'])
        return f"""Your task is to provide step-by-step assembly instructions for a simple mechanical object using the following parts: {parts}.

Ensure that your instructions are:
1. Clear and logical.
2. Detailed in describing how each part should be used.
3. Sequential, ensuring each step follows logically from the previous one.
4. Precise in describing any necessary spatial relationships and orientations of the parts.
5. Comprehensive to result in a functional mechanical object.

Provide your response in plain text format with each step numbered.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The instructions should be clear and logical.", "The sequence of steps should be correct.", "The spatial relationships and orientations should be clearly described.", "The assembly should result in a functional mechanical object.", "Each step should follow logically from the previous one."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
