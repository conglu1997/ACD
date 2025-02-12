class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"initial_shape": "cube", "transformations": ["rotate 90 degrees around the x-axis", "translate up by 3 units", "scale by a factor of 2"]},
            "2": {"initial_shape": "sphere", "transformations": ["translate left by 5 units", "scale by a factor of 0.5", "rotate 45 degrees around the y-axis"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to describe the resulting 3D shape after a series of specified transformations are applied to an initial geometric object.

Initial Shape: {t['initial_shape']}
Transformations:
1. {t['transformations'][0]}
2. {t['transformations'][1]}
3. {t['transformations'][2]}

Provide a detailed description of the resulting shape, including its orientation, position, and size. Ensure your description is clear and precise.

Provide your response in the following format:

Resulting Shape Description:
- Orientation: [Describe the orientation]
- Position: [Describe the position]
- Size: [Describe the size]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should accurately describe the resulting shape after the specified transformations.",
            "The description should include details about the shape's orientation, position, and size."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
