class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "initial_state": "A cube is placed on a table with one face colored red. The red face is on the top. The cube is rotated 90 degrees to the left.",
                "transformation": "Describe the new position of the red face and the orientation of the cube."
            },
            "2": {
                "initial_state": "A rectangular box is standing vertically on its shorter side. One of its longer faces is painted blue. The box is tipped over to lie flat on its longer side.",
                "transformation": "Describe the new position of the blue face and the orientation of the box."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        initial_state = t["initial_state"]
        transformation = t["transformation"]
        instructions = f"""Your task is to visualize and describe the transformation of an object based on the given instructions:

Initial State: {initial_state}

Transformation: {transformation}

Your response should accurately describe the new position of the specified face and the overall orientation of the object after the transformation. Provide your response in plain text format as follows:

New Position: [Describe the new position of the specified face]
Orientation: [Describe the new orientation of the object]

Example response format:

New Position: The red face is now on the left side of the cube.
Orientation: The cube is oriented with the previously left face now on top.

Ensure your response is clear, logically structured, and accurately describes the transformation."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The description should accurately reflect the new position of the specified face.",
            "The orientation of the object should be correctly described after the transformation.",
            "The response should follow the provided format and be clear and logically structured."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
