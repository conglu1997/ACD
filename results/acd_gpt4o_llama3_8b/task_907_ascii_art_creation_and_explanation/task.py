class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "theme": "forest",
                "example": "Create ASCII art representing a forest."
            },
            "2": {
                "theme": "space",
                "example": "Create ASCII art representing outer space."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create ASCII art based on the following theme: '{t['theme']}'. The art should fit within a 40x20 character grid. After creating the art, explain the design choices you made, such as which characters you used to represent different elements, how you arranged them, and why you chose this specific representation.

Submit your response in the following format:

ASCII Art:
[Your ASCII art here (must fit within 40x20 grid)]

Explanation:
[Your explanation here]

Example (for a theme of 'tree'):
ASCII Art:
  ^  
 /|\ 
/ | \ 
Explanation:
I used the '^' symbol to represent the top of the tree and '/' and '\' to represent the branches, creating a simple and recognizable tree shape. The vertical line '|' serves as the trunk, providing structure to the tree."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The ASCII art should be relevant to the given theme.",
            "The ASCII art should fit within the 40x20 character grid.",
            "The explanation should clearly describe the design choices made.",
            "The design choices should contribute to the overall representation of the theme."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
