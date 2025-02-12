class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "instruction": "Rotate the given shape 90 degrees clockwise.",
                "shape": [[1, 0, 0], [1, 1, 1], [0, 0, 1]]
            },
            "2": {
                "instruction": "Reflect the given shape over its vertical axis.",
                "shape": [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        import numpy as np
        return f"""Complete the following task based on the given instruction and shape:

Instruction:
{t['instruction']}

Shape:
{np.array(t['shape'])}

Your task is to:
1. Perform the specified transformation on the given shape.
2. Submit the transformed shape as a 2D array in plain text format.

Ensure that your response is accurate and follows the given instruction."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        import numpy as np
        import ast
        try:
            shape = np.array(t['shape'])
            transformed_shape = np.array(ast.literal_eval(submission))
            if t['instruction'] == "Rotate the given shape 90 degrees clockwise.":
                expected_shape = np.rot90(shape, -1)
            elif t['instruction'] == "Reflect the given shape over its vertical axis.":
                expected_shape = np.fliplr(shape)
            return 1.0 if np.array_equal(transformed_shape, expected_shape) else 0.0
        except Exception as e:
            return 0.0
