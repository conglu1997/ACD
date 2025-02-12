class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"type": "block_structure", "description": "Imagine a 3x3x3 cube made of smaller 1x1x1 blocks. If you remove all the corner blocks, how many blocks are left?"},
            "2": {"type": "rotation", "description": "Consider a 3D object in the shape of an L. The L-shaped object is composed of three connected cubes: one at (0,0,0), the second at (1,0,0), and the third at (2,0,0). If the object is rotated 90 degrees clockwise around the X-axis, what are the new coordinates of each block?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["type"] == "block_structure":
            return f"""Solve the following 3D spatial reasoning problem: {t['description']} Provide your answer as a single integer representing the number of blocks left."""
        elif t["type"] == "rotation":
            return f"""Solve the following 3D spatial reasoning problem: {t['description']} Provide your answer as a comma-separated list of the new coordinates in the format: 'New Coordinates: (x1,y1,z1), (x2,y2,z2), (x3,y3,z3)'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["type"] == "block_structure":
            criteria = ["The answer should be a single integer.", "The answer should correctly represent the number of blocks left after removing all corner blocks from a 3x3x3 cube."]
        elif t["type"] == "rotation":
            criteria = ["The answer should be a comma-separated list of coordinates.", "The coordinates should accurately reflect the new positions of the blocks after a 90-degree clockwise rotation around the X-axis."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
