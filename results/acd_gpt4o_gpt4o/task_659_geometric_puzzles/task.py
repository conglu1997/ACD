class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"shape": "square", "transformations": ["rotate 45 degrees", "scale by 2", "translate right 3 units"]},
            "2": {"shape": "triangle", "transformations": ["reflect over y-axis", "translate left 4 units", "scale by 0.5", "rotate 180 degrees"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to solve the following geometric puzzle by describing the final shape and its position after applying a series of transformations.

Shape: {t['shape']}
Initial Position: Centered at the origin (0,0)
Transformations: {', '.join(t['transformations'])}

Provide a detailed description of the final shape, including its orientation, size, and position relative to the original shape. Ensure that your description is clear and accurate. Provide your response in plain text format, structured as follows:

1. Final Orientation: [Description of the final orientation]
2. Final Size: [Description of the final size]
3. Final Position: [Description of the final position]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The description should accurately reflect the final shape after all transformations.", "The description should include details of orientation, size, and position.", "The response should be clear and structured as specified in the instructions."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
