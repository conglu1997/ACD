class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"image_url": "https://via.placeholder.com/300?text=Sunset+over+a+mountain"},
            "2": {"image_url": "https://via.placeholder.com/300?text=Busy+market+scene"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Generate a descriptive narrative based on the given image available at {t['image_url']}. Ensure your description captures the essence of the scene, including details about the setting, characters, actions, and emotions. Your response should be at least 100 words long. Submit your response as a plain text string."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should be a coherent and contextually relevant description of the image.",
            "The response should capture the essence of the scene, including setting, characters, actions, and emotions.",
            "The response should be at least 100 words long."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
