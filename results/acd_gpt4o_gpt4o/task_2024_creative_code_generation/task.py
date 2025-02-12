class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Write a Python function that generates a random poem using a predefined list of words. The poem should have at least 4 lines and each line should have a different number of words."},
            "2": {"prompt": "Write a Python script that creates a simple text-based game where the player navigates a maze. The maze should be represented as a 2D list and the player should be able to move up, down, left, or right."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return """Your task is to generate a code snippet based on the following prompt:

{0}

Ensure that your code is functional, creative, and meets the requirements specified in the prompt. Provide your code in plain text format, ensuring proper indentation and readability.""".format(t["prompt"])

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The code should be functional and run without errors.",
            "The code should meet the specific requirements of the prompt.",
            "The code should demonstrate creativity in its implementation." ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
