class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "diagram_description": "A rectangle with a length of 10 units and a width of 5 units, with a circle of radius 2 units positioned at the center of the rectangle. There are also two smaller squares with side lengths of 1 unit each positioned at the top-left and bottom-right corners of the rectangle. Additionally, an equilateral triangle with a side length of 3 units is positioned above the center of the rectangle."
            },
            "2": {
                "diagram_representation": {
                    "shapes": [
                        {"type": "rectangle", "length": 10, "width": 5, "position": "origin"},
                        {"type": "circle", "radius": 2, "position": "center of the rectangle"},
                        {"type": "square", "side": 1, "position": "top-left corner of the rectangle"},
                        {"type": "square", "side": 1, "position": "bottom-right corner of the rectangle"},
                        {"type": "triangle", "side": 3, "position": "above the center of the rectangle"}
                    ]
                }
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "diagram_description" in t:
            return f"""Convert the following textual description into a structured representation of the diagram:

{t['diagram_description']}

Submit your response as a JSON object in the following format:
{{"shapes": [{{"type": "shape_type", "dimensions": [dimension_values], "position": "position_description"}}]}}

Example Response:
{{"shapes": [{{"type": "rectangle", "length": 10, "width": 5, "position": "origin"}}, {{"type": "circle", "radius": 2, "position": "center of the rectangle"}}, {{"type": "square", "side": 1, "position": "top-left corner of the rectangle"}}]}}
"""
        else:
            return f"""Generate a textual description of the following diagram representation:

{t['diagram_representation']}

Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "diagram_description" in t:
            validation_criteria = [
                "The structured representation should accurately reflect the shapes and their dimensions described in the text.",
                "The positions of the shapes should be correctly identified and described."
            ]
        else:
            validation_criteria = [
                "The textual description should accurately reflect the shapes and their dimensions in the structured representation.",
                "The positions of the shapes should be correctly described."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
