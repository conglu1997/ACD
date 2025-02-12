class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"image_criteria": "Imagine a surreal landscape featuring a floating island, a giant clock, and an unusual sky. Describe this scene in vivid detail, focusing on colors, shapes, and the overall atmosphere."},
            "2": {"description": "A painting depicts a bustling city street at night with neon lights reflecting off wet pavement. People with umbrellas walk briskly, while cars pass by. The style is reminiscent of impressionism with bold brush strokes and vibrant colors."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'image_criteria' in t:
            return f"""Generate a detailed description of an image based on the given artistic criteria. Focus on vivid details, including colors, shapes, and the overall atmosphere. Ensure that your description is creative and paints a clear picture of the scene.

Artistic Criteria:
{t['image_criteria']}

Submit your description as a plain text string in the following format:

Description: [Your description here]"""
        else:
            return f"""Interpret the following description of a painting. Discuss the artistic style, the emotions it evokes, and any notable elements. Provide a detailed interpretation that includes references to known artistic styles or movements if applicable. Your interpretation should demonstrate a deep understanding of art and its various forms.

Description:
{t['description']}

Submit your interpretation as a plain text string in the following format:

Interpretation: [Your interpretation here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'image_criteria' in t:
            criteria = [
                "The description should be vivid and detailed.",
                "The description should include colors, shapes, and the overall atmosphere.",
                "The description should be creative and paint a clear picture of the scene."
            ]
        else:
            criteria = [
                "The interpretation should discuss the artistic style and emotions evoked.",
                "The interpretation should reference known artistic styles or movements if applicable.",
                "The interpretation should demonstrate a deep understanding of art and its various forms.",
                "The interpretation should be detailed and thorough."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
