class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "Describe the following visual scene: A busy city street with tall buildings, various shops, and people walking on the sidewalks. Include details about the weather, time of day, and any notable activities. Your description should be at least 150 words long."},
            "2": {"description": "Generate a visual scene based on the following description: A serene beach at sunset with calm waves, a few scattered seashells on the sand, and a couple holding hands walking along the water's edge. Include details about the colors in the sky and any other elements you imagine. Your description should be at least 150 words long."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        description = t['description']
        return f"""Complete the following task based on the given description:

Description: {description}

For Task 1, provide a detailed and vivid textual description of the visual scene, including all notable elements and activities. Ensure the description is at least 150 words long. For Task 2, generate a visual scene based on the provided description, ensuring to include all specified elements and additional details to enhance the imagery. Ensure your description is at least 150 words long. Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The description should be vivid and detailed.", "The description should include all specified elements.", "The description should be at least 150 words long."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
