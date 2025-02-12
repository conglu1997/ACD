class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "image_description": "A bustling marketplace with various stalls selling fruits, vegetables, and other goods. People are walking around, some are talking to each other, and a child is holding a balloon.",
                "description": "A bustling marketplace"
            },
            "2": {
                "image_description": "A serene beach with golden sand and clear blue water. A couple is walking hand in hand near the water, and there is a beach umbrella and a towel laid out on the sand.",
                "description": "A serene beach"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to interpret the following visual scene description and generate a detailed description of it.

Image Description: {t['image_description']}

Ensure your description is clear, detailed, and accurately represents the visual elements in the scene. Mention key objects, activities, and the overall ambiance of the scene. Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The description should accurately represent the visual elements in the scene.",
                   "The description should be detailed and mention key objects, activities, and the overall ambiance.",
                   "The language used should be clear and coherent."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
