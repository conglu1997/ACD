class TaskFamily:
    import numpy as np
    
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "task_id": "1",
                "object": "cube",
                "initial_orientation": [0, 0, 0],
                "rotation": [90, 0, 0],
                "target_face": "top"
            },
            "2": {
                "task_id": "2",
                "object": "rectangular prism",
                "initial_orientation": [0, 0, 0],
                "rotation": [0, 90, 0],
                "target_face": "front"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Perform the following spatial visualization task:

Object: {t['object']}
Initial Orientation: {t['initial_orientation']}
Rotation: {t['rotation']}

Identify the face that will be in the {t['target_face']} position after the rotation. Use the face names 'front', 'back', 'left', 'right', 'top', and 'bottom'.

Submit your response as a plain text string indicating the face that will be in the target position. Ensure your response is accurate and adheres to the given orientations and rotations."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        correct_faces = {
            "1": "front",
            "2": "right"
        }
        validation_criteria = [
            f"The face in the {t['target_face']} position should be '{correct_faces[t['task_id']]}'."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
