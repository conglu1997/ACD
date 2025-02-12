class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "Describe a 3D shape, such as a cube, sphere, or pyramid, and how it changes when it undergoes a specific transformation (e.g., rotation, scaling, translation). Include details such as initial dimensions, angles, and the nature of the transformation."
            },
            "2": {
                "description": "Imagine a cube with side length 2 units. The cube is rotated 45 degrees about the z-axis and then scaled by a factor of 1.5 in all directions. Describe the final shape in detail, including any changes in dimensions and orientation."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "prompt" in t:
            instructions = f"""Your task is to describe a 3D shape and its transformation based on the following prompt:\n\n{t['prompt']}\n\nEnsure that your description includes all relevant details such as initial dimensions, angles, and the nature of the transformation. Provide your description in plain text format as follows:\n\nShape Description: [Your description]"""
        else:
            instructions = f"""Your task is to describe the final shape after the given transformations:\n\n{t['description']}\n\nInclude details about the changes in dimensions, orientation, and any other relevant aspects. Provide your description in plain text format as follows:\n\nFinal Shape Description: [Your description]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "prompt" in t:
            criteria = [
                "The description should clearly define a 3D geometric shape, including its initial dimensions and angles.",
                "The transformation should be described accurately, including the nature of the transformation.",
                "The description should be detailed and logically structured.",
                "The response format should match: 'Shape Description: [Your description]'."
            ]
        else:
            criteria = [
                "The final shape should be described accurately after the transformations, including changes in dimensions and orientation.",
                "The description should be detailed and logically structured.",
                "The response format should match: 'Final Shape Description: [Your description]'."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
