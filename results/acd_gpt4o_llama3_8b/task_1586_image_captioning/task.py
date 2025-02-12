class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"image_description": "A beautiful sunset over the mountains with a river flowing through the valley. The sky is painted with hues of orange and pink, and there are silhouettes of birds flying."},
            "2": {"image_description": "A busy market street with vendors selling fruits and vegetables. People are walking around, some carrying shopping bags, while a street musician plays a guitar in the background."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a caption for the following image description. Ensure that the caption is coherent with the description and captures the essence of the scene.

{t['image_description']}

Submit your response as a plain text string in the following format: 'Caption: [Your caption]'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The caption should be coherent with the image description.", "The caption should capture the essence of the scene."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
