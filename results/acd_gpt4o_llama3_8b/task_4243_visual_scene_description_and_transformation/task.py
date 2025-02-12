class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scene_description": "A cozy living room with a fireplace, a sofa, a coffee table, and a bookshelf filled with books. There is a window with curtains and a cat sitting on the windowsill.",
                "transformation": "Change the scene to depict the living room during a Christmas celebration with decorations, a Christmas tree, and a festive atmosphere."
            },
            "2": {
                "scene_description": "A bustling city street with tall buildings, cars driving by, people walking on the sidewalk, and street vendors selling food.",
                "transformation": "Transform the scene to show the same street during a quiet, snowy night with snow-covered streets, closed shops, and a serene atmosphere."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following tasks:

1. Describe the given visual scene in detail.
2. Transform the scene based on the specified modifications.

Scene Description:
{t['scene_description']}

Transformation:
{t['transformation']}

Ensure that your descriptions are vivid, detailed, and accurately reflect the modifications. Submit your response as a plain text string in the following format:

Initial Description:
[Your detailed initial description here]

Transformed Scene:
[Your detailed transformed scene here]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The initial description of the scene should be vivid and detailed.",
            "The transformed scene should accurately reflect the specified modifications.",
            "The overall description should be coherent and creative."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
