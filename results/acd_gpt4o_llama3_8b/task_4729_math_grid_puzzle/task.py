class TaskFamily:
    from typing import Optional

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "grid": [[0, 2, 0], [3, 0, 1], [0, 1, 0]],
                "rule": "Fill the grid such that each row, column, and diagonal add up to the same number."
            },
            "2": {
                "grid": [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                "rule": "Create a 4x4 grid puzzle where each row, column, and diagonal add up to 10."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "rule" in t and "grid" in t:
            grid_str = '\n'.join([' '.join(map(str, row)) for row in t['grid']])
            return f"Solve the following mathematical grid puzzle based on the given rule:\n\nGrid:\n{grid_str}\n\nRule:\n{t['rule']}\n\nSubmit your solution as a series of rows, each represented by a list of numbers (e.g., [[1, 2, 3], [4, 5, 6], [7, 8, 9]])."
        elif "rule" in t:
            return f"Create a new mathematical grid puzzle based on the given rule and submit your grid as a series of rows, each represented by a list of numbers (e.g., [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])."
        else:
            return ""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "rule" in t and "grid" in t:
            criteria = [
                "The solution must follow the given rule.",
                "The grid must be correctly filled based on the rule."
            ]
        else:
            criteria = [
                "The created grid must follow the given rule.",
                "The new grid must be a valid 4x4 grid."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
