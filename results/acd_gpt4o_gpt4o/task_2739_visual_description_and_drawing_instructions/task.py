class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"image_description": "A house with a triangular roof, a door in the center, and two windows on each side of the door. There is a tree on the left side of the house and a sun in the top right corner of the sky.", "drawing_instructions": "Draw a house with a triangular roof. In the center of the house, draw a door, and on each side of the door, draw a window. Next to the house on the left, draw a tree. In the top right corner of the drawing, add a sun."},
            "2": {"image_description": "A car with four wheels, two doors, and a sunroof. There is a tree behind the car and a bird flying in the sky above the tree.", "drawing_instructions": "Start by drawing a car with four wheels. Add two doors to the car and a sunroof on top. Behind the car, draw a tree, and in the sky above the tree, draw a bird flying."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task has two parts:

Part 1: Based on the given description, provide a detailed and coherent visual description of the image.

Description:
{t['image_description']}

Part 2: Generate step-by-step drawing instructions based on a given description.

Instructions:
{t['drawing_instructions']}

Your response should be structured as follows:

1. Visual Description: [Your detailed visual description]
2. Drawing Instructions: [Your step-by-step drawing instructions]

Ensure that your visual description is detailed and coherent, and that your drawing instructions are clear and easy to follow."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The visual description should match the given image description in detail.",
            "The drawing instructions should be clear, sequential, and should accurately reflect the given description.",
            "Both parts should be coherent and easy to understand."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
