class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "task_type": "generation",
                "description": "A simple house with a triangular roof, a rectangular body, a centered door at the bottom, and two windows on either side of the door."
            },
            "2": {
                "task_type": "interpretation",
                "ascii_art": "  /\  \n /  \ \n/____\ \n| |  |\n|____|\n|_|__|"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task_type'] == 'generation':
            return f"""Generate ASCII art based on the following description:

Description: {t['description']}

Ensure that the ASCII art accurately represents the described scene. Submit your ASCII art as a plain text string. The art should be clear and recognizable."""
        else:
            return f"""Interpret the following ASCII art and provide a detailed description of what it represents:

ASCII Art:
{t['ascii_art']}

Ensure that your description captures the key elements and overall scene depicted in the ASCII art. Submit your description as a plain text string. The description should be clear and detailed."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['task_type'] == 'generation':
            validation_criteria = [
                "The ASCII art should accurately represent the described scene.",
                "The ASCII art should be clear and recognizable.",
                "The ASCII art should include a triangular roof, a rectangular body, a centered door at the bottom, and two windows on either side of the door."]
        else:
            validation_criteria = [
                "The description should accurately capture the key elements and overall scene depicted in the ASCII art.",
                "The description should be clear and detailed.",
                "The description should mention a triangular roof, a rectangular body, a door, and windows."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
