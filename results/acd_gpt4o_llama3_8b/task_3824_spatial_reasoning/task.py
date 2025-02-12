class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "Arrange the following objects in a 3x3 grid such that no two identical objects are in the same row, column, or diagonal.", "objects": ["A", "B", "C", "A", "B", "C", "A", "B", "C"], "grid_size": 3},
            "2": {"description": "Place the following objects in a 4x4 grid such that each row and column contains exactly one of each object, and no two identical objects are in the same major diagonal.", "objects": ["1", "2", "3", "4", "1", "2", "3", "4", "1", "2", "3", "4", "1", "2", "3", "4"], "grid_size": 4}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        description = t["description"]
        objects = t["objects"]
        grid_size = t["grid_size"]
        return f"""{description} The objects to be arranged are: {', '.join(objects)}. Submit your solution as a plain text string representing the grid, with rows separated by newlines and objects separated by spaces. For example, a 3x3 grid solution might look like this:

A B C
B C A
C A B"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        objects = t["objects"]
        grid_size = t["grid_size"]
        object_set = set(objects)
        rows = submission.strip().split('\n')
        if len(rows) != grid_size:
            return 0.0
        grid = [row.split() for row in rows]
        if any(len(row) != grid_size for row in grid):
            return 0.0
        for row in grid:
            if any(elem not in object_set for elem in row):
                return 0.0
            if len(set(row)) != grid_size:
                return 0.0
        for col_idx in range(grid_size):
            column = [grid[row_idx][col_idx] for row_idx in range(grid_size)]
            if len(set(column)) != grid_size:
                return 0.0
        diagonals = [[grid[i][i] for i in range(grid_size)], [grid[i][grid_size - 1 - i] for i in range(grid_size)]]
        for diagonal in diagonals:
            if len(set(diagonal)) != grid_size:
                return 0.0
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0
