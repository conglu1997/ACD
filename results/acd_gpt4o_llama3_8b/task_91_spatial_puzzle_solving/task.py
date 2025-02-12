class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "You have a 3x3 grid. Place numbers 1 to 9 in the grid such that each row, column, and diagonal sums to 15.", "solution": [[8, 1, 6], [3, 5, 7], [4, 9, 2]]},
            "2": {"description": "You have a 4x4 grid. Place the letters A, B, C, and D in each row and column such that no letter repeats in any row or column.", "solution": [["A", "B", "C", "D"], ["B", "C", "D", "A"], ["C", "D", "A", "B"], ["D", "A", "B", "C"]]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the following spatial puzzle: {t["description"]} Submit your solution as a nested list representation of the grid in the following format:
[[row1_element1, row1_element2, ...], [row2_element1, row2_element2, ...], ...]. Ensure that your solution meets the conditions specified in the puzzle description."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        solution = t["solution"]
        criteria = [f"The solution must be a nested list representation of the grid.", f"The solution must match the grid: {solution}"]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
