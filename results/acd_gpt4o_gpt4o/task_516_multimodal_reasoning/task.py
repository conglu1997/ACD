class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"image_description": "A photo of a crowded marketplace with numerous stalls selling fruits, vegetables, and other goods. People are seen haggling and purchasing items.", "text": "Describe the scene depicted in the image and explain how it relates to the following text: 'A bustling marketplace with vendors selling various goods.'"},
            "2": {"image_description": "A photograph of the Statue of Liberty, with the American flag waving in the background. Tourists are seen taking pictures and admiring the monument.", "text": "Identify the main subject of the image and describe its significance in the context of the following text: 'A historic monument that stands as a symbol of freedom and resilience.'"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return """Your task is to interpret the given image and text together to provide a comprehensive response. Here are the details:

Image Description: {0}
Text: {1}

Ensure that your response accurately describes the image and explains its relevance to the provided text. Your response should be detailed and should integrate both the visual and textual information. Provide your response in plain text format.""".format(t["image_description"], t["text"])

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should accurately describe the scene depicted in the image.",
            "The response should explain how the scene relates to the provided text.",
            "The response should identify the main subject of the image (if applicable).",
            "The response should describe the significance of the main subject in the context of the provided text (if applicable)."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
