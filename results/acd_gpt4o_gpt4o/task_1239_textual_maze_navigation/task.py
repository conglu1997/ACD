class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "maze_description": "Start at the top-left corner of a 5x5 grid. Move right, down, left, or up to navigate. You must reach the bottom-right corner. The grid is as follows:\nS . # . .\n# . # . #\n. . . # .\n# # . . .\n. . . # E"
            },
            "2": {
                "maze_description": "Start at the top-left corner of a 6x6 grid. Move right, down, left, or up to navigate. You must reach the bottom-right corner. The grid is as follows:\nS . # . . #\n# . # . # .\n. . . # . .\n. # # . # .\n. . . . . .\n# . . # . E"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to navigate through the following maze described in textual form. You start at the position marked 'S' and must reach the position marked 'E'. You can move right (R), down (D), left (L), or up (U). Avoid obstacles marked with '#'. Provide the sequence of moves to reach the end.\n\n{t['maze_description']}\n\nFormat your response as follows:\nPath: <sequence of moves>\n\nExample:\nFor a simple 2x2 grid:\nS E\n# .\nThe correct path would be 'R'.\nEnsure your path is correct and avoids obstacles."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The sequence of moves must lead from the start position to the end position.", "The moves must avoid obstacles (#).", "The moves must be valid (R, D, L, U)."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0