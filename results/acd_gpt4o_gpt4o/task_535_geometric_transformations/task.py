class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"initial_shape": "square", "transformations": "rotate 90 degrees clockwise, translate right 3 units"},
            "2": {"initial_shape": "triangle", "final_shape": "A triangle reflected over the y-axis and translated up 2 units"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'transformations' in t:
            return f"""Your task is to perform the following geometric transformations on the given shape:

Initial Shape: {t['initial_shape']}
Transformations: {t['transformations']}

Describe the final shape after the transformations in detail. Ensure your description includes the final position, orientation, and any other relevant characteristics of the shape. Provide your response in plain text format. Here is an example format for your response:

Final Shape: [Your description of the final shape]"""
        else:
            return f"""Your task is to describe the sequence of geometric transformations needed to achieve the final shape from the initial shape:

Initial Shape: {t['initial_shape']}
Final Shape: {t['final_shape']}

Ensure your description includes all necessary transformations (e.g., translation, rotation, reflection) and their specific parameters (e.g., angle of rotation, direction and distance of translation). Provide your response in plain text format. Here is an example format for your response:

Transformations: [Your description of the transformations]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'transformations' in t:
            criteria = ["The description should accurately reflect the final shape after the transformations.", "The final position and orientation of the shape should be correctly described."]
        else:
            criteria = ["The description should include all necessary transformations.", "The transformations should be described with correct parameters.", "The final shape should match the described transformations."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
