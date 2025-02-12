class TaskFamily:
    import base64
    from io import BytesIO
    from PIL import Image, ImageDraw

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "image_description": "A modern abstract painting with vibrant colors and dynamic forms.",
                "image": "iVBORw0KGgoAAAANSUhEUgAAAAUA\nAAAAFCAYAAACNbyblAAAAHElEQVQI12P4\n9wCFgYGBgWQAiIjX/4x0AKDIQc4HAAAAAElFTkSuQmCC"
            },
            "2": {
                "image_description": "A classical landscape painting depicting a serene countryside scene.",
                "image": "iVBORw0KGgoAAAANSUhEUgAAAAUA\nAAAAFCAYAAACNbyblAAAAHElEQVQI12P4\n9wCFgYGBgWQAiIjX/4x0AKDIQc4HAAAAAElFTkSuQmCC"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Interpret and describe the following artwork based on its visual elements and style:

Image: {t['image_description']}

Your description should include the following sections and be detailed and thorough:
1. Visual Elements: Describe the colors, shapes, forms, and overall composition of the artwork.
2. Style: Identify the artistic style or movement the artwork belongs to and explain its characteristics.
3. Interpretation: Provide a possible interpretation of the artwork's meaning or message.

Submit your response as a plain text string in the following format:

Visual Elements: [Your description]
Style: [Your identification and explanation]
Interpretation: [Your interpretation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The description should accurately reflect the visual elements of the artwork.",
            "The explanation of the style should be relevant and well-argued.",
            "The interpretation should be coherent and plausible based on the visual elements.",
            "The response should be detailed and comprehensive."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
