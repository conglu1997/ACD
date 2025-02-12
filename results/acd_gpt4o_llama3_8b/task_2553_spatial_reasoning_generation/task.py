class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "description": "Generate a description of a simple 3x3 grid pattern where the diagonal cells are filled.",
                "pattern": [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
                "criteria": "The description should clearly indicate the filled and empty cells in the grid."
            },
            "2": {
                "description": "Generate a 4x4 grid pattern based on the following description: 'The first row and the last row are completely filled, and the cells on the main diagonal are filled.'",
                "pattern": [[1, 1, 1, 1], [0, 1, 0, 0], [0, 0, 1, 0], [1, 1, 1, 1]],
                "criteria": "The generated pattern should match the description exactly."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Interpret the given spatial description or pattern and perform the required task as specified.

Description:
{t['description']}

Response Format:
For Task 1: Describe the pattern clearly in text, indicating the positions of filled and empty cells. Example: 'The grid is 3x3. The cell at (1,1) is filled, the cell at (2,2) is filled, the cell at (3,3) is filled, all other cells are empty.'
For Task 2: Generate the grid pattern as a 2D list of 1s and 0s. Example: [[1, 1, 1, 1], [0, 1, 0, 0], [0, 0, 1, 0], [1, 1, 1, 1]]."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "For Task 1: The description should clearly indicate the filled and empty cells in the grid.",
            "For Task 2: The generated pattern should match the description exactly as a 2D list of 1s and 0s."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
