class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "Describe the spatial relationship between three objects: a cube, a sphere, and a pyramid. The cube has a side length of 4 units and is centered at the origin (0, 0, 0). The sphere has a radius of 2 units and is tangentially attached to one face of the cube. The pyramid has a square base with a side length of 3 units and a height of 5 units. It is placed on top of the cube such that the centers of their bases coincide. Additionally, there is a small cone with a height of 2 units and a base radius of 1 unit that is positioned on the top face of the pyramid with its base centered at the apex of the pyramid."},
            "2": {"description": "Describe the spatial configuration of four cylinders. Cylinder A has a height of 10 units and a radius of 2 units and is positioned vertically along the z-axis with its base centered at (0, 0, 0). Cylinder B has a height of 8 units and a radius of 1.5 units and is positioned horizontally along the x-axis with its center at (5, 0, 4). Cylinder C has a height of 6 units and a radius of 1 unit and is positioned horizontally along the y-axis with its center at (0, 5, 6). Cylinder D has a height of 4 units and a radius of 0.5 units and is positioned vertically along the z-axis with its base centered at (2, 2, 0). Additionally, there is a small sphere with a radius of 1 unit centered at (3, 3, 3) that is not intersecting any of the cylinders."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        description = t["description"]
        instructions = f"""Your task is to generate a detailed description of the spatial relationship and configuration based on the following information:

{description}

Ensure that the description is exhaustive, clear, and includes all relevant spatial details. Provide your description in plain text format, using complete sentences and paragraphs."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The description should accurately reflect the spatial relationships and positions of the objects.",
            "The description should be clear and detailed.",
            "The description should include all relevant spatial details mentioned in the task." 
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
