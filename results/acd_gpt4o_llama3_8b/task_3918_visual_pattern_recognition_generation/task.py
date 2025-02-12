class TaskFamily:
    import random

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "type": "recognition",
                "pattern": "⬜⬛⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜⬛⬜",
                "description": "This is a checkerboard pattern with alternating black and white squares."
            },
            "2": {
                "type": "generation",
                "criteria": "Generate a 4x4 checkerboard pattern starting with a white square in the top left corner."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['type'] == 'recognition':
            return f"""Recognize and describe the following visual pattern:

Pattern:\n{t['pattern']}\n\nYour description should include the type of pattern and its characteristics."""
        elif t['type'] == 'generation':
            return f"""Generate a visual pattern based on the following criteria:\n\nCriteria: {t['criteria']}\n\nSubmit your response as a plain text string formatted as a grid of squares, for example:\n⬜⬛⬜⬛\n⬛⬜⬛⬜\n⬜⬛⬜⬛\n⬛⬜⬛⬜"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['type'] == 'recognition':
            criteria = ["The response should accurately describe the visual pattern, including its type and characteristics."]
        elif t['type'] == 'generation':
            criteria = ["The generated pattern should meet the criteria specified and be formatted correctly as a grid of squares."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0