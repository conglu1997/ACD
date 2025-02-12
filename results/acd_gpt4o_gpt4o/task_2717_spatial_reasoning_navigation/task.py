class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"environment": "You are in a rectangular room with a door on the north wall and a window on the east wall. There is a table in the center of the room and a chair beside it. Describe how you would navigate from the door to the window without touching the table."},
            "2": {"environment": "You are in a park with a fountain in the middle. There are benches around the fountain, and trees forming a circle around the benches. Describe how you would walk from the entrance of the park to a bench, passing by the fountain."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a detailed description of how to navigate the given environment based on the following scenario:

Environment: {t['environment']}

Your description should include:
1. Clear and precise directions using spatial terms (e.g., left, right, forward, backward).
2. Descriptions of key landmarks or objects encountered along the way.
3. Any necessary considerations or precautions to avoid obstacles.

Ensure your description is accurate, coherent, and easy to follow. Provide your response in plain text format and structure it in a numbered list format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The description should accurately reflect the environment and provide clear navigation instructions.", "The spatial terms and landmarks mentioned should be correct and relevant."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
