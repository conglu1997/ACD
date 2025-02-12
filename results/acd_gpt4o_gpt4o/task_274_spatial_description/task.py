class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"initial_scene": "A room contains a table in the center, a chair to the left of the table, and a bookshelf against the wall."},
            "2": {"initial_scene": "A park has a bench near the entrance, a fountain in the middle, and a playground at the far end."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to describe the given spatial layout or scene and predict the changes based on the specified actions. Here is the initial scene: '{t["initial_scene"]}'. Actions to consider: 1. Move the object closest to the entrance to the opposite side of the space. 2. Add a new object of your choice to the scene. Describe the final scene in detail. Your response should be in the following format:

1. Initial Scene: [description of initial scene]
2. Actions Taken: [description of actions]
3. Final Scene: [detailed description of the final scene]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The submission should correctly describe the initial scene.",
            "The submission should accurately describe the changes based on the actions.",
            "The final scene should be logically consistent with the initial scene and actions described.",
            "The response should follow the specified format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
