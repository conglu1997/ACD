class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"environment": [[0, 1, 0], [0, 0, 0], [1, 0, 0]], "start": (0, 0), "end": (2, 2)},
            "2": {"environment": [[0, 0, 1, 0], [1, 0, 0, 0], [0, 1, 0, 1], [0, 0, 0, 0]], "start": (0, 0), "end": (3, 3)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to navigate through a simulated environment represented as a grid. The grid has the following properties:
        1. '0' represents a free cell where you can move.
        2. '1' represents an obstacle that you cannot pass through.
        
        You start at the position {t['start']} and your goal is to reach the end position {t['end']}.
        Provide your navigation path as a list of moves in the format [(x1, y1), (x2, y2), ...] where each tuple represents your position in the grid at each step.
        
        Example: [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)]
        
        Note:
        1. You can move up, down, left, or right but not diagonally.
        2. Ensure that you avoid obstacles and do not move out of the grid bounds.
        3. Provide the shortest path possible if there is more than one path.
        4. Your path should not contain repeated positions.
        """

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        import ast
        from collections import deque
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The path must avoid obstacles.", "The path must start at the start position and end at the end position.", "The path must be the shortest possible.", "The path should not contain repeated positions."]
        try:
            path = ast.literal_eval(submission)
            if not isinstance(path, list) or not all(isinstance(move, tuple) and len(move) == 2 and all(isinstance(coord, int) for coord in move) for move in path):
                return 0.0

            # Validate the path according to the environment
            env = t['environment']
            start, end = t['start'], t['end']
            if path[0] != start or path[-1] != end:
                return 0.0

            visited_positions = set()
            current_position = start
            for move in path[1:]:
                if abs(move[0] - current_position[0]) + abs(move[1] - current_position[1]) != 1:  # Check for valid move
                    return 0.0
                if env[move[0]][move[1]] == 1:  # Check for obstacles
                    return 0.0
                if move in visited_positions:  # Check for repeated positions
                    return 0.0
                visited_positions.add(move)
                current_position = move

            # Check if the path is the shortest path
            def bfs_shortest_path(env, start, end):
                rows, cols = len(env), len(env[0])
                queue = deque([(start, 0)])
                visited = set([start])
                directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                while queue:
                    (current, distance) = queue.popleft()
                    if current == end:
                        return distance
                    for d in directions:
                        next_move = (current[0] + d[0], current[1] + d[1])
                        if 0 <= next_move[0] < rows and 0 <= next_move[1] < cols and env[next_move[0]][next_move[1]] == 0 and next_move not in visited:
                            visited.add(next_move)
                            queue.append((next_move, distance + 1))
                return float('inf')

            shortest_path_length = bfs_shortest_path(env, start, end)
            if len(path) - 1 != shortest_path_length:
                return 0.0
        except (ValueError, SyntaxError):
            return 0.0

        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
