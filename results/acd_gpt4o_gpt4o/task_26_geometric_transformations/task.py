class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"shape": "triangle", "transformation": "rotate 90 degrees clockwise"},
            "2": {"shape": "rectangle", "transformation": "translate 5 units to the right and 3 units up"},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        shape = t["shape"]
        transformation = t["transformation"]
        instructions = f"""Your task is to perform the following geometric transformation on the given shape:

Shape: {shape}
Transformation: {transformation}

Describe the resulting shape and its new orientation or position in plain text format. Be precise and clear in your description. Ensure your response includes the exact coordinates or orientation of the transformed shape."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The description should accurately reflect the specified transformation.",
            "The resulting shape should be correctly oriented or positioned according to the transformation.",
            "The response should include exact coordinates or orientation details."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
