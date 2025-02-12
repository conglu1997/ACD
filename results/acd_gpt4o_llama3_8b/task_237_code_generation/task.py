class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"requirements": "Write a Python function named 'filter_even_numbers' that takes a list of integers and returns a new list containing only the even numbers from the input list."},
            "2": {"requirements": "Write a Python function named 'char_frequency' that takes a string and returns a dictionary where the keys are the characters in the string and the values are the number of times each character appears in the string."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following task based on the given requirements:

Requirements:
{t['requirements']}

Generate a Python function that meets the requirements. Ensure that the function is:
1. Named as specified in the requirements.
2. Syntactically correct and logically sound.
3. Performs the specified task correctly.

Submit your function as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        import ast

        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The function should be named correctly.",
            "The function should be syntactically correct.",
            "The function should logically meet the requirements.",
            "The function should perform the specified task correctly."
        ]
        # Parse the function to ensure it is syntactically correct
        try:
            ast.parse(submission)
            return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
        except SyntaxError:
            return 0.0
