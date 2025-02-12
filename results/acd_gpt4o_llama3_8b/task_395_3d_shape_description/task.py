class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "shape_description": "A cube with a side length of 5 cm, with a smaller cube of side length 2 cm cut out from the center of each face.",
                "task_type": "interpret"
            },
            "2": {
                "shape": "A sphere with a radius of 10 cm, with a cylindrical hole of radius 2 cm and height 10 cm drilled through its center along the Z-axis.",
                "task_type": "generate"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task_type"] == "interpret":
            return f"""Interpret the following description of a 3D shape and identify its key elements. Provide a detailed description of the shape's structure and characteristics. Your interpretation should be clear and logically organized.

Description:
{t['shape_description']}

Submit your interpretation as a plain text string in the following format:
'Key Elements: [Your interpretation here]'"""
        elif t["task_type"] == "generate":
            return f"""Generate a detailed description of the following 3D shape. Ensure that the description captures all key elements and characteristics of the shape. Your description should be clear and detailed.

Shape:
{t['shape']}

Submit your description as a plain text string in the following format:
'Detailed Description: [Your description here]'"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["task_type"] == "interpret":
            validation_criteria = ["The interpretation should accurately capture the structure and key elements of the described 3D shape.", "The interpretation should be coherent and logically organized."]
        elif t["task_type"] == "generate":
            validation_criteria = ["The generated description should accurately capture the structure and key elements of the given 3D shape.", "The description should be clear and detailed."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
