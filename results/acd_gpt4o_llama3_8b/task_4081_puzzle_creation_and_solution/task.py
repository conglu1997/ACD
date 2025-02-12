class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "type": "logical",
                "prompt": "Create a new logical puzzle involving a scenario with three different colored hats (red, blue, green) and three people who need to guess the color of their hats based on specific rules and clues. Ensure the puzzle is challenging and requires logical deduction to solve."
            },
            "2": {
                "type": "mathematical",
                "prompt": "Create a new mathematical puzzle involving a sequence of numbers where the participant needs to find the next number in the sequence based on a hidden pattern. The pattern should be non-trivial and require a clear explanation."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Task: Create a {t['type']} puzzle based on the following prompt: {t['prompt']}

Ensure the puzzle is challenging, original, and non-trivial. Then, provide a detailed step-by-step solution to the puzzle you created, explaining the reasoning or mathematical principles used.

Submit your responses in the following format:

1. Puzzle:
[Your created puzzle here]

2. Solution:
[Your solution here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The created puzzle should be coherent, challenging, original, and align with the given prompt.",
            "The solution should be accurate, detailed, and clearly explain the reasoning or mathematical principles used in a step-by-step manner."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
