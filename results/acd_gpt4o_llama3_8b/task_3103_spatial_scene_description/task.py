class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "description": "A room with a rectangular table in the center, a wooden chair to the left of the table, a large window on the wall opposite the chair, and a tall bookshelf next to the window."
            },
            "2": {
                "description": "A park with a circular fountain in the middle, a wooden bench to the right of the fountain, a tall tree behind the bench, and a playground with swings to the left of the fountain."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are given the following description of a scene:

Description: {t['description']}

Your task is to answer the following questions based on the description:
1. What is to the left of the central object?
2. What is located opposite the object to the left of the central object?

Submit your answers as plain text strings in the following format:
1) [Your answer]
2) [Your answer]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The answers should correctly identify the objects based on the spatial relationships described in the text."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
