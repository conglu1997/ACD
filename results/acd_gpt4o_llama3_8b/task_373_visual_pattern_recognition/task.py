class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "description": "Imagine a 3x3 grid where each cell is either filled or empty. The pattern is as follows: The top row is fully filled, the middle row has the middle cell filled, and the bottom row is empty. Describe this pattern in a way that someone could recreate it.",
            },
            "2": {
                "description": "Consider a 4x4 grid with the following pattern: The first and last rows are fully filled, and the two middle rows have the first and last cells filled, with the middle cells empty. Describe this pattern in a way that someone could recreate it.",
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Describe the following visual pattern based on the given description:

{t['description']}

Your description should be clear and detailed enough for someone to recreate the pattern accurately. Use precise language and spatial references. Ensure the description is logically structured and easy to follow. Describe the exact positions of filled and empty cells. A good approach is to describe each row and its pattern individually.

Example response format:

- The 3x3 grid has the following pattern:
  - The top row is fully filled.
  - The middle row has only the middle cell filled.
  - The bottom row is completely empty.

Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The description should accurately reflect the given pattern.",
            "The description should be clear and detailed enough for someone to recreate the pattern.",
            "The description should use precise language and spatial references.",
            "The description should be logically structured and easy to follow.",
            "The description should mention the exact positions of filled and empty cells."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
