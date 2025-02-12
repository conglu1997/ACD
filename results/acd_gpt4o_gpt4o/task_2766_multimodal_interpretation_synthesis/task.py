class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"image_description": "A busy market scene with various stalls, people shopping, and vibrant colors.", "context": "The market is bustling with activity during the day."},
            "2": {"image_description": "A serene beach with gentle waves, golden sand, and a beautiful sunset.", "context": "The beach is peaceful at sunset with a calm atmosphere."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to interpret the given image description and synthesize a coherent and engaging description or story based on it. Ensure that your description accurately reflects the visual details and context provided.

Image Description: {t['image_description']}
Context: {t['context']}

Your response should include:
1. A detailed and accurate description of the image, incorporating the visual elements and context.
2. A coherent narrative or story that relates to the image and context provided.

Ensure your description is engaging and well-written, making the reader visualize the scene clearly."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The description should accurately reflect the visual elements of the image description.",
            "The description should incorporate the provided context.",
            "The narrative or story should be coherent and engaging.",
            "The response should be well-written and make the reader visualize the scene clearly."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
