class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "description": "A bustling city street during the day with tall buildings, people walking on the sidewalks, cars honking, and street vendors selling various items. The sky is clear with the sun shining brightly.",
                "transformation": "Transform this scene into a peaceful nighttime setting."
            },
            "2": {
                "description": "A cozy living room with a fireplace, a comfortable sofa, a coffee table with books, and a large window showing a snowy landscape outside. A cat is curled up on the rug in front of the fireplace.",
                "transformation": "Transform this scene into a summer setting."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Interpret the following detailed description of a visual scene and transform it according to the specified instructions. Ensure that your new description is vivid, coherent, and accurately reflects the transformation theme.

Scene Description:
{t['description']}

Transformation Instructions:
{t['transformation']}

Submit your transformed scene description in the following format:

Transformed Description:
[Your transformed description here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0