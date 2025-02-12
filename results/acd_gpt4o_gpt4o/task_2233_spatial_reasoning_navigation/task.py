class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        maze_1 = [
            ['S', ' ', 'X', ' ', ' ', ' '],
            [' ', ' ', 'X', ' ', ' ', 'X'],
            ['X', ' ', ' ', ' ', 'X', ' '],
            [' ', 'X', 'X', ' ', ' ', ' '],
            [' ', ' ', ' ', 'X', ' ', 'E']
        ]
        maze_2 = [
            ['S', 'X', ' ', ' ', 'X', ' '],
            [' ', 'X', 'X', ' ', ' ', ' '],
            [' ', ' ', 'X', 'X', ' ', ' '],
            ['X', ' ', ' ', ' ', 'X', ' '],
            [' ', ' ', ' ', ' ', ' ', 'E']
        ]
        map_1 = [
            ['Home', ' ', ' ', 'Park'],
            [' ', 'Store', ' ', ' '],
            [' ', ' ', 'School', ' '],
            ['Library', ' ', ' ', 'Office']
        ]
        map_2 = [
            ['Home', ' ', ' ', 'Park'],
            [' ', ' ', 'Mall', ' '],
            [' ', 'Store', ' ', ' '],
            ['Library', ' ', ' ', 'Office']
        ]
        return {
            "1": {"type": "maze", "maze": maze_1, "prompt": "Describe a path from the start (S) to the end (E) in the maze. Use directions such as 'up', 'down', 'left', and 'right'. Provide your response in plain text format."},
            "2": {"type": "map", "map": map_2, "prompt": "Give directions from 'Home' to 'Office' using landmarks on the map. Use directions such as 'north', 'south', 'east', and 'west'. Provide your response in plain text format."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['type'] == 'maze':
            return f"""Your task is to describe a path from the start (S) to the end (E) in the maze.

Maze:
{TaskFamily.format_grid(t['maze'])}

Use directions such as 'up', 'down', 'left', and 'right'. Provide your response in plain text format.

Example response format:
'right, down, down, left, down, right, right, right'"""
        elif t['type'] == 'map':
            return f"""Your task is to give directions from 'Home' to 'Office' using landmarks on the map.

Map:
{TaskFamily.format_grid(t['map'])}

Use directions such as 'north', 'south', 'east', and 'west'. Provide your response in plain text format.

Example response format:
'Head east, then go north past the Store, turn east at the Library, and finally head south to reach the Office.'"""

    @staticmethod
    def format_grid(grid: list[list[str]]) -> str:
        return '\n'.join([' '.join(row) for row in grid])

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should accurately describe the path or directions.",
            "The response should use the correct directional language.",
            "The response should be coherent and easy to follow.",
            "The response should match the expected format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
