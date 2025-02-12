class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "A cube with a side length of 3 units. The cube is centered at the origin (0, 0, 0) and has its faces parallel to the coordinate planes. Additionally, there is a smaller cube with a side length of 1 unit placed at the center of the top face of the larger cube. There is also a sphere with a radius of 0.5 units tangentially attached to the center of one face of the smaller cube."},
            "2": {"description": "A cylinder with a radius of 2 units and a height of 5 units. The cylinder is standing upright on the XY-plane with its base centered at (0, 0, 0). Additionally, there is a cone with the same radius and a height of 3 units placed on top of the cylinder, with its base matching the top of the cylinder. There is also a torus with a major radius of 1.5 units and a minor radius of 0.5 units centered around the cylinder at its midpoint."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a detailed description of the following 3D object based on the given spatial information. Ensure that the description is exhaustive, clear, and includes all relevant details. Here is the information about the object:\n\n{t['description']}\n\nSubmit your description in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The description should accurately represent the 3D object.", "The description should be clear and written in proper English.", "All relevant spatial details should be included.", "The description should be exhaustive."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
