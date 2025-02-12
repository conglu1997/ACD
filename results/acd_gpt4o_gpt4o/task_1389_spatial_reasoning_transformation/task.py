class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"initial_scene": "A desk with a computer monitor on it, a chair in front of the desk, a bookshelf to the right of the desk, and a plant in the corner.", "transformations": "Move the chair to the left side of the desk. Place a lamp on the desk to the left of the computer monitor. Move the plant to the opposite corner."},
            "2": {"initial_scene": "A kitchen with a table in the center, four chairs around the table, a fridge to the left of the table, a sink to the right of the table, and a microwave on the countertop.", "transformations": "Move the fridge to the opposite side of the room. Add a cupboard next to the sink on the right side. Place the microwave inside the new cupboard."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        initial_scene = t["initial_scene"]
        transformations = t["transformations"]
        instructions = f"""Your task is to describe the final scene after applying the specified transformations to the initial scene.\n\nInitial Scene: {initial_scene}\nTransformations: {transformations}\n\nEnsure that your description of the final scene is detailed, coherent, and accurately reflects the transformations provided. The description should not include any elements that were not specified in the transformations. Provide your response in plain text format, structured as follows:\n\n1. Initial Scene: [Description of the initial scene]\n2. Actions Taken: [Description of the transformations applied]\n3. Final Scene: [Description of the final scene after transformations]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The final scene description should accurately reflect the initial scene after the specified transformations.",
            "The description should be detailed and coherent.",
            "The description should not include any elements that were not specified in the transformations."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
