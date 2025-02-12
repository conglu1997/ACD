class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {
                'initial_scenario': 'You are given a description of a 3D geometric structure. The structure consists of a central cube surrounded by six smaller cubes, one attached to each face of the central cube. Describe this structure in detail, including the relative positions of each of the smaller cubes to the central cube.',
                'followups': {
                    'add_cylinder': 'Now, imagine a cylindrical tube passes through the central cube from the top face to the bottom face. Describe the new structure in detail, including the interaction between the cylinder and the cubes.'
                }
            },
            '2': {
                'initial_scenario': 'You are given a description of a garden layout. The garden is rectangular, with a fountain in the center. Four flowerbeds are arranged symmetrically around the fountain, one in each quadrant. Describe the layout in detail, including the relative positions of the flowerbeds and the fountain.',
                'followups': {
                    'add_pathways': 'Now, imagine there are four pathways that connect each flowerbed to the fountain. Describe the new layout in detail, including the positions and orientations of the pathways.'
                }
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Interpret the following spatial description and generate a detailed textual description of the visual scene. Your description should be clear, detailed, and accurately reflect the spatial relationships described. Here is the initial scenario:

{t['initial_scenario']}

Respond with your detailed description in the following format:
Description: [Your detailed description of the visual scene]

You will receive a follow-up scenario based on your choice that you must also address. Please maintain the format and depth of detail in your responses."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            'The description should accurately reflect the spatial relationships described in the scenario.',
            'The response should be coherent, detailed, and logically structured.',
            'The response should maintain clarity and precision in describing the visual scene.'
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
