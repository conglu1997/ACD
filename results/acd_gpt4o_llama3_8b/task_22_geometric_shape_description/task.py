class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"shape": "triangle", "properties": {"base": 5, "height": 8}},
            "2": {"shape": "rectangle", "properties": {"length": 7, "width": 3}},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        shape = t['shape']
        properties = t['properties']
        properties_str = ', '.join([f'{k}: {v}' for k, v in properties.items()])
        return f"""Generate a detailed textual description of a {shape} with the following properties: {properties_str}. The description should be clear, accurate, and include all given properties. Make sure the description is detailed and coherent. For example, a triangle with a base of 5 and height of 8 could be described as 'A triangle with a base of 5 units and a height of 8 units. The base lies horizontally, while the height is measured vertically from the base to the opposite vertex.' Similarly, a rectangle with a length of 7 and width of 3 could be described as 'A rectangle with a length of 7 units and a width of 3 units. The longer sides are 7 units each, and the shorter sides are 3 units each, forming right angles at each corner.' Submit your description as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0
