class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"grid": [
                ["S", "0", "1", "0", "0", "1", "E"],
                ["1", "0", "1", "1", "0", "1", "0"],
                ["0", "0", "0", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0", "1", "1"],
                ["0", "0", "0", "1", "0", "0", "0"]
            ]},
            "2": {"grid": [
                ["S", "1", "0", "1", "0", "1", "E"],
                ["0", "1", "0", "1", "0", "1", "0"],
                ["0", "0", "0", "0", "0", "0", "0"],
                ["1", "1", "1", "1", "1", "1", "0"],
                ["0", "0", "0", "0", "0", "0", "0"],
                ["0", "1", "0", "1", "0", "1", "0"],
                ["0", "0", "0", "0", "0", "0", "0"]
            ]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return "Find the shortest path from the start point 'S' to the endpoint 'E' on the given 2D grid. The grid is represented as a list of lists, where '0' indicates a free cell, '1' indicates an obstacle, 'S' is the start point, and 'E' is the endpoint. Submit the path as a list of coordinates in the form [(row1, col1), (row2, col2), ..., (rowN, colN)], where each coordinate represents a step in the path. Ensure that the path is the shortest possible route and adheres to the grid constraints. You may only move up, down, left, or right, and cannot move diagonally or through obstacles."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        try:
            grid = t['grid']
            instructions = TaskFamily.get_instructions(t)
            correct_path = TaskFamily.find_shortest_path(grid)
            submitted_path = eval(submission)
            return 1.0 if submitted_path == correct_path else 0.0
        except Exception:
            return 0.0

    @staticmethod
    def find_shortest_path(grid: list[list[str]]) -> list[tuple[int, int]]:
        from collections import deque
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        start, end = None, None
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "S":
                    start = (r, c)
                elif grid[r][c] == "E":
                    end = (r, c)
        if not start or not end:
            raise ValueError("Grid must have a start (S) and end (E) point.")
        queue = deque([(start, [start])])
        visited = set([start])
        while queue:
            (current_pos, path) = queue.popleft()
            if current_pos == end:
                return path
            for direction in directions:
                new_r, new_c = current_pos[0] + direction[0], current_pos[1] + direction[1]
                if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] != "1" and (new_r, new_c) not in visited:
                    visited.add((new_r, new_c))
                    queue.append(((new_r, new_c), path + [(new_r, new_c)]))
        return []  # No path found
