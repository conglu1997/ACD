class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"object_description": "A cube with a side length of 2 units, made of wood, with a small red sphere embedded at its center. The cube is resting on one of its faces on a flat surface."},
            "2": {"creation_criteria": "Create a description of a 3D object that consists of a base shape (e.g., cube, sphere, cylinder) and at least two additional features (e.g., embedded shapes, textures, colors). The object must have a unique transformation applied to it (e.g., rotation, scaling, translation)."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'object_description' in t:
            return f"""Your task is to describe the given 3D object in detail and explain any transformations applied to it.

Object Description:
{t['object_description']}

Instructions:
1. Provide a detailed description of the 3D object, including its shape, dimensions, material, and any additional features.
2. Explain any transformations that the object has undergone (e.g., rotations, translations, scaling). Be specific about the type, direction, and magnitude of each transformation.

Your response should be in the following format:
Description: [Your detailed description]
Transformations: [Your explanation of any transformations]"""
        elif 'creation_criteria' in t:
            return f"""Your task is to create a new 3D object based on the given criteria.

Creation Criteria:
{t['creation_criteria']}

Instructions:
1. Provide a detailed description of the new 3D object, ensuring that it includes all specified elements.
2. Explain any transformations applied to the object (e.g., rotations, translations, scaling). Be specific about the type, direction, and magnitude of each transformation.

Your response should be in the following format:
Object Description: [Your detailed description]
Transformations: [Your explanation of any transformations]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'object_description' in t:
            criteria = ["The description should include the shape, dimensions, material, and any additional features of the 3D object.", "The explanation should clearly describe any transformations the object has undergone, including type, direction, and magnitude."]
        elif 'creation_criteria' in t:
            criteria = ["The new 3D object description should include all specified elements in a coherent and detailed manner.", "The explanation should clearly describe any transformations applied to the object, including type, direction, and magnitude."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
