class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "task_type": "generate",
                "criteria": "Generate a logical puzzle involving a grid of numbers where the sum of each row and column must be equal. The grid should be 3x3. Provide the initial state of the grid with some numbers filled in and others left blank."
            },
            "2": {
                "task_type": "solve",
                "puzzle": "Fill in the blanks with numbers 1 to 9 such that the sum of each row and column is equal. Grid: [5, 3, _, _, 7, _, _, _, 2]"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task_type"] == "generate":
            return f"""Generate a logical puzzle based on the following criteria: {t['criteria']}.

Provide the puzzle in the following format:
Puzzle: [1st row, 2nd row, 3rd row]
Example: Puzzle: [5, 3, _, _, 7, _, _, _, 2]
"""
        elif t["task_type"] == "solve":
            return f"""Solve the following logical puzzle:

Puzzle: {t['puzzle']}

Provide your solution in the following format:
Solution: [1st row, 2nd row, 3rd row]
Example: Solution: [5, 3, 7, 2, 7, 6, 4, 9, 2]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["task_type"] == "generate":
            validation_criteria = ["The generated puzzle must involve a grid of numbers where the sum of each row and column is equal.", "The grid should be 3x3.", "Provide the initial state of the grid with some numbers filled in and others left blank."]
        elif t["task_type"] == "solve":
            validation_criteria = ["The solution should fill the grid with numbers 1 to 9 such that the sum of each row and column is equal."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
