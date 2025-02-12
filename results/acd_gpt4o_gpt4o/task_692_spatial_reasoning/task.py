class TaskFamily:
    import random
    from typing import List, Tuple

    @staticmethod
    def generate_shapes() -> List[str]:
        import random
        shapes = ['cube', 'sphere', 'pyramid', 'cylinder']
        return [random.choice(shapes) for _ in range(3)]

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"shapes": TaskFamily.generate_shapes(), "type": "rotate"},
            "2": {"shapes": TaskFamily.generate_shapes(), "type": "combine"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['type'] == 'rotate':
            return f"""Your task is to visualize the following 3D shapes and determine their final orientation after a series of specified rotations. Describe the final orientation of each shape in relation to its initial position. Use the terms 'front', 'back', 'left', 'right', 'top', and 'bottom' to describe the orientations.

Shapes: {', '.join(t['shapes'])}

For instance, if a cube is rotated 90 degrees to the right, describe which face is now in the 'front' position. Provide your response in the following format:

- Shape 1 (initial position): [final orientation]
- Shape 2 (initial position): [final orientation]
- Shape 3 (initial position): [final orientation]"""
        elif t['type'] == 'combine':
            return f"""Your task is to visualize how to combine the following 3D shapes into a single composite shape. Describe the final composite shape and the spatial relationships between the original shapes. Use the terms 'adjacent', 'above', 'below', 'next to', etc., to describe the spatial relationships.

Shapes: {', '.join(t['shapes'])}

For instance, if a sphere is placed above a cube and a cylinder is placed next to the cube, describe the final arrangement. Provide your response in the following format:

- Shape 1: [spatial relationship]
- Shape 2: [spatial relationship]
- Shape 3: [spatial relationship]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0
