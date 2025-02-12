class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "description": "Imagine a cube where each face is colored differently: red, blue, green, yellow, white, and black. Describe how the cube would look if you start with the red face facing you, then rotate the cube 90 degrees to the right. Clearly state the colors of the faces that are visible to you after this rotation."
            },
            "2": {
                "description": "Visualize a pyramid with a square base. The base is colored orange, and each of the four triangular faces is colored differently: purple, brown, gray, and pink. Describe the colors of the faces you see when the pyramid is placed on the orange base and viewed from directly in front of one of the triangular faces. Clearly state the colors of the faces that are visible to you from this angle."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Describe and manipulate the given 3D object based on the following description. Provide your solution in a clear and concise manner.\n\nDescription:\n{t['description']}\n\nFormat your response as follows:\nFor Task 1, describe the colors of each visible face of the cube after the rotation.\nFor Task 2, describe the colors of the visible faces of the pyramid from the specified angle. Ensure your descriptions are logically consistent and accurately reflect the transformations described."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The solution should describe the colors of the visible faces correctly.",
            "The solution should be based on the given transformations.",
            "The description should be logically consistent with the described spatial transformations."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
