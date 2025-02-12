import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"type": "solve", "pieces": [[1,1,0,0,0,0,0], [0,1,1,0,0,0,0], [0,0,1,1,0,0,0], [0,0,0,1,1,0,0], [0,0,0,0,1,1,0], [0,0,0,0,0,1,1], [1,0,0,0,0,0,1]], "target_shape": [[1,1,1,1,1,1,1], [1,0,0,0,0,0,1], [1,0,0,0,0,0,1], [1,0,0,0,0,0,1], [1,0,0,0,0,0,1], [1,0,0,0,0,0,1], [1,1,1,1,1,1,1]]},
            "2": {"type": "construct", "pieces": [[1,1,0,0,0,0,0], [0,1,1,0,0,0,0], [0,0,1,1,0,0,0], [0,0,0,1,1,0,0], [0,0,0,0,1,1,0], [0,0,0,0,0,1,1], [1,0,0,0,0,0,1]], "target_shape": None}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['type'] == 'solve':
            return f"""Your task is to solve the given tangram puzzle. You have the following pieces:
{t['pieces']}

Arrange the pieces to match the target shape:
{t['target_shape']}

Provide your solution as a list of coordinates for each piece, where each coordinate is a tuple (x, y) indicating the top-left corner of the piece on a 7x7 grid. Each piece can only be used once, and they cannot overlap. List the pieces in the same order as given. The pieces should fit exactly within the target shape without any gaps or overlaps. Example response format: [(0, 0), (1, 2), (3, 4), ...]."""
        elif t['type'] == 'construct':
            return f"""Your task is to construct a new tangram puzzle. You have the following pieces:
{t['pieces']}

Arrange the pieces to form a new shape on a 7x7 grid. Provide the coordinates for each piece, where each coordinate is a tuple (x, y) indicating the top-left corner of the piece. Each piece can only be used once, and they cannot overlap. List the pieces in the same order as given. The pieces should fit exactly within the 7x7 grid without any gaps or overlaps. Example response format: [(0, 0), (1, 2), (3, 4), ...]."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []
        if t['type'] == 'solve':
            criteria.append("The solution should correctly match the target shape using all given pieces without any gaps or overlaps.")
        elif t['type'] == 'construct':
            criteria.append("The constructed shape should be valid and use all given pieces without any gaps or overlaps.")
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
