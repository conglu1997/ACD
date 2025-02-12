class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "emotion": "joy",
                "provided_narrative": "As the sun set over the horizon, Sarah felt a wave of happiness wash over her. The day's events had gone perfectly, and she was surrounded by the people she loved most."
            },
            "2": {
                "emotion": "sadness",
                "provided_narrative": "John sat alone in his room, staring at the photo of his late grandmother. Memories of her filled his mind, and a deep sense of loss settled in his heart."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task involves two parts: first, generate a narrative based on the given emotional prompt, and second, analyze the emotional content of the provided narrative.\n\nEmotion: {t['emotion']}\n\nGuidelines for the Narrative Generation:\n1. The narrative should evoke the given emotion.\n2. Ensure the narrative is coherent and engaging.\n3. Keep the narrative appropriate for a general audience.\n\nResponse Format:\nGenerated Narrative: [Your narrative]\n\nProvided Narrative: {t['provided_narrative']}\n\nGuidelines for the Analysis:\n1. Identify the key elements that contribute to the emotional content of the provided narrative.\n2. Explain why the narrative evokes the given emotion, considering language, context, and character actions.\n3. Provide your response in plain text format.\n\nResponse Format:\nGenerated Narrative: [Your narrative]\nAnalysis: [Your analysis]\n\nExample Response:\nGenerated Narrative:\n  As the first snowflakes fell, children ran outside with glee, building snowmen and laughing together. The air was filled with the sound of joy and excitement.\n\nAnalysis:\n  The narrative evokes joy through the depiction of children playing and the cheerful atmosphere created by the first snowfall. The use of words like 'glee' and 'laughing' reinforces the happy emotion."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The generated narrative evokes the given emotion.",
            "The narrative is coherent and engaging.",
            "The analysis correctly identifies the key elements contributing to the emotional content.",
            "The analysis provides a clear and logical explanation of why the narrative evokes the given emotion."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
