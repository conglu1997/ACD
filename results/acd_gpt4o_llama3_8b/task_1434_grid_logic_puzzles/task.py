class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "grid_size": 4,
                "clues": [
                    "1. The red square is immediately to the right of the blue square.",
                    "2. The green square is in the top-left corner.",
                    "3. The yellow square is directly below the green square."
                ],
                "solution": [
                    ["G", "", "", ""],
                    ["Y", "", "", ""],
                    ["", "", "", ""],
                    ["", "B", "R", ""]
                ]
            },
            "2": {
                "grid_size": 5,
                "clues": [
                    "1. The star is in the center of the grid.",
                    "2. The circle is immediately to the left of the triangle.",
                    "3. The square is directly above the circle.",
                    "4. The hexagon is in the bottom-right corner."
                ],
                "solution": [
                    ["", "", "", "", ""],
                    ["", "", "", "", ""],
                    ["", "", "S", "", ""],
                    ["", "", "C", "T", ""],
                    ["", "", "", "", "H"]
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the following grid-based logic puzzle. Use the given clues to deduce the correct placement of each element in the grid.

Grid Size: {t['grid_size']}x{t['grid_size']}
Clues:
{chr(10).join(t['clues'])}

Provide your solution as a grid with each cell labeled with the corresponding element (e.g., 'R' for red, 'B' for blue, 'G' for green, 'Y' for yellow, 'S' for star, 'C' for circle, 'T' for triangle, 'H' for hexagon). Use the following format for your response:

1. [Your solution for row 1]
2. [Your solution for row 2]
...
{t['grid_size']}. [Your solution for row {t['grid_size']}]

Ensure your solution adheres to all the given clues. Here is an example for a 2x2 grid:

Example Clues:
1. The red square is to the left of the blue square.
2. The green square is above the yellow square.

Example Solution:
1. R B
2. G Y"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        import re
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "Each element's placement must adhere to the given clues.",
            "The grid must be fully completed with no empty cells.",
            "The solution must match the expected grid configuration."
        ]

        # Convert the submission to a grid format
        submission_lines = submission.strip().split('\n')
        submission_grid = [re.split(r'\s+', line.strip())[1:] for line in submission_lines]

        # Validate against the solution
        solution_grid = t['solution']
        for i in range(len(solution_grid)):
            for j in range(len(solution_grid[i])):
                if submission_grid[i][j] != solution_grid[i][j]:
                    return 0.0

        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
