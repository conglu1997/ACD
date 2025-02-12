class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "grid_size": [5, 5],
                "start": [0, 0],
                "end": [4, 4],
                "obstacles": [[1, 1], [2, 2], [3, 3]]
            },
            "2": {
                "grid_size": [6, 6],
                "start": [0, 0],
                "end": [5, 5],
                "obstacles": [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to navigate through a grid-based map from the start position to the end position. The grid is represented as a list of lists, where each cell can either be empty or contain an obstacle. You must find the optimal path that adheres to the following rules:\n\n1. You can move up, down, left, or right, but not diagonally.\n2. You cannot move through obstacles.\n3. The path should be as short as possible.\n\nGrid Size: {t['grid_size']}\nStart Position: {t['start']}\nEnd Position: {t['end']}\nObstacles: {t['obstacles']}\n\nProvide your response as a list of coordinates representing the path from start to end. Each coordinate should be in the format [row, column].\n\nExample Response:\n[[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 4], [2, 4], [3, 4], [4, 4]]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        import ast
        try:
            path = ast.literal_eval(submission)
            if not isinstance(path, list):
                return 0.0
            # Check if path starts and ends correctly
            if path[0] != t['start'] or path[-1] != t['end']:
                return 0.0
            # Check if path is valid and adheres to rules
            rows, cols = t['grid_size']
            obstacles = set(tuple(ob) for ob in t['obstacles'])
            for i in range(1, len(path)):
                r, c = path[i]
                prev_r, prev_c = path[i-1]
                if (r, c) in obstacles or not (0 <= r < rows and 0 <= c < cols):
                    return 0.0
                if abs(r - prev_r) + abs(c - prev_c) != 1:  # Must move only one step up, down, left, or right
                    return 0.0
            # Check if path is shortest (strict check)
            from collections import deque
            def bfs(start, end):
                queue = deque([start])
                visited = set([tuple(start)])
                parents = {tuple(start): None}
                while queue:
                    current = queue.popleft()
                    if current == tuple(end):
                        break
                    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        nr, nc = current[0] + dr, current[1] + dc
                        if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and (nr, nc) not in obstacles:
                            queue.append((nr, nc))
                            visited.add((nr, nc))
                            parents[(nr, nc)] = current
                # Reconstruct path
                path = []
                step = tuple(end)
                while step is not None:
                    path.append(list(step))
                    step = parents[step]
                path.reverse()
                return path
            shortest_path = bfs(t['start'], t['end'])
            if path == shortest_path:
                return 1.0
            else:
                return 0.0
        except Exception:
            return 0.0
