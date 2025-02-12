class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"puzzle": "Identify the shape that fits into the missing spot in the following sequence: circle, square, triangle, hexagon, pentagon, octagon, ?"},
            "2": {"puzzle": "Rotate the 'T' shaped block to fit into the following pattern: [T(0°), T(90°), T(180°), ?]"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to solve the following spatial puzzle:

Puzzle: {t["puzzle"]}

Provide your solution in plain text format, ensuring that your answer is coherent and correctly solves the puzzle. Specify the missing shape or the correct rotation as appropriate. For example, 'Missing shape: heptagon' or 'Rotation: 270 degrees clockwise'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The solution must correctly solve the puzzle.", "The solution must be coherent and clearly stated."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
