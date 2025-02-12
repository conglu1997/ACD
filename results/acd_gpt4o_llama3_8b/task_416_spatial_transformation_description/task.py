class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"object": "cube", "axis": "x", "angle": 90},
            "2": {"object": "pyramid", "axis": "y", "angle": 180}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        object = t['object']
        axis = t['axis']
        angle = t['angle']
        return f"""Describe the transformation of a {object} when it is rotated {angle} degrees around the {axis}-axis.

Ensure your description is clear, detailed, and accurately conveys the spatial transformation of the object. Your submission should be a plain text string in the following format:

Description: [Your detailed description]

Example:
Object: Cube
Axis: X
Angle: 90 degrees
Description: The cube, initially resting on one of its faces, is rotated 90 degrees around the x-axis. This rotation causes the cube to turn so that another face, which was perpendicular to the x-axis, now becomes the base. The orientation of the other faces changes accordingly, with the top face now facing forward."

Focus on describing both the initial and final orientations of the object and any intermediate steps if necessary."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The description should accurately reflect the spatial transformation of the object.",
            "The description should mention the initial and final orientation of the object.",
            "The description should include any intermediate steps if necessary.",
            "The description should be clear and detailed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
