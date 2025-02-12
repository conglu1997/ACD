class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "Visualize a 3x3x3 cube and describe the configuration of cubes when one cube is removed from the center of each face. Additionally, explain the resulting structure in terms of its symmetry and any remaining sub-cubes."},
            "2": {"description": "Imagine a 2D grid of 5x5 squares where each row alternates between filled and empty squares, starting with a filled square in the top-left corner. Describe the pattern and provide the coordinates of each filled square."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to interpret and visualize spatial configurations based on the given descriptions. Provide clear and accurate visualizations and solutions.

Description: {t['description']}

For Task 1, describe the configuration of the 3x3x3 cube with one cube removed from the center of each face. Explain the resulting structure in terms of its symmetry and any remaining sub-cubes.

For Task 2, describe the pattern of the 5x5 grid and provide the coordinates of each filled square. Ensure your response includes:
1. A detailed description of the pattern.
2. The coordinates of all filled squares.

Provide your response in plain text format, including explanations and any necessary coordinates or configurations. Your response should be structured as follows:

Task 1:
[Description of the 3x3x3 cube configuration]

Task 2:
[Description of the 5x5 grid pattern]
[Coordinates of filled squares]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The description of the 3x3x3 cube should include the changes in symmetry and the configuration of remaining sub-cubes.",
            "The coordinates of the filled squares in the 5x5 grid should match the alternating pattern described."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
