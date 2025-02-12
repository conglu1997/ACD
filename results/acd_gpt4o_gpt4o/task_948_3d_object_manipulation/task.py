class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"type": "describe", "prompt": "Describe a cube with a smaller cube removed from one of its corners."},
            "2": {"type": "manipulate", "prompt": "Imagine a pyramid with a square base. Describe the resulting shape if the top half is cut off parallel to the base."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["type"] == "describe":
            return f"""Your task is to describe the given 3D object in detail. Imagine a cube with a smaller cube removed from one of its corners. Provide a detailed description of how the object looks, including information about the changes in its faces and edges. Structure your response in the following format: \n- Overview of the shape \n- Description of faces \n- Description of edges \n- Any other notable features."""
        else:
            return f"""Your task is to manipulate the given 3D object based on the described operation. Imagine a pyramid with a square base. Describe the resulting shape if the top half is cut off parallel to the base. Provide a detailed description of the new shape, including its faces and edges. Structure your response in the following format: \n- Overview of the transformation \n- Description of the new shape \n- Description of faces \n- Description of edges \n- Any other notable features."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["type"] == "describe":
            criteria = ["The response should accurately describe the cube with a smaller cube removed from one of its corners.", "The description should include changes in faces and edges."]
        else:
            criteria = ["The response should accurately describe the resulting shape of the pyramid after the top half is cut off parallel to the base.", "The description should include changes in faces and edges."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
