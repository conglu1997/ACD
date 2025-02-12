class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"shapes": ["square", "triangle", "rectangle"], "target_shape": "house"},
            "2": {"shapes": ["triangle", "circle", "rectangle"], "target_shape": "tree"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        shapes = ', '.join(t['shapes'])
        target_shape = t['target_shape']
        return f"""You are given the following shapes: {shapes}. Arrange these shapes to form a {target_shape}. Describe how you would arrange the shapes to create the target shape. Your response should include:
1. A step-by-step description of how to arrange the shapes.
2. An explanation of why this arrangement forms the target shape.

Submit your solution as a plain text string describing the arrangement process in the following format:

Step-by-Step Description: [Your description here]
Explanation: [Your explanation here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The solution should include a step-by-step description of how to arrange the shapes.",
            "The solution should explain why this arrangement forms the target shape."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
