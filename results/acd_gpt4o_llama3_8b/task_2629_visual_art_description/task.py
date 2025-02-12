class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"instructions": "Draw a simple house with a door, two windows, and a chimney. Include a tree next to the house."},
            "2": {"instructions": "Draw a beach scene with a palm tree, a sun in the sky, and waves in the ocean. Include a beach ball on the sand."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Describe step-by-step how to draw the following scene: {t['instructions']}. Ensure that your description is clear and detailed enough for someone to visualize and draw the scene accurately. Submit your response in the following format:
1. [Step 1: Description of the first element to draw]
2. [Step 2: Description of the next element to draw]
...

Your description should include specific details about the shapes, sizes, and positions of each element in the scene. For example, specify whether a shape is a square, circle, or triangle, and provide relative sizes and positions (e.g., 'Draw a large square in the center of the page'). Include details about how elements relate to each other spatially (e.g., 'Place the tree to the left of the house and make it about half the height of the house')."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The description must be clear and logically ordered.",
            "The steps should be detailed enough to accurately draw the scene.",
            "The description should include specific details about shapes, sizes, and positions of each element.",
            "The positional relationships and proportions of the elements should be clearly described.",
            "The description must specify how elements relate to each other spatially, including relative sizes."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
