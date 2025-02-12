class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "task": "describe_3d_object",
                "object": "cube",
                "size": 3,
                "color": "red"
            },
            "2": {
                "task": "transform_3d_object",
                "object": "cuboid",
                "dimensions": [2, 3, 4],
                "transformation": "rotate 90 degrees around the x-axis"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task'] == 'describe_3d_object':
            return f"Describe the following 3D object: A {t['size']}x{t['size']}x{t['size']} {t['color']} {t['object']}. Provide a detailed description of its geometric properties, including the number of faces, edges, and vertices, as well as any symmetry properties. Submit your description as a plain text string in the following format: 'Description: [Your description]'."
        elif t['task'] == 'transform_3d_object':
            return f"Perform the following transformation on the given 3D object: A {t['dimensions'][0]}x{t['dimensions'][1]}x{t['dimensions'][2]} {t['object']}. Transformation: {t['transformation']}. Describe the new orientation and dimensions of the object after the transformation, including any changes to its faces, edges, and vertices. Submit your description as a plain text string in the following format: 'Transformation Result: [Your description]'."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['task'] == 'describe_3d_object':
            validation_criteria = [
                "The description should accurately capture the geometric properties of the object, including the number of faces, edges, vertices, and any symmetry properties.",
                "The response should follow the format: 'Description: [Your description]'."
            ]
        elif t['task'] == 'transform_3d_object':
            validation_criteria = [
                "The description should accurately capture the new orientation and dimensions of the object after the transformation, including any changes to its faces, edges, and vertices.",
                "The response should follow the format: 'Transformation Result: [Your description]'."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
