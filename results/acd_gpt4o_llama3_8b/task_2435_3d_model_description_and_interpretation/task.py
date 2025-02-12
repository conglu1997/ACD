class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"type": "furniture", "object": "chair"},
            "2": {"type": "architecture", "object": "house"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Task 1: Generate a detailed textual description for a 3D model of a {t['type']} object, specifically a {t['object']}. Your description should include:
1. Dimensions and proportions.
2. Materials and textures.
3. Key features and components.
4. Any special design elements or unique aspects.

Task 2: Interpret the following textual description and visualize the 3D model. Describe the model in terms of its shape, dimensions, materials, and key features. Example description: 'A modern house with two floors. The first floor has a large rectangular living room with wooden flooring and a glass wall facing the garden. The second floor has three bedrooms with carpeted floors and a balcony extending from the master bedroom.'

Submit your response as a plain text string in the following format:

Visualization: [Your detailed visualization of the 3D model]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The description should be detailed and cover all specified aspects.",
            "The interpretation should be accurate and coherent.",
            "The response should follow the specified format.",
            "The description should demonstrate creativity and originality where applicable.",
            "The interpretation should demonstrate clear understanding of the spatial relationships and object features."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
