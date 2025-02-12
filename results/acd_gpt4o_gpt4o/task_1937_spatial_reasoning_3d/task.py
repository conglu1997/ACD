class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "Visualize a cube with edges labeled from 1 to 12. Describe the order of edges encountered if you walk along the edges starting from edge 1 and moving in a clockwise direction around the cube.", "task_type": "visualization"},
            "2": {"description": "Imagine a pyramid with a square base. The vertices of the base are labeled A, B, C, and D, and the apex is labeled E. Describe the sequence of faces you would encounter if you walk from vertex A to vertex E, touching each face once.", "task_type": "visualization"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        description = t["description"]
        instructions = f"""Your task is to interpret and visualize the following 3D object based on the given description:\n\nDescription:\n{description}\n\nProvide your response in plain text format, ensuring that your description is clear, accurate, and follows the given scenario. Format your response as follows:\n\nResponse:\n[Your description here]\n\nExample:\nResponse:\n1 -> 2 -> 3 -> ..."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should accurately describe the sequence of edges or faces as per the given scenario.",
            "The response should be coherent and logically consistent.",
            "The response should follow the specified format."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
