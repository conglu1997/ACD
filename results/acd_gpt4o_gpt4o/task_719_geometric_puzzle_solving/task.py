class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"shapes": ["triangle", "square", "triangle"], "target_shape": "hexagon"},
            "2": {"shapes": ["rectangle", "triangle", "circle"], "target_shape": "house shape with a triangular roof"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        shapes = ", ".join(t["shapes"])
        target_shape = t["target_shape"]
        instructions = f"""Your task is to solve a geometric puzzle involving the following shapes: {shapes}.

1. Determine if it is possible to arrange the given shapes to form the target shape: {target_shape}.
2. If it is possible, describe the arrangement of the shapes in detail.
3. If it is not possible, provide an explanation as to why not.

Example:
Shapes: triangle, square, triangle
Target Shape: hexagon

Possible Solution:
- Step 1: Place the square in the center.
- Step 2: Arrange one triangle on the left side of the square.
- Step 3: Arrange the other triangle on the right side of the square.
- This forms a hexagon shape.

If the shapes cannot form the target shape, explain why, such as "The given shapes do not have the necessary angles to form a hexagon."

Your response should be in the following format:

Solution:
- Step 1: [description of step]
- Step 2: [description of step]
- ...

Or, if not possible:
Explanation: [Your detailed explanation]
"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The solution should accurately describe the arrangement if the shapes can form the target shape.",
            "If the shapes cannot form the target shape, the explanation should be logically sound."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
