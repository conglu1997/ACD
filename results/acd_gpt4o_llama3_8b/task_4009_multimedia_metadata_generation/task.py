class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "content_type": "image",
                "content_description": "A vibrant image of a bustling city street at night with neon signs, people walking, and vehicles moving"
            },
            "2": {
                "content_type": "audio",
                "content_description": "A 30-second audio clip of a thunderstorm with rain, thunder, occasional wind, and distant sounds of animals"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate relevant metadata for the following {t['content_type']} content:

Content Description: {t['content_description']}

Your metadata should include the following fields:
1. Title: A concise title for the content.
2. Tags: A list of tags that describe the content (e.g., 'city', 'night', 'neon', 'people', 'vehicles' for an image).
3. Description: A brief description of the content capturing key details.
4. Category: A suitable category for the content (e.g., 'Cityscape', 'Nature', 'Weather').

Submit your metadata as a plain text string in the following format:
- Title: [Your title]
- Tags: [Your tags]
- Description: [Your description]
- Category: [Your category]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The metadata is relevant and coherent.",
            "The tags accurately describe the content.",
            "The description captures key details of the content.",
            "The category is appropriate for the content.",
            "The format for each metadata field is correctly followed."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
