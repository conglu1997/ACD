class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task": "calculate_area", "description": "A rectangle has a length of 8 units and a width of 5 units. Calculate its area."},
            "2": {"task": "describe_transformation", "description": "A triangle with vertices at (0,0), (1,0), and (0,1) is reflected over the y-axis. Describe the coordinates of the vertices of the transformed triangle."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task"] == "calculate_area":
            return f"Your task is to calculate the area of a geometric shape based on the following description:\n\n{t['description']}\n\nSubmit your answer in plain text format."
        elif t["task"] == "describe_transformation":
            return f"Your task is to describe the transformation of a geometric shape based on the following description:\n\n{t['description']}\n\nSubmit your answer in plain text format."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["task"] == "calculate_area":
            criteria = ["The response should correctly calculate the area as 40 square units."]
        elif t["task"] == "describe_transformation":
            criteria = ["The response should correctly describe the transformed coordinates as (0,0), (-1,0), and (0,1)."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
