class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "a simple house with a triangular roof, a square body, and a door in the middle"},
            "2": {"description": "a tree with a round canopy and a straight trunk"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate ASCII art based on the following description: '{t['description']}'. Ensure the art is clear and resembles the described object. The ASCII art should fit within a 10x10 grid. For example, if the description is 'a simple house with a triangular roof, a square body, and a door in the middle', the ASCII art could look like this:

   /\
  /  \
 /____\
 |    |
 |____|

Submit your ASCII art as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The ASCII art should have a triangular roof, a square body, and a door in the middle for the house.",
            "The ASCII art should have a round canopy and a straight trunk for the tree.",
            "The ASCII art should be visually recognizable and clear.",
            "The ASCII art should fit within a 10x10 grid."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
