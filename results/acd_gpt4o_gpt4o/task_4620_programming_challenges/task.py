class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem": "Write a Python function that takes a list of integers and returns a new list containing only the even numbers from the original list.", "example": "Input: [1, 2, 3, 4, 5, 6], Output: [2, 4, 6]"},
            "2": {"problem": "Write a Python function that determines if a given string is a palindrome (a string that reads the same forwards and backwards).", "example": "Input: 'racecar', Output: True; Input: 'hello', Output: False"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to write a Python function to solve the following problem:

Problem: {t['problem']}
Example: {t['example']}

Provide your solution in plain text format, including the function definition and any necessary comments to explain your code."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The code should correctly solve the problem as described.", "The code should be syntactically correct and executable."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
