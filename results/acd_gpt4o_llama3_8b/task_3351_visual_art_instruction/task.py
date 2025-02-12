class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "abstract expressionism", "constraints": "Use primary colors only and include at least three geometric shapes (e.g., circles, squares, triangles)."},
            "2": {"theme": "landscape painting", "constraints": "Depict a sunset scene with a mountain range and a river. Use a warm color palette."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Generate detailed and coherent instructions for creating a visual art piece based on the following theme and constraints: 'Theme: {t['theme']}, Constraints: {t['constraints']}'. Ensure that the instructions are clear enough for an artist to follow and include specific details about colors, shapes, and composition. Submit your instructions as a plain text string."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The instructions should align with the given theme.", "The instructions should adhere to the specified constraints.", "The instructions should be detailed and coherent."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
