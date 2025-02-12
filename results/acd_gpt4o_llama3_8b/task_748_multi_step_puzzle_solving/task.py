class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "description": "You are given a 4x4 grid with the following numbers: 1, 2, 3, 4. Each row and column must contain each number exactly once. Fill in the missing numbers: \n\n| 1 | 2 |   | 4 |\n|   |   | 4 |   |\n|   | 4 |   | 2 |\n| 4 |   | 2 | 1 |"
            },
            "2": {
                "description": "You need to distribute 5 distinct items (A, B, C, D, E) into 5 boxes such that no item is placed in the box with the same index number (e.g., item A cannot be in box 1). Provide a valid distribution."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the following multi-step logical puzzle based on the given description and constraints:\n\nDescription:\n{t['description']}\n\nFor Task 1, submit your solution as a 4x4 grid with numbers filled in. For example:\n| 1 | 2 | 3 | 4 |\n| 3 | 1 | 4 | 2 |\n| 2 | 4 | 1 | 3 |\n| 4 | 3 | 2 | 1 |\n\nFor Task 2, submit your solution as a list of item-box pairs. For example: 'A-2, B-3, C-4, D-5, E-1'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The solution for Task 1 must correctly fill in the grid according to the rules.",
            "The solution for Task 2 must correctly assign each item to a box such that no item is in the box with the same index number."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
