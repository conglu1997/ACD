class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {"blueprint": "A cube with a side length of 5 units, with a small spherical indentation of radius 1 unit on one face."},
            "2": {"description": "A rectangular prism with dimensions 3x4x6 units, with a cylindrical hole of radius 1 unit running through its longest dimension and a conical cutout on one face with a base radius of 2 units and height of 3 units."}
        }
        assert len(tasks) == 2, "There should be exactly two tasks."
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'blueprint' in t:
            return f"""Generate a detailed description of the 3D object based on the following blueprint:

Blueprint: {t['blueprint']}

Ensure your description includes all relevant dimensions, shapes, and spatial relationships. Provide your response in plain text format."""
        else:
            return f"""Interpret the following description of a 3D object and generate a blueprint in text format:

Description: {t['description']}

Ensure your blueprint includes all relevant dimensions, shapes, and spatial relationships. Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should accurately capture the dimensions, shapes, and spatial relationships described in the blueprint or description.",
            "The response should be coherent and logically structured."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
