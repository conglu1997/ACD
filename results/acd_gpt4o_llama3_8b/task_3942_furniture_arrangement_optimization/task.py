class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"room_dimensions": "10x12 feet", "furniture": ["sofa", "coffee table", "TV stand", "bookshelf"], "constraints": ["TV stand must be against the wall", "sofa should face the TV stand"]},
            "2": {"room_dimensions": "15x20 feet", "furniture": ["dining table", "6 chairs", "sideboard", "cabinet"], "constraints": ["dining table should be at the center", "cabinet must be against the wall"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        room_dimensions = t['room_dimensions']
        furniture = ', '.join(t['furniture'])
        constraints = '\n'.join(t['constraints'])
        return f"""You are given the dimensions of a room and a list of furniture items to arrange within the room. Your task is to provide an optimal arrangement that ensures functionality and aesthetic appeal. Consider the given constraints while arranging the furniture.

Room Dimensions: {room_dimensions}
Furniture: {furniture}
Constraints:\n{constraints}

Submit your response as a plain text string in the following format:

Furniture Arrangement:
[Describe your arrangement in detail, including the positions and orientations of each furniture item.]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The arrangement should adhere to the given room dimensions and constraints.",
            "The arrangement should be functional and aesthetically appealing.",
            "The description should be clear and detailed, specifying the positions and orientations of each furniture item.",
            "The arrangement should make efficient use of space without overcrowding."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
