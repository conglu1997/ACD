class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task_type": "identify", "scene": "A living room with a sofa, a coffee table, and a lamp. The sofa is to the left of the coffee table, and the lamp is on the coffee table.", "question": "Identify the spatial relationships between the objects in the scene."},
            "2": {"task_type": "generate", "description": "Generate a new arrangement for a bedroom with a bed, a nightstand, and a bookshelf. Ensure the bed is in the center of the room, the nightstand is to the left of the bed, and the bookshelf is against the wall opposite the bed.", "criteria": "The arrangement should follow the specified spatial relationships."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task_type"] == "identify":
            instructions = f"""Your task is to identify the spatial relationships between the objects in the following scene:

Scene: {t['scene']}

Question: {t['question']}

Provide your answer in plain text format, clearly describing the spatial relationships between the objects (e.g., 'The sofa is to the left of the coffee table, and the lamp is on the coffee table.')."""
        else:
            instructions = f"""Your task is to generate a new arrangement for a bedroom based on the following description:

{t['description']}

Ensure the arrangement follows the specified spatial relationships and is formatted as a list of spatial relationships. For example: 'The bed is in the center of the room, the nightstand is to the left of the bed, and the bookshelf is against the wall opposite the bed.'"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["task_type"] == "identify":
            criteria = ["The response should correctly identify the spatial relationships between the objects in the given scene."]
        else:
            criteria = ["The generated arrangement should follow the specified spatial relationships."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
