class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "description": "Imagine a room with a round table in the center, a wooden chair to the left of the table, and a large window on the wall directly opposite the chair. Describe the spatial relationships in detail and suggest a new arrangement where the chair is next to the window instead.",
                "initial_scene": "A room with a round table in the center, a wooden chair to the left of the table, and a large window on the wall directly opposite the chair.",
                "new_constraint": "The chair is next to the window."
            },
            "2": {
                "description": "Visualize a garden with a large oak tree in the middle, an iron bench under the tree, and a stone fountain 10 feet to the right of the tree. Describe the spatial relationships in detail and propose a new arrangement where the bench is next to the fountain.",
                "initial_scene": "A garden with a large oak tree in the middle, an iron bench under the tree, and a stone fountain 10 feet to the right of the tree.",
                "new_constraint": "The bench is next to the fountain."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Read the following scene description carefully and describe the spatial relationships in detail. Then, rearrange the scene based on the given new constraint and describe the new spatial relationships. \n\nInitial Scene: {t['initial_scene']}\nNew Constraint: {t['new_constraint']}\n\nYour response should include: \n1. Detailed Description: A detailed description of the initial spatial relationships, specifying the positions and relative distances of objects.\n2. New Arrangement: A new detailed description of the spatial relationships after applying the new constraint, ensuring logical coherence. \n\nSubmit your response as a plain text string in the following format:\n\nDetailed Description: [Your detailed description here]\nNew Arrangement: [Your new arrangement here]"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The detailed description should accurately reflect the initial spatial relationships, specifying positions and relative distances.",
            "The new arrangement should respect the new constraint and logically describe the updated spatial relationships."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
