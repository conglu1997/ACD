class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {'criteria': 'Describe a 3D object that resembles a modern skyscraper. It should have a rectangular base, a height of approximately 300 meters, and feature at least 10 different floors with varying designs. Each floor should have unique features such as balconies, gardens, or terraces.'},
            '2': {'criteria': 'Describe a 3D object that resembles a futuristic vehicle. It should be aerodynamic, have a length of approximately 5 meters, and feature at least 3 distinct sections with specific functionalities. Each section should have unique details such as control panels, passenger seating, or cargo space.'}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Generate a detailed description of a 3D object based on the following criteria: {t['criteria']}\nStructure your description into clear sections, detailing the shape, dimensions, features, and relative positioning. Ensure each section is comprehensive and covers all specified features. Your description should be vivid and imaginative while maintaining logical consistency. Submit your description as a plain text string in the following format:\n\n1. Shape and Dimensions: [Your description]\n2. Floor/Section Features: [Your description]\n3. Unique Elements: [Your description]"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The description should accurately reflect the given criteria.", "The description should be detailed, vivid, and logically structured.", "The description should logically explain the spatial relationships and features.", "The response should follow the given format and cover all specified sections.", "The description should be coherent and maintain a logical flow."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
