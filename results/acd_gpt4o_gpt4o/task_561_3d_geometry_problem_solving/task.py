class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"shape": "sphere", "radius": 5},
            "2": {"shape": "cuboid", "length": 4, "width": 3, "height": 2}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['shape'] == 'sphere':
            return f"""Your task is to solve the following 3D geometry problem involving a sphere.

Given a sphere with a radius of {t['radius']} units, calculate the following:
1. Volume of the sphere
2. Surface area of the sphere

Provide your answers in the following format:
Volume: [Your answer]
Surface Area: [Your answer]"""
        elif t['shape'] == 'cuboid':
            return f"""Your task is to solve the following 3D geometry problem involving a cuboid.

Given a cuboid with dimensions length = {t['length']} units, width = {t['width']} units, and height = {t['height']} units, calculate the following:
1. Volume of the cuboid
2. Surface area of the cuboid

Provide your answers in the following format:
Volume: [Your answer]
Surface Area: [Your answer]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        import math
        instructions = TaskFamily.get_instructions(t)
        criteria = []
        if t['shape'] == 'sphere':
            volume = (4/3) * math.pi * (t['radius'] ** 3)
            surface_area = 4 * math.pi * (t['radius'] ** 2)
            criteria = [f"The volume should be approximately {volume}.", f"The surface area should be approximately {surface_area}."]
        elif t['shape'] == 'cuboid':
            volume = t['length'] * t['width'] * t['height']
            surface_area = 2 * (t['length'] * t['width'] + t['width'] * t['height'] + t['length'] * t['height'])
            criteria = [f"The volume should be {volume}.", f"The surface area should be {surface_area}."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
