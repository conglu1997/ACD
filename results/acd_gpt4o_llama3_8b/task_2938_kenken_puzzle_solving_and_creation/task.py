class TaskFamily:
    import itertools
    import re

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "type": "solve",
                "puzzle": "4x4 KenKen Puzzle:\n1. Cage with cells (1,1) and (1,2), target 3, operation +\n2. Cage with cells (1,3), target 1, operation none\n3. Cage with cells (1,4) and (2,4), target 4, operation /\n4. Cage with cells (2,1) and (3,1), target 2, operation -\n5. Cage with cells (2,2), target 3, operation none\n6. Cage with cells (2,3), (3,3) and (4,3), target 24, operation *\n7. Cage with cells (3,2) and (4,2), target 4, operation /\n8. Cage with cells (3,4) and (4,4), target 3, operation -\n9. Cage with cells (4,1), target 1, operation none"
            },
            "2": {
                "type": "create",
                "size": "4x4",
                "cages": "\n1. Cage with 2 cells, target 3, operation +\n2. Cage with 1 cell, target 1\n3. Cage with 2 cells, target 4, operation /\n4. Cage with 2 cells, target 2, operation -\n5. Cage with 1 cell, target 3\n6. Cage with 3 cells, target 24, operation *\n7. Cage with 2 cells, target 4, operation /\n8. Cage with 2 cells, target 3, operation -\n9. Cage with 1 cell, target 1"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['type'] == 'solve':
            return f"""Solve the following KenKen puzzle. Ensure that no digits repeat in any row or column, and that the digits within each outlined region (cage) combine to form the specified target number using the specified arithmetic operation.

Puzzle:
{t['puzzle']}

Submit your solution as a plain text string in the following format:

Solution:
[[row1], [row2], [row3], [row4]]
Each row should be a list of four integers, representing the values in the cells from left to right."""
        elif t['type'] == 'create':
            return f"""Create a KenKen puzzle with the specified size and cages. Ensure that the puzzle is solvable and that no digits repeat in any row or column. Each cage should combine to form the specified target number using the specified arithmetic operation.

Size: {t['size']}
Cages:
{t['cages']}

Submit your puzzle as a plain text string in the following format:

Puzzle:
[[row1], [row2], [row3], [row4]]
Each row should be a list of four integers, representing the values in the cells from left to right."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['type'] == 'solve':
            criteria = ["The solution should ensure no digits repeat in any row or column.", "The digits within each cage should combine to form the specified target number using the specified arithmetic operation."]
        elif t['type'] == 'create':
            criteria = ["The created puzzle should be solvable.", "No digits should repeat in any row or column.", "The digits within each cage should combine to form the specified target number using the specified arithmetic operation."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0