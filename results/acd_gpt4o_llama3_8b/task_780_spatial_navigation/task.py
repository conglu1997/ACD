class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"maze_description": "You are at the entrance of a maze. Move forward 3 steps, turn left, move forward 2 steps, turn right, move forward 1 step, and then turn left again. Describe your final position relative to the starting point."},
            "2": {"maze_description": "You are in the middle of a forest with paths in all directions. Move north for 2 steps, then turn east and move 3 steps. Next, turn south and walk 1 step, then turn west and move 2 steps. Describe your final position relative to the starting point."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Navigate through the described maze or pathway by providing step-by-step directions based on the given spatial instructions:

Maze Description: {t['maze_description']}

Ensure that your directions are clear, accurate, and follow the given instructions exactly. Submit your final position as a plain text string describing your location relative to the starting point in the format 'x steps [direction] and y steps [direction] from starting point'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The final position should be correctly described relative to the starting point."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
