class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "initial_arrangement": "A room with a bed in the center, a desk to the left of the bed, a chair in front of the desk, and a bookshelf against the right wall.",
                "transformation_criteria": "Move the bed to the left wall, place the desk in the center, and move the bookshelf to the left of the desk."
            },
            "2": {
                "initial_arrangement": "A garden with a tree in the center, a flower bed to the right of the tree, a bench to the left of the tree, and a fountain in front of the tree.",
                "transformation_criteria": "Move the tree to the back of the garden, place the flower bed in the center, and move the bench to the right of the flower bed."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Describe how to transform the following initial spatial arrangement based on the given criteria:

Initial Arrangement: {t['initial_arrangement']}
Transformation Criteria: {t['transformation_criteria']}

Ensure that your description is clear, logical, and accurately follows the transformation criteria. Mention the new positions of all specified objects. Break down the transformation into distinct steps. Submit your response as a plain text string in the following format:

Transformation Description: [Your description]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The description should clearly indicate the new positions of all specified objects.",
            "The transformation should follow the given criteria accurately.",
            "The description should be logical and coherent.",
            "The transformation should be broken down into distinct steps."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
