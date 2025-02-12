class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {'image': TaskFamily.generate_sample_image_1(), 'prompt': 'Create a short story based on this image.'},
            '2': {'image': TaskFamily.generate_sample_image_2(), 'prompt': 'Create a short story based on this image.'}
        }

    @staticmethod
    def generate_sample_image_1() -> str:
        from PIL import Image, ImageDraw, ImageFont
        import base64
        from io import BytesIO
        # Create a simple image for the task
        img = Image.new('RGB', (200, 200), color = (73, 109, 137))
        d = ImageDraw.Draw(img)
        d.text((10, 10), 'A sunny day in the park', fill=(255, 255, 0))
        buffered = BytesIO()
        img.save(buffered, format='PNG')
        img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
        return img_str

    @staticmethod
    def generate_sample_image_2() -> str:
        from PIL import Image, ImageDraw, ImageFont
        import base64
        from io import BytesIO
        # Create another simple image for the task
        img = Image.new('RGB', (200, 200), color = (193, 66, 66))
        d = ImageDraw.Draw(img)
        d.text((10, 10), 'A mysterious forest', fill=(255, 255, 255))
        buffered = BytesIO()
        img.save(buffered, format='PNG')
        img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
        return img_str

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a coherent and engaging short story based on the provided image.

Prompt: {t['prompt']}

Image (base64-encoded): {t['image']}

Ensure that your story is creative, well-structured, and aligns with the visual elements of the image. Provide your response in plain text format with clear sections that outline your story:
1. Introduction: [Introduce the characters and setting]
2. Plot: [Develop the story with a clear sequence of events]
3. Conclusion: [Conclude the story in a satisfying manner]

Remember to create a story that is both engaging and coherent, making sure to closely align the narrative with the visual elements present in the image. Be sure to elaborate on how the visual elements influence the story."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The story should be coherent and engaging.", "The story should align with the visual elements of the image.", "The story should have a clear introduction, plot, and conclusion.", "The story should elaborate on how the visual elements influence the narrative."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
