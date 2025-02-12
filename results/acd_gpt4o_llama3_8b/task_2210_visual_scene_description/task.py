class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "image_description": "A bustling city street with tall skyscrapers, people walking on the sidewalks, and cars driving by. There's a park in the distance with children playing."
            },
            "2": {
                "image_description": "A serene beach at sunset. The sky is filled with vibrant colors, and the waves are gently crashing onto the shore. There are a few people in the distance, and a lighthouse on a cliff."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Interpret and describe the visual scene based on the provided image description:

Image Description: {t['image_description']}

Your description should include:
1. Details about the main elements in the scene.
2. The spatial relationships between these elements.
3. Any notable features or activities occurring in the scene.
4. A vivid and detailed narrative that accurately reflects the scene described.

Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = ["The description should accurately reflect the main elements of the scene.", "The spatial relationships between elements should be correctly described.", "The response should be vivid and detailed, capturing notable features and activities.", "The description should be logically consistent with the provided image description."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
