class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "shapes": [
                    {"type": "square", "position": [0, 0], "size": 2},
                    {"type": "triangle", "position": [3, 3], "size": 2}
                ],
                "transformations": [
                    {"shape": 0, "type": "translate", "by": [2, 1]},
                    {"shape": 1, "type": "rotate", "by": 90}
                ]
            },
            "2": {
                "shapes": [
                    {"type": "circle", "position": [1, 1], "radius": 1},
                    {"type": "rectangle", "position": [4, 4], "size": [2, 1]}
                ],
                "transformations": [
                    {"shape": 0, "type": "scale", "by": 2},
                    {"shape": 1, "type": "translate", "by": [-2, -3]}
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = "You will be given a set of shapes and a series of geometric transformations. Your task is to describe the final position and dimensions of each shape after all transformations have been applied."
        shapes = t['shapes']
        transformations = t['transformations']

        instructions += "\nShapes:"
        for i, shape in enumerate(shapes):
            if shape['type'] == 'square':
                instructions += f"\n- Shape {i}: Square at position {shape['position']} with size {shape['size']}"
            elif shape['type'] == 'triangle':
                instructions += f"\n- Shape {i}: Triangle at position {shape['position']} with size {shape['size']}"
            elif shape['type'] == 'circle':
                instructions += f"\n- Shape {i}: Circle at position {shape['position']} with radius {shape['radius']}"
            elif shape['type'] == 'rectangle':
                instructions += f"\n- Shape {i}: Rectangle at position {shape['position']} with size {shape['size']}"

        instructions += "\nTransformations:"
        for transformation in transformations:
            if transformation['type'] == 'translate':
                instructions += f"\n- Translate Shape {transformation['shape']} by {transformation['by']}"
            elif transformation['type'] == 'rotate':
                instructions += f"\n- Rotate Shape {transformation['shape']} by {transformation['by']} degrees"
            elif transformation['type'] == 'scale':
                instructions += f"\n- Scale Shape {transformation['shape']} by a factor of {transformation['by']}"

        instructions += "\nSubmit the final position and dimensions of each shape as a plain text string in the following format:"
        instructions += "\nShape 0: [final position, final dimensions]"
        instructions += "\nShape 1: [final position, final dimensions]"
        instructions += "\nFor example:"
        instructions += "\nShape 0: [2, 1], size 2"
        instructions += "\nShape 1: [3, 3], size 2"
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)

        def apply_transformations(shapes, transformations):
            def translate(position, by):
                return [position[0] + by[0], position[1] + by[1]]

            def rotate(position, angle):
                import math
                rad = math.radians(angle)
                x, y = position
                x_new = x * math.cos(rad) - y * math.sin(rad)
                y_new = x * math.sin(rad) + y * math.cos(rad)
                return [round(x_new, 2), round(y_new, 2)]

            def scale(size, factor):
                if isinstance(size, list):
                    return [round(s * factor, 2) for s in size]
                return round(size * factor, 2)

            for transformation in transformations:
                shape = shapes[transformation['shape']]
                if transformation['type'] == 'translate':
                    shape['position'] = translate(shape['position'], transformation['by'])
                elif transformation['type'] == 'rotate':
                    shape['position'] = rotate(shape['position'], transformation['by'])
                elif transformation['type'] == 'scale':
                    if shape['type'] == 'circle':
                        shape['radius'] = scale(shape['radius'], transformation['by'])
                    else:
                        shape['size'] = scale(shape.get('size', [shape['size']]), transformation['by'])
            return shapes

        try:
            shapes = apply_transformations(t['shapes'], t['transformations'])
            final_shapes_description = ""
            for i, shape in enumerate(shapes):
                if shape['type'] == 'circle':
                    final_shapes_description += f"Shape {i}: {shape['position']}, radius {shape['radius']}\n"
                else:
                    final_shapes_description += f"Shape {i}: {shape['position']}, size {shape['size']}\n"
            criteria = [final_shapes_description.strip()]
            return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
        except Exception:
            return 0.0
