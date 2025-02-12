class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "objects": ["A", "B", "C", "D"],
                "constraints": [
                    "A must be to the left of B",
                    "C must be to the right of A",
                    "D must be between B and C"
                ]
            },
            "2": {
                "objects": ["X", "Y", "Z", "W", "V"],
                "constraints": [
                    "X must be to the left of Y",
                    "Z must be to the right of X",
                    "W must be between Y and Z",
                    "V must be to the right of W"
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        objects = ", ".join(t["objects"])
        constraints = "\n".join(t["constraints"])
        return f"""Arrange the objects in a linear order based on the given constraints. The objects are: {objects}. Here are the constraints:\n{constraints}\n
Submit your arrangement as a plain text string in the following format: [Object1, Object2, Object3, ...]. Ensure that your arrangement satisfies all the constraints."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The arrangement should satisfy all given constraints."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
