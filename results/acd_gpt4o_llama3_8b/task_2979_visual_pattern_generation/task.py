class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "description": "A pattern with concentric circles and alternating colors in each circle. The colors should be red, blue, and yellow in a repeating sequence."
            },
            "2": {
                "description": "A pattern with a central star surrounded by hexagons. Each hexagon should have a different color, and all colors in the pattern should be different shades of green."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a visual pattern based on the following description:

Description: {t['description']}

Describe your generated pattern in detail, explaining how each element of the description is represented in the pattern. Include details such as the arrangement, colors, and any other relevant attributes. Submit your description as a plain text string in the following format:

Pattern Description:
1. [Description of the first element]
2. [Description of the second element]
3. [Description of the third element]
..."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The generated pattern should accurately reflect the given description.",
            "The description should be detailed enough to visualize the pattern.",
            "The response should be coherent and logically sequenced."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
