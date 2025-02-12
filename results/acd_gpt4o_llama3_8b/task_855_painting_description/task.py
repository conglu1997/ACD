class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "painting_name": "Starry Night",
                "context": "This painting by Vincent van Gogh depicts a night sky filled with swirling clouds and bright stars, with a small town below."
            },
            "2": {
                "criteria": "Imagine a painting that depicts a futuristic cityscape at night. Describe the scene in detail, including the buildings, the sky, the streets, and any people or vehicles present."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'painting_name' in t:
            return f"""Describe the following famous painting in detail based on the provided context:

Painting Name: {t['painting_name']}
Context: {t['context']}

Ensure that your description includes visual elements, the painting's style, and any notable features. Submit your response as a plain text string in the format:

Description:
[Your description]"""
        elif 'criteria' in t:
            return f"""Generate a detailed description of an imaginary painting based on the following criteria:

Criteria: {t['criteria']}

Ensure that your description is vivid, creative, and captures the essence of the scene. Avoid plagiarism and ensure originality. Submit your response as a plain text string in the format:

Description:
[Your description]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'painting_name' in t:
            criteria = ["The description should include visual elements of the painting.", "The description should capture the painting's style and notable features."]
        else:
            criteria = ["The description should be vivid and creative.", "The description should capture the essence of the scene.", "The description should be original and avoid plagiarism."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
