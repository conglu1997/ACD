class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"map": "A 5x5 grid where the starting point is at (0, 0) and the destination is at (4, 4). Obstacles are located at (1, 1), (2, 2), and (3, 3)."},
            "2": {"map": "A 6x6 grid where the starting point is at (0, 0) and the destination is at (5, 5). Obstacles are located at (1, 2), (2, 3), and (4, 4)."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Based on the given map, generate clear and precise step-by-step navigation instructions from the starting point to the destination. The instructions should avoid all obstacles and should be in the format 'Move to (x, y)'. Ensure that the instructions are logically coherent, avoid any ambiguity, and represent the shortest valid path. Here is the map: {t['map']}. Example: Move to (0, 1), Move to (1, 1), Move to (2, 1), ... Ensure that all moves are valid and avoid obstacles."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The instructions should provide a clear path from the starting point to the destination.",
            "The instructions should avoid all obstacles.",
            "The steps should be logically coherent and avoid ambiguity.",
            "All moves should be valid and avoid obstacles.",
            "The path should represent the shortest valid route."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
