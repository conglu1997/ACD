class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "problem": "Generate a Python program that creates a visual representation (ASCII art) of a Christmas tree. The tree should have at least 5 levels and a base.",
                "answer": "N/A"
            },
            "2": {
                "problem": "Write a Python script that simulates a simple text-based game where the player navigates a maze. The maze should be at least 5x5 in size and the player should be able to move up, down, left, and right.",
                "answer": "N/A"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Write a Python program to solve the following problem:

Problem:
{t['problem']}

Your program should be syntactically correct and logically consistent. Ensure that it adheres to good coding practices and solves the problem effectively. Submit your response as a plain text string containing the Python code."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The program should be syntactically correct.",
            "The program should logically solve the problem as described.",
            "The solution should be creative and effective."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
