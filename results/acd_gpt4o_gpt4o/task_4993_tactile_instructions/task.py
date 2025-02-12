class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "Create detailed step-by-step instructions for making a paper crane using a square piece of paper. Ensure that each step is clear, logical, and easy to follow."},
            "2": {"tactile_instructions": "Fold the paper in half diagonally to form a triangle. Unfold the paper and then fold it in half diagonally the other way to form another triangle. Unfold the paper again and fold it in half horizontally to form a rectangle. Unfold once more and fold it in half vertically to form another rectangle. Finally, collapse the paper along the creases to form a square base and then pull out the wings to form the crane."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'description' in t:
            return f"""Your task is to create detailed step-by-step instructions for making a paper crane using a square piece of paper. Ensure each step is clear, logical, and easy to follow, and include any necessary details to help someone complete the task. Provide your instructions in plain text format.

Response format:
Step 1: [Detailed instructions]
Step 2: [Detailed instructions]
..."""
        else:
            return f"""You are given a set of tactile instructions for making a paper crane. Your task is to interpret these instructions and describe the final object that is created. Ensure your description is detailed and accurately represents the final object. The instructions are provided below:

{t['tactile_instructions']}

Response format:
Description: [Detailed description of the final object]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'description' in t:
            criteria = ["The instructions should be clear and easy to follow.", "Each step should be detailed and logically sequenced.", "The instructions should lead to the successful creation of a paper crane."]
        else:
            criteria = ["The description should accurately represent the final object created from the tactile instructions.", "The description should be detailed and reflect all key features of the paper crane."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
