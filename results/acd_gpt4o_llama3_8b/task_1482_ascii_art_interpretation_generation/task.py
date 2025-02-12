class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "task_type": "interpretation",
                "ascii_art": """
   _____
  /     \
 /       \
|         |
|  O   O  |
|    ^    |
|  \___/  |
 \_______/
"""
            },
            "2": {
                "task_type": "generation",
                "criteria": "Create a simple ASCII art representation of a house with a door and two windows."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task_type'] == 'interpretation':
            return f"""Interpret the following ASCII art and describe what you see in plain text:

{t['ascii_art']}

Your description should be clear and accurately represent all the elements and structure of the ASCII art. Describe each part of the image in detail, such as the shapes, positions, and any notable features."""
        elif t['task_type'] == 'generation':
            return """Generate ASCII art based on the following criteria:

Criteria: {t['criteria']}

Your ASCII art should be clear, recognizable, and meet the specified criteria. Ensure that the house has distinct features like a roof, walls, a door, and two windows. Submit your response as a plain text string in the following format:

ASCII Art:
[Your ASCII art here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['task_type'] == 'interpretation':
            criteria = ["The description should accurately represent the ASCII art, including all its elements and structure in detail."]
        elif t['task_type'] == 'generation':
            criteria = ["The ASCII art should clearly represent a house with a roof, walls, a door, and two windows.", "The ASCII art should be recognizable and meet the specified criteria."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
