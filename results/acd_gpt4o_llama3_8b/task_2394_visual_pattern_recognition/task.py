class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "pattern": [
                    [1, 4, 7, 10],
                    [2, 5, 8, 11],
                    [3, 6, 9, 12],
                    [13, 14, 15, 16]
                ],
                "task_type": "identify"
            },
            "2": {
                "criteria": "Generate a 4x4 grid pattern where each row and each column contains the numbers 1 to 4 exactly once, and no two adjacent cells (horizontally, vertically, or diagonally) contain consecutive numbers.",
                "task_type": "generate"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task_type"] == "identify":
            return f"""Identify the underlying rule in the following visual pattern and describe it in detail. Your description should be clear and logically organized.

Pattern:
{t['pattern']}

Submit your description as a plain text string in the following format:
'Pattern Rule: [Your description here]'
"""
        elif t["task_type"] == "generate":
            return f"""Generate a visual pattern based on the given criteria. Ensure that the pattern adheres to the specified rules and is logically ordered.

Criteria:
{t['criteria']}

Submit your pattern as a plain text string in the following format:
'Pattern: [[row1], [row2], [row3], [row4]]'
For example, a valid submission format would look like:
Pattern: [[1, 3, 2, 4], [4, 2, 1, 3], [3, 1, 4, 2], [2, 4, 3, 1]]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["task_type"] == "identify":
            validation_criteria = ["The description should accurately capture the underlying rule of the pattern.", "The description should be coherent and logically organized."]
        elif t["task_type"] == "generate":
            validation_criteria = ["The generated pattern should adhere to the given criteria.", "The pattern should be logically ordered and follow the specified rules.", "No adjacent cells (horizontally, vertically, or diagonally) should contain consecutive numbers."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
