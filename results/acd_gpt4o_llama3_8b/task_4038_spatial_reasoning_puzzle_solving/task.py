class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"puzzle": "3x3 sliding puzzle", "initial_state": "1 2 3 4 5 6 7 8 0", "goal_state": "1 2 3 4 5 6 7 0 8"},
            "2": {"puzzle": "4x4 sliding puzzle", "initial_state": "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 0", "goal_state": "1 2 3 4 5 6 7 8 9 10 11 12 13 14 0 15"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are provided with a {t['puzzle']} where the tiles are numbered and 0 represents the empty space. The initial state of the puzzle is {t['initial_state']}. Your task is to describe the sequence of moves needed to achieve the goal state {t['goal_state']}. Use the following format for each move: 'Move tile X to the empty space.' Ensure that your sequence is correct and leads directly from the initial state to the goal state without any extraneous steps. Each move should be valid for the current state of the puzzle.

Submit your moves as a plain text string in the following format:

Moves:
1. Move tile X to the empty space.
2. Move tile Y to the empty space.
...

Example:
Moves:
1. Move tile 8 to the empty space.
2. Move tile 5 to the empty space.
3. Move tile 2 to the empty space.
..."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0
