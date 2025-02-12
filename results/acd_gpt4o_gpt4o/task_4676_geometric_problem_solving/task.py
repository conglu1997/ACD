class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem": "Calculate the area and perimeter of a rectangle with a length of 8 units and a width of 5 units. Then, determine the length of the diagonal of the rectangle.", "type": "area_perimeter_diagonal"},
            "2": {"problem": "Calculate the volume and surface area of a cylinder with a radius of 3 units and a height of 7 units. Then, determine the lateral surface area of the cylinder.", "type": "volume_surface_area_lateral"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to solve the following geometric problem. Calculate the required geometric properties based on the given parameters. Show all your calculations and provide the final answers.

Problem: {t['problem']}

Provide your response in the following format:

- Calculations: [Your step-by-step calculations]
- Final Answers: [Your final answers]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The calculations should be correct and logical.", "The final answers should be accurate based on the given problem."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
