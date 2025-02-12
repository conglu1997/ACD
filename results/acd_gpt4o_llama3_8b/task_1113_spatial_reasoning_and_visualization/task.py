class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "layout": "Imagine a room with the following items: A rectangular table is in the center, a large window is on the north wall, a tall bookshelf is on the east wall, and a wide door is on the south wall. Describe the room in detail, including the positions, relative sizes, and any additional details you think are relevant."
            },
            "2": {
                "manipulation": "You are given a 3x3 grid where each cell can be occupied by a different object. Initially, the grid is empty. Place the following objects in the grid according to the instructions: 1) A chair in the center cell. 2) A lamp to the immediate left of the chair. 3) A plant in the top-right corner. Describe the final arrangement of objects in the grid, including their positions relative to each other."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'layout' in t:
            return f"""Describe the following room layout in detail based on the provided information:

Layout: {t['layout']}

Ensure that your description includes the positions, relative sizes, and any additional details to make the room visualization clear. Submit your response as a plain text string in the format:

Description:
[Your description]"""
        elif 'manipulation' in t:
            return f"""Perform the following spatial manipulation task based on the provided instructions:

Instructions: {t['manipulation']}

Ensure that your description includes the final positions of all objects in the grid, including their positions relative to each other. Submit your response as a plain text string in the format:

Final Grid:
[Your description of the grid]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'layout' in t:
            criteria = ["The description should clearly detail the positions and relative sizes of the items in the room.", "The room layout should be easily visualizable based on the description.", "The description should include additional relevant details to enhance visualization."]
        else:
            criteria = ["The description should accurately reflect the final positions of all objects in the grid.", "The grid layout should be correct based on the provided instructions.", "The description should include the positions of objects relative to each other."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
