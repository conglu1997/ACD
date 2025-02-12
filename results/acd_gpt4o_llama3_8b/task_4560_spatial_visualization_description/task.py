class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "context": "a living room",
                "objects": ["sofa", "coffee table", "television", "bookshelf", "lamp"],
                "relationships": ["next to the", "in front of the", "behind the", "to the left of the", "to the right of the"]
            },
            "2": {
                "context": "a park",
                "objects": ["bench", "fountain", "tree", "flower bed", "statue"],
                "relationships": ["next to the", "in front of the", "behind the", "to the left of the", "to the right of the"]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Describe the spatial arrangement and visual relationships between the following objects in the context of {t['context']}. Be detailed in your description, ensuring that the relative positions and relationships between the objects are clear and logically coherent. Use the following spatial relationships where appropriate: {', '.join(t['relationships'])}.

Objects: {', '.join(t['objects'])}

Example format:

Description: The sofa is next to the coffee table. The television is in front of the sofa. The bookshelf is behind the lamp, which is to the left of the sofa."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = ["The description should clearly convey the spatial arrangement of the objects.", "The relationships between objects should be logically coherent.", "The description should be detailed and vivid."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
