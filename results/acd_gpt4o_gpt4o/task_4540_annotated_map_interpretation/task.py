class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "map": "A simple map of a park with various landmarks such as a playground, pond, and picnic area located at specific coordinates. Playground is at (2,3), Pond is at (5,5), Picnic Area is at (1,6). The park is a 10x10 grid.",
                "annotations": "P - Playground, Po - Pond, PA - Picnic Area",
                "question": "Where is the playground located relative to the pond? Provide your answer in terms of direction (e.g., north, northeast, etc.) and distance (e.g., number of grid units)."
            },
            "2": {
                "map": "A city map with locations of various amenities like hospitals, schools, and restaurants located at specific coordinates. Hospital is at (3,4), School is at (6,1), Restaurant is at (8,5). The city grid is a 10x10 grid.",
                "annotations": "H - Hospital, S - School, R - Restaurant",
                "question": "If you start at the school and go to the restaurant, what landmarks do you pass? List the landmarks in order of passing, including their coordinates."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to interpret the given annotated map and answer the specific question based on the map and its annotations.

Map Description:
{t['map']}

Annotations:
{t['annotations']}

Question:
{t['question']}

Provide your answer in a clear and concise manner, ensuring it accurately reflects the details from the map and annotations. Format your response as follows:

Answer: [Your Answer]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The answer should be clear and concise.",
            "The answer should accurately reflect the details from the map and annotations.",
            "The answer should be logically consistent with the given coordinates and annotations.",
            "The answer should include direction and distance for Task 1.",
            "The answer should include landmarks and their coordinates for Task 2."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
