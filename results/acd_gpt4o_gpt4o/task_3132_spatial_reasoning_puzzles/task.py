class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"puzzle": "Given a 3x3 grid with the following layout: \n\n1 2 3\n4 5 6\n7 8 9\n\nIf you rotate the grid 90 degrees clockwise, what will be the new positions of the numbers? Provide the new grid layout in the same format."},
            "2": {"puzzle": "You have a T-shaped piece that fits into a 4x4 grid. The T-shape occupies the following coordinates: \n\n(1,2), (2,1), (2,2), (2,3), (3,2)\n\nIf you mirror the T-shape along the vertical axis, what will be the new coordinates? Provide the new coordinates in the same format."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to solve the following spatial reasoning puzzle:\n\n{t['puzzle']}\n\nEnsure your response is clear and follows the specified format. Provide the new grid layout or coordinates in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "rotate" in t['puzzle']:
            criteria = ["The response should correctly provide the new positions of the numbers in the grid after a 90-degree clockwise rotation."]
        elif "mirror" in t['puzzle']:
            criteria = ["The response should correctly provide the new coordinates of the T-shape after mirroring along the vertical axis."]
        else:
            criteria = []
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
