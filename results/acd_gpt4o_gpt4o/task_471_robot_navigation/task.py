class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"grid": [[0, 1, 0, 0], [0, 1, 0, 1], [0, 0, 0, 1], [1, 1, 0, 0]], "start": [0, 0], "goal": [3, 3]},
            "2": {"grid": [[0, 0, 0, 0, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 0, 1, 0]], "start": [0, 0], "goal": [4, 4]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to guide a robot through a grid-based maze from the start position {t['start']} to the goal position {t['goal']}. The grid is represented as a list of lists where 0 denotes an open space and 1 denotes an obstacle. Provide a series of movement instructions as a list of strings. The possible movements are 'UP', 'DOWN', 'LEFT', and 'RIGHT'. Make sure the robot does not move into an obstacle or outside the grid.

Provide your response in the following format:
['UP', 'RIGHT', 'RIGHT', 'DOWN', ...]

Here is the grid:
{t['grid']}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        import ast

        def is_valid_path(grid, start, goal, path):
            rows, cols = len(grid), len(grid[0])
            r, c = start
            moves = {'UP': (-1, 0), 'DOWN': (1, 0), 'LEFT': (0, -1), 'RIGHT': (0, 1)}
            for move in path:
                if move not in moves:
                    return False
                dr, dc = moves[move]
                r, c = r + dr, c + dc
                if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 1:
                    return False
            return (r, c) == goal

        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The robot must reach the goal position without moving into obstacles or outside the grid.",
            "The instructions must be a valid sequence of 'UP', 'DOWN', 'LEFT', and 'RIGHT'."
        ]
        try:
            path = ast.literal_eval(submission)
            valid_path = is_valid_path(t['grid'], t['start'], t['goal'], path)
        except:
            valid_path = False
        return 1.0 if valid_path and eval_with_llm_judge(instructions, submission, criteria) else 0.0
