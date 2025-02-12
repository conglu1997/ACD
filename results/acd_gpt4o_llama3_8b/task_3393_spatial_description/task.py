class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {'scene': 'There is a table in the center of the room. On the table, there is a vase with flowers. To the left of the table, there is a chair. To the right of the table, there is a bookshelf. The window is located behind the table, and a lamp is on the bookshelf. There is a painting on the wall opposite the window.'},
            '2': {'scene': 'In the park, there is a large tree in the middle. To the north of the tree, there is a bench. To the south of the tree, there is a fountain. To the east of the tree, there is a playground. To the west of the tree, there is a statue. Near the statue, there is a small pond.'}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        scene = t['scene']
        return f"""Describe the spatial relationships between the objects in the following scene:

{scene}

Your description should clearly explain where each object is located relative to others in the scene. Ensure your description is detailed, well-structured, and accurate. Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The description should accurately represent the spatial relationships described in the scene.",
            "The description should be clear and well-structured."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
