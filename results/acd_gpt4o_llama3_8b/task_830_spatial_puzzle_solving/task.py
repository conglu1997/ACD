class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "puzzle": "Maze",
                "description": "You are in a maze with the following structure:\n\nS . . # . .\n# # . # . #\n. . . . . .\n. # # # . .\n. . . E . #\n\n'S' is the start point and 'E' is the end point. '.' represents a walkable path and '#' represents a wall. Provide the sequence of moves (up, down, left, right) to reach 'E' from 'S'. No diagonal moves are allowed. Format your response as a comma-separated string (e.g., 'right, right, down, down')."
            },
            "2": {
                "puzzle": "Block Arrangement",
                "description": "You have the following blocks: [A, B, C, D]. Arrange these blocks in a 2x2 grid such that the sum of the numbers on each side of the grid is equal. Each block has the following numbers on its sides (top, right, bottom, left):\nA: (1, 2, 1, 2)\nB: (2, 1, 2, 1)\nC: (1, 1, 2, 2)\nD: (2, 2, 1, 1)\nProvide the arrangement of blocks in the format:\nTop-Left: [Block, rotation]\nTop-Right: [Block, rotation]\nBottom-Left: [Block, rotation]\nBottom-Right: [Block, rotation]\nwhere rotation indicates the number of 90-degree clockwise turns from the initial position. Ensure that the sum of the numbers on all adjacent sides of the grid is equal. For example, if Block A is placed at the Top-Left with no rotation, it should be represented as 'Top-Left: [A, 0]'."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the following spatial puzzle based on the given description:\n\n{t['description']}\n\nSubmit your response as a plain text string in the appropriate format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['puzzle'] == 'Maze':
            criteria = ["The sequence of moves should correctly navigate from 'S' to 'E' without hitting any walls.", "The format of the response should be a comma-separated string of moves.", "No diagonal moves should be included."]
        elif t['puzzle'] == 'Block Arrangement':
            criteria = [
                "The arrangement of blocks should ensure that the sums of the numbers on all adjacent sides of the grid are equal.",
                "The format should be 'Top-Left: [Block, rotation]', 'Top-Right: [Block, rotation]', 'Bottom-Left: [Block, rotation]', and 'Bottom-Right: [Block, rotation]'."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
