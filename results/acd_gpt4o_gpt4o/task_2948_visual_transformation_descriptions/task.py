class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"initial_scene": "A simple garden with a tree, flowers, and a pond.", "target_scene": "The same garden with a fountain in place of the pond and a birdhouse on the tree."},
            "2": {"initial_scene": "A kitchen with a dining table, chairs, and a refrigerator.", "target_scene": "The same kitchen with the dining table replaced by a kitchen island and an additional window on the wall."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Your task is to describe the steps required to transform the initial scene into the target scene based on the given descriptions. Here are the descriptions:\n\nInitial Scene: {t['initial_scene']}\nTarget Scene: {t['target_scene']}\n\nProvide a detailed step-by-step transformation in plain text format."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The description should clearly and accurately outline the steps to transform the initial scene into the target scene."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
