class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "art_description": "A serene landscape painting depicting a sunset over a calm lake, with mountains in the background and a small boat gently floating on the water. The sky is a gradient of warm colors, transitioning from orange to pink to purple as the sun sets. The reflection of the mountains and the boat can be seen in the still water, creating a mirror-like effect."
            },
            "2": {
                "art_description": "A vibrant abstract painting filled with swirling colors and geometric shapes, evoking a sense of chaos and energy. The colors range from bright reds and yellows to deep blues and greens, all blending and clashing with each other. Some shapes are sharp and angular, while others are smooth and curved, creating a dynamic and lively composition."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Describe the following piece of visual art based on the given description:

{t['art_description']}

Your description should be vivid and detailed, capturing the essence of the artwork. Ensure that your description is at least 100 words long and provides a clear visual representation of the art. Submit your description as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The description should be vivid and detailed.",
            "The description should capture the essence of the artwork.",
            "The description should be at least 100 words long."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
