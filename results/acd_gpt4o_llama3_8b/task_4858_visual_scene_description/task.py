class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scene_description": "A bustling city street with towering skyscrapers, numerous pedestrians, and a variety of vehicles including cars, buses, and bicycles. Bright billboards and shop signs add to the vibrant atmosphere. A street musician plays a guitar on the sidewalk, while a food vendor serves hot dogs from a cart nearby."
            },
            "2": {
                "scene_description": "A serene beach at sunset with golden sand, gentle waves lapping the shore, and a few seagulls flying overhead. A family builds a sandcastle near the water's edge, while a couple walks hand in hand along the shoreline. In the background, a lighthouse stands tall on a rocky outcrop, its light beginning to shine as the sky turns shades of orange and pink."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Based on the following detailed description of a visual scene, generate a narrative that vividly describes the scene. Your narrative should be engaging, logically structured, and capture all the key elements mentioned in the description. Use rich, descriptive language to bring the scene to life. Do not rely on pre-existing narratives.

Scene Description: {t['scene_description']}

Submit your narrative as a plain text string in the following format:

Narrative:
[Your narrative here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The narrative should be logically structured.",
            "The narrative should capture all key elements mentioned in the description.",
            "The narrative should use rich, descriptive language to bring the scene to life.",
            "The narrative should be original and not rely on pre-existing texts."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0