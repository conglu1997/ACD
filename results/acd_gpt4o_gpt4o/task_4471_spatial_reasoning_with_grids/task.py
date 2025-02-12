class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"grid_size": 5, "objects": {"A": [1, 1], "B": [3, 2], "C": [4, 4]}},
            "2": {"grid_size": 4, "description": "A 4x4 grid with objects placed as follows: Object X is in the top-left corner, Object Y is in the bottom-right corner, and Object Z is directly to the right of Object X."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'objects' in t:
            return f"""Your task is to describe the spatial arrangement of objects within a {t['grid_size']}x{t['grid_size']} grid.

Objects: {', '.join([f'{k} at {v}' for k, v in t['objects'].items()])}

Ensure your description is clear, accurate, and captures the relative positions of the objects within the grid. Provide your description in plain text format. Your response should be structured as follows:

Description: [Your detailed description]. Ensure that your description follows the format 'Object at [row, column]'. For example, 'Object A at [1, 1], Object B at [3, 2], Object C at [4, 4]'."""
        else:
            return f"""Your task is to reconstruct the spatial arrangement of objects within a {t['grid_size']}x{t['grid_size']} grid based on the following description:

Description: {t['description']}

Ensure your reconstruction is accurate and clearly specifies the positions of all objects within the grid. Provide your reconstruction in plain text format, listing the objects and their positions in the format 'Object at [row, column]'. Your response should be structured as follows:

Reconstruction: [List of objects and their positions]. Ensure that your reconstruction follows the format 'Object at [row, column]'. For example, 'Object X at [0, 0], Object Y at [3, 3], Object Z at [0, 1]'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'objects' in t:
            criteria = ["The description should accurately capture the relative positions of the objects.", "The description should be clear and coherent.", "The description should follow the specified format."]
        else:
            criteria = ["The reconstruction should accurately specify the positions of all objects within the grid.", "The reconstruction should be clear and follow the specified format."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
