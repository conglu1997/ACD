class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "type": "spatial_description",
                "prompt": "Imagine a room that is 5 meters by 5 meters with a height of 3 meters. In the center of the room, there is a circular table with a diameter of 2 meters and a height of 0.75 meters. To the left of the table, there is a chair positioned 1 meter away, and the chair is 0.5 meters high. Describe the spatial layout and the positions of the objects in relation to each other. Consider the distances and orientations accurately."
            },
            "2": {
                "type": "spatial_manipulation",
                "prompt": "Given the same room and objects as before, imagine moving the chair to the right side of the table, 1 meter away from it. Describe the new spatial layout and the positions of the objects in relation to each other. Consider the distances and orientations accurately."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["type"] == "spatial_description":
            prompt = t["prompt"]
            instructions = f"""Your task is to describe the spatial layout of the given scenario.

Prompt: {prompt}

Your description should be:
1. Clear and precise.
2. Include all objects and their spatial relationships.
3. Understandable to someone who cannot see the layout.
4. Consider distances and orientations accurately.

Provide your description in plain text format.
"""
        elif t["type"] == "spatial_manipulation":
            prompt = t["prompt"]
            instructions = f"""Your task is to describe the new spatial layout after making the specified changes.

Prompt: {prompt}

Your description should be:
1. Clear and precise.
2. Include all objects and their new spatial relationships.
3. Understandable to someone who cannot see the layout.
4. Consider distances and orientations accurately.

Provide your description in plain text format.
"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The description should be clear and precise.",
            "The description should include all objects and their spatial relationships.",
            "The description should be understandable to someone who cannot see the layout.",
            "The description should consider distances and orientations accurately."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
