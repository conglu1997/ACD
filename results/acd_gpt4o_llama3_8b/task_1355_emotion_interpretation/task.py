class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"image_url": "https://example.com/real_image1.jpg", "description": "Interpret the emotion displayed by the person in the image and describe it in detail."},
            "2": {"image_url": "https://example.com/real_image2.jpg", "description": "Interpret the emotion displayed by the person in the image and describe it in detail."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Interpret the emotion displayed by the person in the following image and describe it in detail. Provide a detailed description of the facial expression and the emotion it conveys. Here is the image URL: {t['image_url']}\n\n{t['description']}\n\nYour response should follow this format:\n\nEmotion: [The identified emotion]\nDescription: [A detailed description of the facial expression that supports the identified emotion]\n\nFocus on aspects such as the eyes (e.g., are they wide open or squinting?), mouth (e.g., is it smiling, frowning, or neutral?), eyebrows (e.g., are they raised, furrowed, or relaxed?), and overall facial tension (e.g., is the face relaxed or tense?). Ensure your description is clear, logically structured, and demonstrates an understanding of the emotion being conveyed."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The description should accurately identify the emotion being conveyed.", "The description should include specific details about the facial expression, such as the eyes (e.g., are they wide open or squinting?), mouth (e.g., is it smiling, frowning, or neutral?), eyebrows (e.g., are they raised, furrowed, or relaxed?), and overall facial tension (e.g., is the face relaxed or tense?), that support the identified emotion."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
