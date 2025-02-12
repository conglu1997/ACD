class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "description": "Draw a simple house with a triangular roof, a rectangular door, and two square windows. The house should be centered on the canvas and have a width of 200 units and a height of 150 units. The roof should be red, the house body yellow, and the door and windows blue.",
                "canvas_size": "400x400"
            },
            "2": {
                "description": "Create a scene with a sun in the top-right corner, a tree in the bottom-left corner, and a river flowing from the middle of the canvas to the bottom-right corner. The sun should be a yellow circle, the tree should have a brown trunk and green leaves, and the river should be blue.",
                "canvas_size": "500x500"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        description = t["description"]
        canvas_size = t["canvas_size"]
        width, height = canvas_size.split('x')
        instructions = f"""Your task is to generate SVG code based on the following artistic description:

Description: {description}

The SVG code should fit within a canvas of size {canvas_size}. Ensure that the SVG code is correctly formatted and accurately represents the described scene or object. Pay attention to colors, shapes, and positions as specified in the description.

Provide your SVG code in plain text format.

Example format:
<svg width='{width}' height='{height}' xmlns='http://www.w3.org/2000/svg'>
  [Your SVG elements here]
</svg>

Ensure that your SVG code includes the following elements:
- For Task 1: A triangle for the roof, a rectangle for the door, and squares for the windows.
- For Task 2: A circle for the sun, a tree with a trunk and leaves, and a flowing river."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The SVG code should be correctly formatted.",
            "The SVG code should accurately represent the described scene or object.",
            "The shapes, colors, and positions should match the description.",
            "The SVG should fit within the specified canvas size.",
            "For Task 1: The SVG elements should include a triangle for the roof, a rectangle for the door, and squares for the windows.",
            "For Task 2: The SVG elements should include a circle for the sun, a tree with a trunk and leaves, and a flowing river. The positions should match the description."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
