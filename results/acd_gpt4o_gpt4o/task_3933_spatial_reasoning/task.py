class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {"shape": [[1, 0, 0], [1, 1, 1], [0, 0, 1]], "rotation": 90},
            "2": {"shape": [[0, 1, 0], [1, 1, 1], [0, 0, 0]], "rotation": 180}
        }
        assert len(tasks) == 2, "There should be exactly two tasks."
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        import numpy as np
        shape = np.array(t['shape'])
        shape_str = '\n'.join([' '.join(map(str, row)) for row in shape])
        return f"""Given the following 2D shape (represented as a grid of 0s and 1s):

{shape_str}

Predict the outcome of rotating the shape by {t['rotation']} degrees clockwise. Provide your response as a matrix of 0s and 1s in plain text format, where each row of the matrix is on a new line and values are space-separated."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        import numpy as np

        # Helper function to rotate the matrix
        def rotate_matrix(matrix, degrees):
            if degrees == 90:
                return np.rot90(matrix, -1)
            elif degrees == 180:
                return np.rot90(matrix, 2)
            elif degrees == 270:
                return np.rot90(matrix, 1)
            else:
                return matrix

        # Convert the submission to a matrix
        try:
            submission_matrix = np.array([list(map(int, row.split())) for row in submission.strip().split('\n')])
        except Exception:
            return 0.0

        # Calculate the correct rotated shape
        correct_shape = rotate_matrix(np.array(t['shape']), t['rotation'])
        criteria = [f"The resulting matrix after rotating by {t['rotation']} degrees should be: \n{correct_shape}"]
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
