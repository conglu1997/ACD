class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"dimensions": [5, 5], "start": [0, 0], "end": [4, 4], "constraints": ["include at least 2 dead ends", "avoid straight paths longer than 3 cells"]},
            "2": {"dimensions": [7, 7], "start": [0, 0], "end": [6, 6], "constraints": ["include at least 3 loops", "use all cells at least once"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to create a maze based on the following criteria:

Dimensions: {t['dimensions'][0]}x{t['dimensions'][1]}
Start: {t['start']}
End: {t['end']}
Constraints: {', '.join(t['constraints'])}

Provide the maze layout using 'O' for open paths and 'X' for walls. Each row of the maze should be represented on a new line, with characters separated by spaces. Also, provide the solution path from start to end as a list of coordinates in the format [(x1, y1), (x2, y2), ...].

Example format:
Maze:
O X O O O
O X X X O
O O O X O
X X O O O
O O O X O

Solution Path: [(0, 0), (0, 2), (1, 2), (2, 2), (2, 3), (2, 4), (3, 4), (4, 4)]

Ensure that your maze adheres to the constraints and that the solution path is valid and navigates through open paths only. The solution path should not pass through walls and should be the shortest valid path."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The maze should match the given dimensions.",
            "The maze should use 'O' for open paths and 'X' for walls.",
            "The solution path should start at the specified start point and end at the specified end point.",
            "The maze should adhere to the given constraints.",
            "The solution path should be valid, navigate through open paths only, and be the shortest valid path."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
