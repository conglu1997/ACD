class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"puzzle_type": "sequence", "sequence": [1, 1, 2, 3, 5, 8, 13]},
            "2": {"puzzle_type": "grid", "grid_size": 3, "grid": [[1, 2, 3], [4, 0, 5], [6, 7, 8]], "goal_state": [[1, 2, 3], [4, 5, 6], [7, 8, 0]]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['puzzle_type'] == 'sequence':
            return f"""Your task is to identify the pattern in the given sequence of numbers and provide the next number in the sequence.

Sequence: {t['sequence']}

Instructions:
1. Analyze the given sequence of numbers.
2. Identify the pattern or rule governing the sequence.
3. Provide the next number in the sequence.

Your response should be in the following format:
Next Number: [Your answer]"""
        elif t['puzzle_type'] == 'grid':
            grid_display = '\n'.join([' '.join(map(str, row)) for row in t['grid']])
            goal_display = '\n'.join([' '.join(map(str, row)) for row in t['goal_state']])
            return f"""Your task is to solve the given sliding puzzle and provide the sequence of moves required to reach the goal state.

Grid Size: {t['grid_size']}x{t['grid_size']}
Initial Grid:\n{grid_display}
Goal State:\n{goal_display}

Instructions:
1. Analyze the initial grid and the goal state.
2. Determine a sequence of moves to reach the goal state.
3. Provide the sequence of moves in the format: U (up), D (down), L (left), R (right).

Your response should be in the following format:
Moves: [Your sequence of moves]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['puzzle_type'] == 'sequence':
            correct_answer = 21
            criteria = ["The next number in the sequence should be a correct continuation of the pattern."]
        elif t['puzzle_type'] == 'grid':
            criteria = ["The sequence of moves should correctly solve the puzzle and reach the goal state."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
