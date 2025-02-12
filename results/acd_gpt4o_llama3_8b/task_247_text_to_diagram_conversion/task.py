class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "description": "Create a diagram based on the following description: A rectangle with a circle inside it, touching the top side of the rectangle. There is also a small square outside the rectangle, positioned at the bottom left corner of the rectangle.",
                "constraints": "The diagram should accurately reflect the spatial relationships described."
            },
            "2": {
                "description": "Create a diagram based on the following description: Two overlapping circles of the same size, positioned horizontally. There is a triangle above the intersection of the circles, with its base parallel to the line where the circles intersect.",
                "constraints": "The diagram should accurately reflect the spatial relationships described."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Convert the following textual description into a corresponding diagram:

Description: {t['description']}

Constraints: {t['constraints']}

Ensure that your diagram accurately reflects the spatial relationships described. Submit your diagram as an ASCII art representation or a structured textual description that can be visualized as a diagram. Do not use any external tools or resources for creating the diagram. Your submission should be in plain text format.

Example of a simple diagram in ASCII art:

Description: A small square inside a larger square.

Diagram:
+-----+
|     |
| +-+ |
| | | |
| +-+ |
|     |
+-----+

To ensure clarity, structure your ASCII art as follows:
1. Use '+' for corners, '-' for horizontal lines, and '|' for vertical lines.
2. Align all elements properly to reflect spatial relationships.
3. Clearly label each element if necessary."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The diagram should accurately reflect the spatial relationships described.",
            "The diagram should be clear and coherent."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
