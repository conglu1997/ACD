class TaskFamily:
    import numpy as np

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {'shape': [[0, 0], [1, 0], [0.5, 0.866]], 'transformations': 'rotate 60; translate 1 0'},
            '2': {'shape': [[0, 0], [2, 0], [2, 2], [0, 2]], 'transformations': 'rotate 45; translate -1 -1'}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to interpret and manipulate geometric shapes based on the given instructions.

Shape: {t['shape']}
Transformations: {t['transformations']}

1. Interpret the given shape as a list of vertices in Cartesian coordinates (x, y).
2. Apply the transformations to the shape in the given order. The transformations can be 'rotate <angle>' in degrees and 'translate <dx> <dy>' in units.
3. Provide the coordinates of the vertices of the transformed shape.

Your response format:
Transformed Shape: [List of vertices of the transformed shape]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        import json
        import numpy as np

        def apply_transformations(shape, transformations):
            shape = np.array(shape)
            for transformation in transformations.split('; '):
                if 'rotate' in transformation:
                    angle = float(transformation.split()[1])
                    radians = np.deg2rad(angle)
                    rotation_matrix = np.array([
                        [np.cos(radians), -np.sin(radians)],
                        [np.sin(radians), np.cos(radians)]
                    ])
                    shape = shape.dot(rotation_matrix)
                elif 'translate' in transformation:
                    dx, dy = map(float, transformation.split()[1:])
                    shape = shape + np.array([dx, dy])
            return shape.tolist()

        try:
            expected_shape = apply_transformations(t['shape'], t['transformations'])
            submission_shape = json.loads(submission.split(': ')[1])
            return 1.0 if np.allclose(expected_shape, submission_shape, atol=0.01) else 0.0
        except (json.JSONDecodeError, IndexError, ValueError) as e:
            print(f"Error parsing submission: {e}")
            return 0.0
