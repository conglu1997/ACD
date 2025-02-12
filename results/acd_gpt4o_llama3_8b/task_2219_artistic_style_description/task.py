class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task_type": "image_to_description", "image": "https://example.com/art1.jpg"},
            "2": {"task_type": "description_to_style", "description": "A painting with bold, swirling colors and thick brush strokes, often depicting intense emotion and movement. This style often focuses on the inner experiences and emotions of the subject, rather than realistic representation."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task_type"] == "image_to_description":
            return f"""Given the following image, provide a detailed description of the artistic style. Include elements such as color usage, brush strokes, subject matter, and any notable techniques or characteristics. The image can be found at the following URL (note: this is a placeholder URL):
{t['image']}
Submit your description as a plain text string."""
        elif t["task_type"] == "description_to_style":
            return f"""Given the following description, identify the artistic style being described. Provide a name for the style and a brief explanation of your reasoning based on the elements mentioned in the description:
{t['description']}
Submit your response as a plain text string in the following format:
Style: [Name of the style]
Explanation: [Brief explanation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["task_type"] == "image_to_description":
            criteria = [
                "The description should accurately reflect the visual elements of the image.",
                "The description should include details about color usage, brush strokes, and subject matter.",
                "The description should mention any notable techniques or characteristics."]
        elif t["task_type"] == "description_to_style":
            criteria = [
                "The identified style should logically match the description provided.",
                "The explanation should reference elements mentioned in the description."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
