class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "Create an SVG image of a house with a triangular roof, a rectangular door, and two square windows. The house should be centered in the SVG canvas, and all elements should be correctly proportioned. The roof should be centered above the house, and the door should be centered below the roof with the windows symmetrically placed on either side."},
            "2": {"description": "Create an SVG image of a tree with a brown rectangular trunk and a green circular canopy. The tree should be centered in the SVG canvas, and all elements should be correctly proportioned. The trunk should be directly below the canopy."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate SVG code to create the following visual design:

{t['description']}

Ensure your SVG code is correct, and the design matches the description. Submit your SVG code as a plain text string. Here are examples of SVG code for a simple circle and a rectangle:

Circle:
<svg width='100' height='100'>
  <circle cx='50' cy='50' r='40' stroke='black' stroke-width='3' fill='red' />
</svg>

Rectangle:
<svg width='200' height='100'>
  <rect width='200' height='100' style='fill:rgb(0,0,255);stroke-width:3;stroke:rgb(0,0,0)' />
</svg>

Your SVG code should follow similar syntax and structure."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The SVG code should correctly represent the described visual design.",
            "The design elements should be correctly proportioned and positioned as described.",
            "The colors of the design elements should be correct.",
            "The SVG code should be syntactically correct.",
            "The overall design should be centered in the SVG canvas."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
