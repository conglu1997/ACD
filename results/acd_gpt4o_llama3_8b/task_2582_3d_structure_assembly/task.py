class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"parts": ["cube", "cylinder", "cone", "pyramid"], "goal_structure": "cylinder on top of cube, cone on top of cylinder, pyramid on top of cone"},
            "2": {"parts": ["sphere", "rectangular prism", "triangular prism", "cylinder"], "goal_structure": "rectangular prism on the ground, sphere on top of rectangular prism, triangular prism leaning against sphere, cylinder on top of triangular prism"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        parts = ', '.join(t["parts"])
        goal_structure = t["goal_structure"]
        return f"""Given the following parts: {parts}, describe in detail the steps to assemble the goal structure: {goal_structure}. Ensure your instructions are clear and logical, and that they describe how to position each part relative to the others.

Submit your response as a plain text string with each step clearly numbered."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The steps should be clear and logical.",
            "The steps should accurately describe how to assemble the given parts into the goal structure.",
            "The order and spatial relationships of the parts should be correct.",
            "The response should follow the provided format."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
