class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "shape": "pentagon",
                "transformation": "rotate 180 degrees around the origin and then translate 2 units right"
            },
            "2": {
                "shape": "hexagon",
                "transformation": "rotate 90 degrees counterclockwise around the origin and then reflect across the x-axis"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Describe the transformation of the following 2D geometric shape:

Shape: {t['shape']}
Transformation: {t['transformation']}

Ensure your description is clear, detailed, and accurately conveys the transformation of the shape. Mention the initial and final positions of the shape and any relevant changes in orientation or dimensions. Submit your response as a plain text string in the following format:

Description: [Your detailed description]

Example:
Shape: Square
Transformation: Reflect across the x-axis
Description: A square initially positioned with vertices at (1,1), (1,-1), (-1,-1), and (-1,1) will have its vertices at (1,-1), (1,1), (-1,1), and (-1,-1) after reflecting across the x-axis.

Example:
Shape: Triangle
Transformation: Rotate 90 degrees clockwise around the origin and then translate 3 units up
Description: A triangle initially positioned with vertices at (1,0), (0,1), and (-1,0) will have its vertices at (0,1), (-1,0), and (0,-1) after the rotation. After translating 3 units up, the vertices will be at (0,4), (-1,3), and (0,2)."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = ["The response should accurately describe the transformation of the shape as specified in the instructions."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
