class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "Draw a diagram of a simple house layout with a kitchen, living room, and two bedrooms. The kitchen should be adjacent to the living room, and the bedrooms should be next to each other."},
            "2": {"description": "Create a flowchart for the process of making a cup of tea. The steps include boiling water, placing a teabag in a cup, pouring hot water into the cup, and letting it steep."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        description = t["description"]
        return f"""Create a diagram based on the following description:

{description}

Your response should be a base64-encoded image string that accurately represents the described layout or process. Ensure that all elements are clearly labeled and positioned according to the description."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The diagram should accurately represent the spatial relationships described in the task.",
            "All elements in the diagram should be clearly labeled.",
            "All elements should be correctly positioned according to the description."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
