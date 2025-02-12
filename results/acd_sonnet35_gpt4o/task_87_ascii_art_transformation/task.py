import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        subjects = ["castle", "spaceship", "underwater scene", "cityscape"]
        transformations = ["rotate 90 degrees clockwise", "mirror horizontally", "invert (replace spaces with '#' and vice versa)", "scale up by 2x"]
        tasks = {
            "1": {
                "operation": "create",
                "subject": random.choice(subjects),
                "size": "15x15",
                "required_elements": random.sample(["at least one curve", "symmetry", "nested shapes", "perspective"], 2)
            },
            "2": {
                "operation": "transform_and_analyze",
                "initial_art": """
      _____
     /     \
    /       \
   /  ^   ^  \
  |  (o) (o)  |
  (     <     )
   |  \___/  |
    \_____/
   ____|_|____
  /    | |    \
 /     | |     \
/______|_|______\
""",
                "transformation": random.choice(transformations)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['operation'] == 'create':
            return f"Create an ASCII art representation of a {t['subject']} using a {t['size']} character grid. Your art must include {' and '.join(t['required_elements'])}. Use only standard ASCII characters. Your response should follow this format:\n\nASCII Art:\n[Your ASCII art here]\n\nExplanation:\n[A brief explanation of your design choices and how you incorporated the required elements]\n"
        elif t['operation'] == 'transform_and_analyze':
            return f"Given the following ASCII art:\n\n{t['initial_art']}\n\n1. Transform this ASCII art by applying the following operation: {t['transformation']}.\n2. Analyze the original and transformed ASCII art.\n\nYour response should follow this format:\n\nTransformed ASCII Art:\n[Your transformed ASCII art here]\n\nTransformation Explanation:\n[A brief explanation of how you performed the transformation, including any challenges you faced]\n\nAnalysis:\n[Compare and contrast the original and transformed ASCII art, discussing aspects such as symmetry, balance, visual impact, and how the transformation affected the representation of the original object]\n"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The submission must include ASCII art that matches the given instructions",
            "The ASCII art should be visually recognizable and coherent",
            "For the 'create' task, the ASCII art must incorporate all required elements specified in the instructions",
            "The explanation provided should be clear, relevant, and demonstrate understanding of the design choices or transformation process",
            "For transformation tasks, the transformed art should accurately reflect the requested operation",
            "The analysis should demonstrate a deep understanding of visual elements in ASCII art and how they are affected by transformations",
            "The response should strictly follow the specified format",
            "The ASCII art should make creative and effective use of ASCII characters to represent the subject or transformation"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
