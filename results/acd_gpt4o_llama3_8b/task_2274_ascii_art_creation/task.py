class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "Create an ASCII art of a simple house. The house should have a door, a window, and a triangular roof."},
            "2": {"description": "Create an ASCII art of a tree. The tree should have a trunk and a canopy."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        description = t["description"]
        return f"""Create an ASCII art representation based on the following description:

Description: {description}

Submit your ASCII art as a plain text string in the following format:

Example:
House:
  /\
 /  \
/____\
|    |
|____|

Tree:
  /\
 /  \
/____\
  ||
  ||

Your ASCII art should be recognizable and coherent."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The ASCII art should match the description provided.", "The ASCII art should be recognizable and coherent."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
