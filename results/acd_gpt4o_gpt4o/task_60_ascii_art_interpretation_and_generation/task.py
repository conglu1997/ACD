class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "A small house with a triangular roof, a rectangular body, a door in the center, and a window on each side of the door.", "art": None},
            "2": {"description": None, "art": "  /\  \n /  \ \n/____\ \n| _  _ |\n||_||_||\n|_____|"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["description"]:
            return f"""Create an ASCII art representation of the following description:

{t["description"]}

Ensure that the ASCII art is clear, accurate, and matches the description closely."""
        else:
            return f"""Provide a textual description of the following ASCII art:

{t["art"]}

Ensure that the description is clear, detailed, and accurately represents the ASCII art."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The ASCII art should match the description closely.", "The textual description should be detailed and accurate."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
