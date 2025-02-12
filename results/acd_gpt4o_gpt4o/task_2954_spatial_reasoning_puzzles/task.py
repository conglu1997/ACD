class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"puzzle": "A 3x3 grid is shown with some cells filled and some empty. The task is to complete the grid based on specific rules.", "grid": [[1, 0, 1], [0, 1, 0], [1, 0, "?"]], "rules": "Each row and column should have exactly two 1s and one 0."},
            "2": {"puzzle": "A sequence of shapes is shown. The task is to determine the next shape in the sequence.", "sequence": ["circle", "square", "triangle", "circle", "square", "?"], "rules": "Identify the pattern and determine the next shape."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "grid" in t:
            return f"""Solve the following spatial reasoning puzzle:

Puzzle: {t['puzzle']}
Grid: {t['grid']}
Rules: {t['rules']}

Provide your solution by filling in the missing cell in the grid. Your response should be a 3x3 grid with each cell filled based on the rules provided. For example, if the initial grid is [[1, 0, 1], [0, 1, 0], [1, 0, "?"]], you might submit [[1, 0, 1], [0, 1, 0], [1, 0, 0]] if that follows the rules."""
        else:
            return f"""Solve the following spatial reasoning puzzle:

Puzzle: {t['puzzle']}
Sequence: {', '.join([shape if shape is not None else '?' for shape in t['sequence']])}
Rules: {t['rules']}

Provide your solution by identifying the next shape in the sequence. Your response should be a single word representing the shape, such as 'triangle'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "grid" in t:
            criteria = ["The completed grid should follow the rules provided."]
        else:
            criteria = ["The identified shape should correctly follow the pattern in the sequence."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
