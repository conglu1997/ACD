class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"image_description": "The image shows a bustling city street. There are tall buildings on either side of the street, and various shops on the ground floor. People are walking on the sidewalks, some carrying shopping bags. There is a traffic light at the intersection showing red, and several cars are waiting at the light."},
            "2": {"image_description": "The image depicts a serene beach scene. There are gentle waves lapping at the shore, and a few people are sunbathing on the sand. In the background, there are palm trees and a beachside café. A child is building a sandcastle near the water's edge."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following task based on the given image description:

Image Description: {t['image_description']}

Answer the following questions based on the image description:
1. What is the current state of the traffic light?
2. How many people are carrying shopping bags?
3. What is the child doing near the water's edge?
4. What is the primary activity of the people on the sand?

Submit your answers as a plain text string with clearly labeled sections for each question (e.g., 'Answer 1', 'Answer 2')."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should correctly answer the question based on the image description.",
            "Each answer should be clearly labeled as 'Answer 1', 'Answer 2', etc.",
            "The answers should be coherent and logically derived from the description."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
